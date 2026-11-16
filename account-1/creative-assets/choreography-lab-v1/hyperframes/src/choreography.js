// BeatGaler — Choreography Lab V1
// One scene, three motion models. Every pose is a pure function of time t.
//
//   A  rigid helix orbit, fixed camera        (control)
//   B  independent trajectories + depth strata, fixed camera
//   C  B's object motion unchanged + animated 3D camera
//
// Shared by all variants: covers, card size, layout seed, global angular
// velocity profile, background, fog, lens (40° vertical FOV) and duration.
// Nothing here reads a clock, a timer or an unseeded random number.
import * as THREE from "../lib/three.module.min.js";

export const DURATION = 6.0;
export const WIDTH = 720;
export const HEIGHT = 1280;
export const FOV = 40;
export const MASTER_CAMERA = { pos: [0, 0, 9.0], target: [0, 0, 0] };
export const COVERS = [
  ...Array.from({ length: 20 }, (_, i) => `cover-${String(i + 1).padStart(2, "0")}.jpg`),
  ...Array.from({ length: 4 }, (_, i) => `cover-${String(i + 21).padStart(2, "0")}.avif`),
];
const N = COVERS.length;
const BG = 0x07070a;

// ---------------------------------------------------------------- helpers
const clamp01 = (x) => Math.min(1, Math.max(0, x));
const lerp = (a, b, u) => a + (b - a) * u;
const easeOutExpo = (x) => (x >= 1 ? 1 : 1 - Math.pow(2, -10 * x));
const easeOutQuint = (x) => 1 - Math.pow(1 - x, 5);
const easeInOutCubic = (x) => (x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2);
const easeInOutSine = (x) => -(Math.cos(Math.PI * x) - 1) / 2;
// Decelerating landing with zero start slope: a card already moving on the
// orbit leaves it without a velocity kick (QA v1 found a 72 px/frame² snap
// when easeOutQuint started from the live orbit pose).
const easeSmoothOut = (x) => 1 - Math.pow(1 - x, 4) * (1 + 4 * x);

function mulberry32(a) {
  return function () {
    a |= 0;
    a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

// Cubic Hermite through (time, value) knots with finite-difference tangents.
// endTangentZero: start and end velocity are zero (ease in / ease out).
function hermiteTrack(knots, endTangentZero = true) {
  const n = knots.length;
  const m = knots.map((k, i) => {
    if (endTangentZero && (i === 0 || i === n - 1)) return k[1].map(() => 0);
    const a = knots[Math.max(0, i - 1)];
    const b = knots[Math.min(n - 1, i + 1)];
    return k[1].map((_, d) => (b[1][d] - a[1][d]) / (b[0] - a[0]));
  });
  return (t) => {
    if (t <= knots[0][0]) return knots[0][1].slice();
    if (t >= knots[n - 1][0]) return knots[n - 1][1].slice();
    let i = 0;
    while (t > knots[i + 1][0]) i++;
    const [t0, p0] = knots[i];
    const [t1, p1] = knots[i + 1];
    const h = t1 - t0;
    const s = (t - t0) / h;
    const h00 = 2 * s ** 3 - 3 * s ** 2 + 1;
    const h10 = s ** 3 - 2 * s ** 2 + s;
    const h01 = -2 * s ** 3 + 3 * s ** 2;
    const h11 = s ** 3 - s ** 2;
    return p0.map((_, d) => h00 * p0[d] + h10 * h * m[i][d] + h01 * p1[d] + h11 * h * m[i + 1][d]);
  };
}

function bezier3(p0, p1, p2, p3, u) {
  const v = 1 - u;
  return new THREE.Vector3()
    .addScaledVector(p0, v * v * v)
    .addScaledVector(p1, 3 * v * v * u)
    .addScaledVector(p2, 3 * v * u * u)
    .addScaledVector(p3, u * u * u);
}

// -------------------------------------------- shared global angular motion
// Angular velocity (rad/s) of the helix. Same profile for A, B and C, so any
// difference between variants comes from structure and camera, not tempo.
// Knot values use zero slopes -> each segment is an ease-in-out.
const OMEGA_KNOTS = [
  [0.0, 2.2], [1.4, 1.0], [3.0, 1.05], [3.9, 2.8], [4.8, 0.9], [5.6, 0.3], [6.0, 0.25],
];
function omega(t) {
  let i = 0;
  if (t <= 0) return OMEGA_KNOTS[0][1];
  if (t >= DURATION) return OMEGA_KNOTS[OMEGA_KNOTS.length - 1][1];
  while (t > OMEGA_KNOTS[i + 1][0]) i++;
  const [t0, w0] = OMEGA_KNOTS[i];
  const [t1, w1] = OMEGA_KNOTS[i + 1];
  const s = (t - t0) / (t1 - t0);
  return lerp(w0, w1, s * s * (3 - 2 * s));
}
// Integrated angle table, built once (simulate at load, look up at t).
const THETA_DT = 1 / 1200;
const THETA = (() => {
  const n = Math.ceil(DURATION / THETA_DT) + 2;
  const a = new Float64Array(n);
  for (let i = 1; i < n; i++) {
    const tm = (i - 0.5) * THETA_DT;
    a[i] = a[i - 1] + omega(tm) * THETA_DT;
  }
  return a;
})();
function globalAngle(t) {
  const x = clamp01(t / DURATION) * DURATION / THETA_DT;
  const i = Math.floor(x);
  const f = x - i;
  return lerp(THETA[i], THETA[Math.min(i + 1, THETA.length - 1)], f);
}

// ------------------------------------------------------------- layout seed
const HELIX_SCALE = 0.95; // card edge in world units while orbiting
const GRID_SCALE = 0.76; // card edge when resting in the gallery grid
const GRID = { cols: 4, rows: 6, step: 0.86 };

function buildCards() {
  const rnd = mulberry32(20261105);
  const strata = { radius: [2.35, 1.75, 1.2], speed: [1.0, 0.82, 0.66], drift: [0.08, 0.05, 0.03] };
  // shuffled stratum assignment (no visible i%3 pattern)
  const order = Array.from({ length: N }, (_, i) => i).sort((a, b) => mulberry32(a * 977 + 13)() - mulberry32(b * 977 + 13)());
  const cards = [];
  for (let i = 0; i < N; i++) {
    const s = order.indexOf(i) % 3;
    const base = (i * 2 * Math.PI) / 8;
    cards.push({
      i,
      cover: COVERS[i],
      stratum: s,
      // A (rigid): uniform helix, one radius, radial facing
      a: { theta: base, y: (i - 11.5) * 0.34, r: 1.75 },
      // B/C (independent)
      r: strata.radius[s] * (1 + (rnd() - 0.5) * 0.12),
      k: strata.speed[s] * (1 + (rnd() - 0.5) * 0.14),
      phi: base + (rnd() - 0.5) * 0.5,
      y0: (i - 11.5) * 0.34 + (rnd() - 0.5) * 0.16,
      drift: strata.drift[s],
      yaw: (rnd() - 0.5) * 1.2, // ±34°: some faces edge-on, some frontal
      pitch: (rnd() - 0.5) * 0.7,
      wobble: rnd() * Math.PI * 2,
      dep: 0, // entrance departure (set below)
      entDur: 0.85 + rnd() * 0.2,
      jitter: rnd(),
      jitter2: rnd(),
    });
  }
  // entrance: far stratum leaves the deck first, near last (near overlaps far)
  const entranceRank = cards.slice().sort((p, q) => q.stratum - p.stratum || p.i - q.i);
  entranceRank.forEach((c, rank) => {
    c.rank = rank;
    c.dep = 0.12 + rank * 0.042 + (c.jitter - 0.5) * 0.02;
    c.deck = new THREE.Vector3(0.0 + (rank - 12) * 0.004, -2.9 + rank * 0.012, 0.6 + rank * 0.02);
  });
  // heroes: four near-stratum cards closest to the vertical centre
  const heroes = cards.filter((c) => c.stratum === 0).sort((p, q) => Math.abs(p.y0) - Math.abs(q.y0)).slice(0, 4);
  // fly-by points near the lens (master camera sits at z = 9)
  const pass = [
    [-0.95, 0.85, 6.1], [1.05, -0.4, 5.7], [-0.5, -1.15, 5.9], [0.85, 0.6, 5.5],
  ];
  const heroSlots = [[1, 2], [2, 3], [1, 3], [2, 2]];
  heroes.forEach((c, j) => {
    c.hero = j;
    c.gridDep = 3.3 + j * 0.17 + (c.jitter2 - 0.5) * 0.05;
    c.gridDur = 1.95 + ((j * 7) % 4) * 0.07;
    c.pass = new THREE.Vector3(...pass[j]);
    c.slot = heroSlots[j];
  });
  // remaining slots, assigned by where each card is at t = 4.0 (top rows <- top cards)
  const free = [];
  for (let r = 0; r < GRID.rows; r++) for (let col = 0; col < GRID.cols; col++) {
    if (!heroSlots.some(([hc, hr]) => hc === col && hr === r)) free.push([col, r]);
  }
  const rest = cards.filter((c) => c.hero === undefined);
  rest.sort((p, q) => helixPosB(q, 4.0).y - helixPosB(p, 4.0).y);
  for (let r = 0; r < GRID.rows; r++) {
    const rowSlots = free.filter(([, rr]) => rr === r);
    const rowCards = rest.splice(0, rowSlots.length).sort((p, q) => helixPosB(p, 4.0).x - helixPosB(q, 4.0).x);
    rowCards.forEach((c, k) => (c.slot = rowSlots[k]));
  }
  // shortest flights leave first: an organic gather, not a raster wipe
  cards.filter((c) => c.hero === undefined)
    .sort((p, q) => helixPosB(p, 4.0).distanceTo(slotPos(p.slot)) - helixPosB(q, 4.0).distanceTo(slotPos(q.slot)))
    .forEach((c, order) => {
      c.gridDep = 3.9 + order * 0.038 + (c.jitter2 - 0.5) * 0.06;
      c.gridDur = 0.78 + c.jitter * 0.2;
    });
  return cards;
}

function slotPos(slot) {
  const [col, row] = slot;
  return new THREE.Vector3((col - (GRID.cols - 1) / 2) * GRID.step, ((GRID.rows - 1) / 2 - row) * GRID.step, 0);
}

// ------------------------------------------------------------ motion models
const _e = new THREE.Euler();
const _q = new THREE.Quaternion();
const IDENTITY = new THREE.Quaternion();
const DECK_Q = new THREE.Quaternion().setFromEuler(new THREE.Euler(-1.08, 0.18, 0.05, "YXZ"));

// The helix axis leans away from the lens so its turns read as stacked
// ellipses with visible gaps, not a flat wall. Shared by every variant.
const TILT = new THREE.Quaternion().setFromEuler(new THREE.Euler(-0.32, 0, 0, "YXZ"));

function helixPosB(c, t) {
  const th = c.phi + c.k * globalAngle(t);
  return new THREE.Vector3(c.r * Math.sin(th), c.y0 + c.drift * t, c.r * Math.cos(th)).applyQuaternion(TILT);
}
function helixQuatB(c, t) {
  const th = c.phi + c.k * globalAngle(t);
  const bank = -0.1 * c.k * omega(t) + 0.06 * Math.sin(2.1 * t + c.wobble);
  return TILT.clone().multiply(new THREE.Quaternion().setFromEuler(_e.set(c.pitch, th + c.yaw, bank, "YXZ")));
}

// A: everything rides one rigid group transform.
function poseA(c, t) {
  const ent = easeOutExpo(clamp01((t - 0.1) / 1.3));
  const groupY = -7 * (1 - ent) + 0.15 * t;
  const th = c.a.theta + globalAngle(t);
  const pos = new THREE.Vector3(c.a.r * Math.sin(th), c.a.y, c.a.r * Math.cos(th)).applyQuaternion(TILT);
  pos.y += groupY;
  const quat = TILT.clone().multiply(new THREE.Quaternion().setFromEuler(_e.set(0, th, 0, "YXZ")));
  return { pos, quat, scale: HELIX_SCALE };
}

// B (and C): per-card entrance, orbit, peel and gallery landing.
function poseB(c, t) {
  const pop = easeOutExpo(clamp01((t - 0.05 - c.rank * 0.012) / 0.4));
  let pos = helixPosB(c, t);
  let quat = helixQuatB(c, t);
  let scale = HELIX_SCALE;
  // 1. unfold from the deck
  const e = easeOutQuint(clamp01((t - c.dep) / c.entDur));
  if (e < 1) {
    const lift = new THREE.Vector3(0, 0, 0.9 * Math.sin(Math.PI * e));
    pos = c.deck.clone().lerp(pos, e).add(lift);
    quat = DECK_Q.clone().slerp(quat, e);
  }
  // 2/3. peel (heroes) or gallery flight (others)
  if (t > c.gridDep) {
    const u0 = clamp01((t - c.gridDep) / c.gridDur);
    const u = c.hero !== undefined ? easeInOutCubic(u0) : easeSmoothOut(u0);
    const atDep = helixPosB(c, c.gridDep);
    const radial = new THREE.Vector3(atDep.x, 0, atDep.z).normalize();
    const slot = slotPos(c.slot);
    let p1, p2;
    if (c.hero !== undefined) {
      p1 = atDep.clone().addScaledVector(radial, 1.1).add(new THREE.Vector3(0, 0, 1.4));
      p2 = c.pass;
    } else {
      p1 = atDep.clone().addScaledVector(radial, 0.4).add(new THREE.Vector3(0, 0, 0.6));
      p2 = slot.clone().add(new THREE.Vector3(0, 0, 0.9));
    }
    pos = bezier3(pos, p1, p2, slot, u); // P0 is the live orbit pose -> continuous
    const settle = easeInOutSine(u);
    quat = quat.clone().slerp(IDENTITY, settle);
    if (c.hero !== undefined) {
      quat.multiply(_q.setFromEuler(_e.set(0, 0, 0.35 * Math.sin(Math.PI * u0), "YXZ")));
    }
    scale = lerp(HELIX_SCALE, GRID_SCALE, easeInOutCubic(u0));
    if (c.hero !== undefined) scale *= 1 + 0.45 * Math.sin(Math.PI * Math.min(1, u0 * 1.15));
  }
  return { pos, quat, scale: scale * pop };
}

// C camera: low and close at the deck, crane up the helix, push in, retreat
// while heroes fly at the lens, then land on the master frame shared with B.
const CAM_POS = hermiteTrack([
  [0.0, [0.6, -2.6, 6.0]],
  [1.3, [2.0, -0.9, 7.4]],
  [2.5, [1.2, 0.8, 6.9]],
  [3.1, [-0.5, 0.4, 6.4]],
  [4.1, [-0.4, 0.2, 8.4]],
  [5.45, [0, 0, 9.0]],
  [6.0, [0, 0, 8.8]],
]);
const CAM_TARGET = hermiteTrack([
  [0.0, [0, -2.6, 0]],
  [1.3, [0, -0.6, 0]],
  [2.5, [0, 0.5, 0]],
  [3.1, [0, 0.3, 0]],
  [4.1, [0, 0.1, 0]],
  [5.45, [0, 0, 0]],
  [6.0, [0, 0, 0]],
]);
const CAM_ROLL = hermiteTrack([[0, [0.0]], [1.3, [0.05]], [2.5, [-0.035]], [3.4, [0.02]], [5.45, [0]], [6, [0]]]);

export const VARIANTS = {
  a: { label: "A · rigid orbit · fixed camera", pose: poseA, camera: "fixed" },
  b: { label: "B · independent trajectories + depth · fixed camera", pose: poseB, camera: "fixed" },
  c: { label: "C · independent trajectories + animated 3D camera", pose: poseB, camera: "animated" },
};

export function cameraAt(variant, t) {
  if (VARIANTS[variant].camera === "fixed") return { pos: MASTER_CAMERA.pos, target: MASTER_CAMERA.target, roll: 0 };
  return { pos: CAM_POS(t), target: CAM_TARGET(t), roll: CAM_ROLL(t)[0] };
}

// ------------------------------------------------------------------- scene
function roundedAlpha() {
  const s = 256;
  const cv = document.createElement("canvas");
  cv.width = cv.height = s;
  const g = cv.getContext("2d");
  g.fillStyle = "#000";
  g.fillRect(0, 0, s, s);
  g.fillStyle = "#fff";
  const r = s * 0.06;
  g.beginPath();
  g.roundRect(2, 2, s - 4, s - 4, r);
  g.fill();
  const tex = new THREE.CanvasTexture(cv);
  return tex;
}

export function createLab(canvas, variant) {
  if (!VARIANTS[variant]) variant = "c";
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: false, preserveDrawingBuffer: true });
  renderer.setPixelRatio(1);
  renderer.setSize(WIDTH, HEIGHT, false);
  renderer.setClearColor(BG, 1);
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  const scene = new THREE.Scene();
  scene.fog = new THREE.Fog(BG, 7.0, 15.5);
  const camera = new THREE.PerspectiveCamera(FOV, WIDTH / HEIGHT, 0.1, 60);
  const cards = buildCards();
  const alpha = roundedAlpha();
  const geo = new THREE.PlaneGeometry(1, 1);
  const loader = new THREE.TextureLoader();
  const loads = [];
  for (const c of cards) {
    // Double-sided print: the back face carries the same art, un-mirrored,
    // slightly darker, so a card seen from behind still reads as a cover.
    const mat = new THREE.MeshBasicMaterial({ color: 0xffffff, alphaMap: alpha, alphaTest: 0.5, side: THREE.FrontSide });
    const backMat = new THREE.MeshBasicMaterial({ color: 0xb4b4b4, alphaMap: alpha, alphaTest: 0.5, side: THREE.BackSide });
    loads.push(
      loader.loadAsync(`assets/covers/${c.cover}`).then((tex) => {
        tex.colorSpace = THREE.SRGBColorSpace;
        tex.anisotropy = 4;
        mat.map = tex;
        const back = tex.clone();
        back.wrapS = THREE.RepeatWrapping;
        back.repeat.x = -1;
        back.offset.x = 1;
        back.needsUpdate = true;
        backMat.map = back;
        mat.needsUpdate = true;
        backMat.needsUpdate = true;
      }),
    );
    const group = new THREE.Group();
    group.add(new THREE.Mesh(geo, mat));
    group.add(new THREE.Mesh(geo, backMat));
    c.obj = group;
    scene.add(group);
  }
  const spec = VARIANTS[variant];

  function applyPose(t) {
    for (const c of cards) {
      const p = spec.pose(c, t);
      c.obj.position.copy(p.pos);
      c.obj.quaternion.copy(p.quat);
      c.obj.scale.setScalar(Math.max(p.scale, 1e-4));
    }
    const cam = cameraAt(variant, t);
    camera.position.set(...cam.pos);
    camera.up.set(Math.sin(cam.roll), Math.cos(cam.roll), 0);
    camera.lookAt(...cam.target);
    camera.updateMatrixWorld();
    scene.updateMatrixWorld();
  }

  function render(t) {
    applyPose(Math.min(Math.max(t, 0), DURATION));
    renderer.render(scene, camera);
  }

  // Ground-truth instrumentation for QA: exact projected corners and depth.
  const corners = [[-0.5, -0.5], [0.5, -0.5], [0.5, 0.5], [-0.5, 0.5]];
  function sample(t) {
    applyPose(t);
    const out = [];
    const v = new THREE.Vector3();
    for (const c of cards) {
      const pts = corners.map(([x, y]) => {
        v.set(x, y, 0).applyMatrix4(c.obj.matrixWorld);
        const dist = v.distanceTo(camera.position);
        v.project(camera);
        return [v.x, v.y, v.z, dist];
      });
      const centre = new THREE.Vector3().setFromMatrixPosition(c.obj.matrixWorld);
      const normal = new THREE.Vector3(0, 0, 1).applyQuaternion(c.obj.quaternion);
      const toCam = camera.position.clone().sub(centre).normalize();
      out.push({
        id: c.cover,
        stratum: c.stratum,
        hero: c.hero ?? null,
        corners: pts,
        world: centre.toArray(),
        camDist: centre.distanceTo(camera.position),
        facing: normal.dot(toCam), // 1 = frontal, 0 = edge-on, <0 = back face
      });
    }
    return { t, camera: camera.position.toArray(), cards: out };
  }

  const ready = Promise.all(loads).then(() => renderer.compileAsync(scene, camera)).then(() => {
    render(0);
    // one readback so a software GPU finishes the first (slowest) draw during setup
    const gl = renderer.getContext();
    gl.readPixels(0, 0, 1, 1, gl.RGBA, gl.UNSIGNED_BYTE, new Uint8Array(4));
  });
  return { variant, label: spec.label, render, sample, ready, cards };
}
