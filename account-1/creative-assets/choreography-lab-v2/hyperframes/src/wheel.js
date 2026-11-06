// BeatGaler — Choreography Lab V2: "rolodex wheel"
//
// Reconstruction study of the Apple Music cover motion (owner decision
// 2026-11-05: get as close to the reference as possible), with BeatGaler's
// own covers and copy. Structure inferred from the reference frames:
//   - ONE ordered wheel of N covers, evenly spaced (rigid, like lab V1 "A");
//   - each cover is a radial page: its plane contains the radial direction
//     and the wheel axis (a rolodex / paddle wheel), so seen near the axis
//     the pages read as thin spokes and, off-axis, as faces;
//   - the pages start bunched (a closed deck) and fan open into the wheel;
//   - the wheel turns continuously while it grows, turns its axis sideways
//     and brings its rim past the lens: the pages flip by like a rolodex;
//   - the wheel leaves upward and the frame clears.
// Times are reference seconds (original Apple file). Every pose is a pure
// function of t; nothing reads a clock or an unseeded random number.
import * as THREE from "../lib/three.module.min.js";

export const DURATION = 6.0;
export const WIDTH = 720;
export const HEIGHT = 1280;
export const COVERS = [
  ...Array.from({ length: 20 }, (_, i) => `cover-${String(i + 1).padStart(2, "0")}.jpg`),
  ...Array.from({ length: 4 }, (_, i) => `cover-${String(i + 21).padStart(2, "0")}.avif`),
];

// ------------------------------------------------------------ parameters
// Everything an art director would tune lives here.
export const RIG = {
  cards: 28, // pages on the wheel (covers repeat after 24)
  page: 0.82, // page edge, world units
  radius: 2.0, // distance from axis to page centre
  // blade pitch: each page turns about its own radial line (turbine blade).
  // With the wheel tilted by the same angle, pages on one side read edge-on
  // and pages on the other side open to full faces, as in the reference.
  bladePitch: -0.55,
  fov: 62,
  camera: [0, 0, 6.2],
  appear: 1.22, // first frame with pages (reference: 1.20-1.23 s)
  leave: 4.5, // wheel is off frame from here (reference: clear by ~4.4 s)
  phase0: -0.9, // wheel angle of the deck when it appears (radians, wheel space)
  // fraction of the full circle the pages occupy (pages join the wheel from one end)
  spread: [[1.22, [0.35]], [1.3, [0.55]], [1.42, [0.8]], [1.56, [0.96]], [1.66, [1.0]]],
  // wheel angular velocity, rad/s (sign sets the turning direction). At the
  // climax ~1 page passes per frame (reference "riffle"): 2*PI/cards*30 ~ 6.7
  omega: [[1.22, [-2.0]], [1.6, [-2.6]], [3.0, [-2.5]], [3.45, [-3.2]], [3.7, [-6.0]], [4.3, [-6.5]], [4.6, [-6.5]]],
  // wheel centre (world)
  position: [
    [1.22, [0.3, 1.0, -1.0]],
    [1.45, [0.15, 1.05, -0.4]],
    [1.72, [0.05, 1.05, 0.0]],
    [3.0, [0.05, 1.05, 0.5]],
    [3.4, [0.6, 0.95, 1.6]],
    [3.72, [1.45, 0.95, 3.4]],
    [4.02, [1.45, 1.0, 3.5]],
    [4.3, [1.45, 3.8, 3.0]],
    [4.5, [1.45, 7.0, 2.4]],
  ],
  // ring pose, Euler XYZ radians + screen roll (fitted 2026-11-06 by mask IoU
  // at 1.9/2.2/2.6 s: 0.51, was 0.25). Held for the whole shot: the climax is
  // reached by tipping the same wheel, never by swinging its axis sideways.
  rotation: [[1.22, [-0.75, 0.0, 0.0, 0.0]], [4.5, [-0.75, 0.0, 0.0, 0.0]]],
  // rigid moves of the whole wheel: [tip about the screen x axis, final roll].
  // Entrance: opens from edge-on. Climax: the bottom-left rim comes toward the
  // lens and we look down on it while the spin carries pages up and away
  // (reference 3.33-3.73 s: the lower row slides left and lies back).
  tip: [
    [1.22, [-0.8, 0.45]],
    [1.42, [-0.3, 0.3]],
    [1.72, [0.0, 0.25]],
    [3.0, [0.0, 0.25]],
    [3.72, [-0.35, 0.6]],
    [4.5, [-0.35, 0.6]],
  ],
  // blade pitch over time: pages turn on their radial line and lie back into
  // the wheel plane for the climax
  pitch: [[1.22, [-0.55]], [3.0, [-0.55]], [3.72, [-1.45]], [4.5, [-1.45]]],
  // overall wheel scale
  scale: [[1.22, [0.85]], [1.45, [0.92]], [1.72, [0.95]], [3.0, [1.02]], [3.72, [1.1]], [4.5, [1.1]]],
};

// ---------------------------------------------------------------- helpers
const clamp01 = (x) => Math.min(1, Math.max(0, x));

// Cubic Hermite through (time, value[]) knots; finite-difference tangents,
// zero slope at both ends (ease in/out at the track limits).
export function track(knots) {
  const n = knots.length;
  const m = knots.map((k, i) => {
    if (i === 0 || i === n - 1) return k[1].map(() => 0);
    const a = knots[i - 1];
    const b = knots[i + 1];
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

export function buildRig(rig = RIG) {
  const spread = track(rig.spread);
  const omega = track(rig.omega);
  const position = track(rig.position);
  const rotation = track(rig.rotation);
  const scale = track(rig.scale);
  const tip = rig.tip ? track(rig.tip) : null;
  const pitch = rig.pitch ? track(rig.pitch) : null;
  // integrate wheel angle once (table, 1/1200 s)
  const dt = 1 / 1200;
  const n = Math.ceil(DURATION / dt) + 2;
  const theta = new Float64Array(n);
  for (let i = 1; i < n; i++) {
    const tm = (i - 0.5) * dt;
    theta[i] = theta[i - 1] + (tm >= rig.appear ? omega(tm)[0] : 0) * dt;
  }
  const angle = (t) => {
    const x = clamp01(t / DURATION) * DURATION / dt;
    const i = Math.floor(x);
    return theta[i] + (theta[Math.min(i + 1, n - 1)] - theta[i]) * (x - i);
  };
  return { spread, omega, position, rotation, scale, angle, tip, pitch };
}

// ------------------------------------------------------------------ poses
const _m = new THREE.Matrix4();
const _x = new THREE.Vector3();
const _y = new THREE.Vector3(0, 0, 1); // wheel axis
const _z = new THREE.Vector3();

export function wheelMatrix(R, t, rig = RIG) {
  const p = R.position(t);
  const r = R.rotation(t);
  const s = R.scale(t)[0];
  const q = new THREE.Quaternion().setFromEuler(new THREE.Euler(r[0], r[1], r[2], "XYZ"));
  // r[3]: roll about the camera's view axis, applied last (turns the whole
  // pattern of faces/slivers around the screen)
  q.premultiply(new THREE.Quaternion().setFromAxisAngle(new THREE.Vector3(0, 0, 1), r[3] ?? 0));
  // tip: [angle about the screen's horizontal axis (negative = bottom of the
  // wheel swings toward the lens), final roll about the view axis]. Used for
  // the entrance (wheel opens from edge-on) and the climax (bottom rim dives
  // past the lens) so both moves rotate the wheel as one rigid object.
  const tp = R.tip ? R.tip(t) : [0, 0];
  q.premultiply(new THREE.Quaternion().setFromAxisAngle(new THREE.Vector3(1, 0, 0), tp[0]));
  q.premultiply(new THREE.Quaternion().setFromAxisAngle(new THREE.Vector3(0, 0, 1), tp[1]));
  return new THREE.Matrix4().compose(new THREE.Vector3(...p), q, new THREE.Vector3(s, s, s));
}

// Page k in wheel space: centre on the radius, plane = span(radial, axis).
export function pageLocal(R, k, t, rig = RIG) {
  const N = rig.cards;
  const spread = R.spread(t)[0];
  // fan anchored on the last page: the deck opens behind it
  const phi = rig.phase0 + R.angle(t) + (N - 1 - k) * spread * (2 * Math.PI / N);
  _x.set(Math.cos(phi), Math.sin(phi), 0); // radial
  // page basis: art "up" = radial (outward), art "right" = wheel axis
  _z.crossVectors(_y, _x);
  _m.makeBasis(_y, _x, _z);
  _m.multiply(new THREE.Matrix4().makeRotationY(R.pitch ? R.pitch(t)[0] : rig.bladePitch));
  _m.setPosition(_x.x * rig.radius, _x.y * rig.radius, 0);
  return _m.clone();
}

// ------------------------------------------------------------------ scene
function roundedAlpha() {
  const s = 256;
  const cv = document.createElement("canvas");
  cv.width = cv.height = s;
  const g = cv.getContext("2d");
  g.fillStyle = "#000";
  g.fillRect(0, 0, s, s);
  g.fillStyle = "#fff";
  g.beginPath();
  g.roundRect(2, 2, s - 4, s - 4, s * 0.05);
  g.fill();
  return new THREE.CanvasTexture(cv);
}

export function createWheel(canvas, rig = RIG) {
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true, preserveDrawingBuffer: true });
  renderer.setPixelRatio(1);
  renderer.setSize(WIDTH, HEIGHT, false);
  renderer.setClearColor(0x000000, 0); // transparent: page colour and type sit under the canvas
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(rig.fov, WIDTH / HEIGHT, 0.05, 80);
  camera.position.set(...rig.camera);
  camera.lookAt(0, 0, 0);
  const R = buildRig(rig);
  const alpha = roundedAlpha();
  const geo = new THREE.PlaneGeometry(rig.page, rig.page);
  const loader = new THREE.TextureLoader();
  const textures = {};
  const loads = COVERS.map((name) =>
    loader.loadAsync(`assets/covers/${name}`).then((tex) => {
      tex.colorSpace = THREE.SRGBColorSpace;
      tex.anisotropy = 8;
      const back = tex.clone();
      back.wrapS = THREE.RepeatWrapping;
      back.repeat.x = -1;
      back.offset.x = 1;
      back.needsUpdate = true;
      textures[name] = { front: tex, back };
    }),
  );
  const wheel = new THREE.Group();
  wheel.matrixAutoUpdate = false;
  scene.add(wheel);
  const pages = [];
  for (let k = 0; k < rig.cards; k++) {
    const cover = COVERS[k % COVERS.length];
    const front = new THREE.MeshBasicMaterial({ alphaMap: alpha, alphaTest: 0.5, side: THREE.FrontSide });
    const back = new THREE.MeshBasicMaterial({ alphaMap: alpha, alphaTest: 0.5, side: THREE.BackSide });
    const g = new THREE.Group();
    g.matrixAutoUpdate = false;
    g.add(new THREE.Mesh(geo, front), new THREE.Mesh(geo, back));
    wheel.add(g);
    pages.push({ k, cover, g, front, back });
  }

  function apply(t) {
    wheel.visible = t >= rig.appear && t < rig.leave;
    wheel.matrix.copy(wheelMatrix(R, t, rig));
    for (const p of pages) p.g.matrix.copy(pageLocal(R, p.k, t, rig));
    scene.updateMatrixWorld(true);
  }
  function render(t) {
    apply(Math.min(Math.max(t, 0), DURATION));
    renderer.render(scene, camera);
  }
  // exact geometry for QA
  const corners = [[-0.5, -0.5], [0.5, -0.5], [0.5, 0.5], [-0.5, 0.5]];
  function sample(t) {
    apply(t);
    const v = new THREE.Vector3();
    return {
      t,
      visible: wheel.visible,
      cards: pages.map((p) => {
        const mw = p.g.matrixWorld;
        const pts = corners.map(([x, y]) => {
          v.set(x * rig.page, y * rig.page, 0).applyMatrix4(mw);
          const d = v.distanceTo(camera.position);
          v.project(camera);
          return [v.x, v.y, v.z, d];
        });
        const c = new THREE.Vector3().setFromMatrixPosition(mw);
        const nrm = new THREE.Vector3(0, 0, 1).transformDirection(mw);
        return { id: `${p.k}:${p.cover}`, corners: pts, camDist: c.distanceTo(camera.position),
          facing: nrm.dot(camera.position.clone().sub(c).normalize()) };
      }),
    };
  }
  const ready = Promise.all(loads)
    .then(() => {
      for (const p of pages) {
        p.front.map = textures[p.cover].front;
        p.back.map = textures[p.cover].back;
        p.front.color.setScalar(1);
        p.back.color.setScalar(0.82);
        p.front.needsUpdate = p.back.needsUpdate = true;
      }
      return renderer.compileAsync(scene, camera);
    })
    .then(() => {
      render(0);
      const gl = renderer.getContext();
      gl.readPixels(0, 0, 1, 1, gl.RGBA, gl.UNSIGNED_BYTE, new Uint8Array(4));
    });
  return { render, sample, ready, rig };
}
