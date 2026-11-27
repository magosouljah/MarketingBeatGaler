/* ============ VARIANTE C-C1-H2 — «Before buying another melody pack, listen to some of your old beats.» ============
   Todo lo que distingue a esta version vive aqui; el resto de modulos es comun a las variantes.
   Intro: la ficha de un melody pack a punto de comprarse, en el "ahora" de la linea del tiempo. El cursor llega al boton y no
   compra: la camara lo deja atras y viaja al pasado, pasa despacio por YOUR OLD BEATS y se detiene en bosque (2023).
   Fondo negro, Gallery con bosque en la columna izquierda, clip que cae pesado por debajo, subtitulos amarillos, cierre a la izquierda. */
const V = {
  id: "H2", hook: { vo: "C-H2.wav", dur: 3.64 },
  theme: { ground: "#0A0A0B", ink: "#F3F1EC", note: "#FF453A", label: "#b4b4b4", stem: "rgba(243,241,236,.24)" },
  YS: 3000, seed: 9021, target: { year: 2023, off: .5, cover: "041" },
  time: { OLD: 6.93, OLD0: 9.50, NEW0: 4.02, LANEX: 742, BACK: 4.9, GAL: 5.35, RCLICK: 5.75, OPEN: 6.15, SPLASH: 6.23, NOTE1: 6.30, NOTE2: 6.50 },
  gallery: { col: 0, row: 1, menuDx: 58,
    covers: ["035", "011", "053", "041", "027", "006", "029", "034", "045", "017", "059", "026"],
    names: ["Halo", "Tape 04", "Velvet", "bosque", "Sunday", "Rust", "Opal", "Motel", "Kites", "Third Floor", "Lagoon", "Smoke"] },
  // portadas de la biblioteca sin personajes, marcas ni personas reconocibles
  pool: ["006", "011", "017", "022", "023", "026", "027", "029", "031", "034", "035", "039", "041", "045", "053", "055", "059", "002", "010", "033", "042", "057"],
  drag: { arc: 170, wob: 34, K: 58, C: 7.5, dip: .85, tilt: .013 },      // cae por debajo, con mas peso y mas retraso
  sub: "accent", end: "left",
  CX: 0, WX: 0,
  notes(h) { return [["First beat", h.XF + 500, -1, -5, h.XF + 900], ["FL trial", h.X(2022) + 1700, 1, 4, h.X(2022) + 1000], ["Forgot this one", h.TX - 60, 1, 4, h.TX + 560],
    ["Made 200 beats", h.X(2024) + 600, 1, -3, h.X(2024) - 150], ["First sale", h.X(2025) - 1200, -1, -4, h.X(2025) - 500], ["Pack #9", h.X(2025) + 1500, 1, 4, h.X(2025) + 900], ["Stuck again", h.X(2026) + 900, 1, -3, h.X(2026) + 350]]; },
  zones(h) { const cx = h.NOWX - 360, wx = h.X(2025) + 1500; return [[cx - 520, h.XR, -1], [wx - 620, wx + 420, -1]]; },
  words(h) { const cx = h.NOWX - 360, wx = h.X(2025) + 1500, L = cx - 360, o = 2.05;
    return [{ s: "BEFORE", t: 0.02, x: L, y: -1570, fs: 168, out: o }, { s: "BUYING", t: 0.39, x: L, y: -1425, fs: 168, out: o }, { s: "ANOTHER", t: 0.71, x: L, y: -1280, fs: 168, out: o },
      { s: "YOUR", t: 2.69, x: wx - 420, y: -900 }, { s: "OLD", t: 2.84, x: wx - 420, y: -697 }, { s: "BEATS", t: 3.13, x: wx - 420, y: -494 }].map(w => (w.out === undefined ? { ...w, out: 4.3 } : w)); },
  cam(h) { const cx = h.NOWX - 360, wx = h.X(2025) + 1500, B = this.time.BACK;
    return { cx: h.herm([[0, cx, -20], [1.8, cx - 90, -120], [2.55, wx + 900, -2400], [3.65, wx - 500, -700], [B, h.TX, 0]]),
      cy: t => kf(t, [[0, -700], [1.8, -700], [2.6, 40, E.ioC], [4.1, 40], [B, h.TY, E.ioC]]),
      z: t => kf(t, [[0, .8], [1.8, .8], [2.6, .56, E.ioC], [3.65, .6, E.ioS], [B, .64, E.ioS]]) }; },
  /* ficha del melody pack (tienda ficticia) */
  extra: {
    init(h) { const cx = h.NOWX - 360; V.CX = cx; const el = document.createElement("div"); el.id = "store"; el.style.cssText = `position:absolute;left:${cx - 360}px;top:-1080px;width:720px;height:880px;border-radius:44px;background:#19191b;box-shadow:0 0 0 2px rgba(255,255,255,.1),0 50px 120px rgba(0,0,0,.6);overflow:hidden;font-family:var(--font);color:#f2f2f2`;
      el.innerHTML = `<div id="sart" style="position:absolute;left:30px;top:30px;width:660px;height:470px;border-radius:28px;background:linear-gradient(140deg,#7b2ff7 0%,#f107a3 55%,#ff9a3c 100%);overflow:hidden"><div style="position:absolute;left:40px;top:150px;font:900 104px/.9 var(--disp);letter-spacing:-.04em">MELODY<br>PACK</div><div style="position:absolute;left:44px;top:380px;font:700 40px/1 var(--font);letter-spacing:.14em">VOL. 12</div></div>
        <div style="position:absolute;left:40px;top:540px;font:700 50px/1 var(--font);letter-spacing:-.02em">Melody Pack Vol. 12</div><div style="position:absolute;left:40px;top:608px;font:400 32px/1 var(--font);color:#9a9a9a">120 loops · WAV + MIDI</div>
        <div style="position:absolute;left:40px;top:738px;font:700 76px/1 var(--font);letter-spacing:-.03em">$29.99</div><div id="sbuy" style="position:absolute;left:380px;top:724px;width:300px;height:104px;border-radius:52px;background:#f2f2f2;color:#0c0c0c;font:700 40px/104px var(--font);text-align:center">Buy now</div>`;
      $("vx").appendChild(el); V._store = el; V._art = el.querySelector("#sart"); V._buy = el.querySelector("#sbuy"); },
    frame(t, h, st) { V._store.style.visibility = st.s1 ? "visible" : "hidden"; if (!st.s1) return;
      V._art.style.transform = `scale(${(1 + pulse(t, 1.03, .035, 12, 26) + pulse(t, 1.40, .03, 12, 26)).toFixed(4)})`;
      V._buy.style.transform = `scale(${(1 + .06 * E.ioS(seg(t, 1.2, 1.5)) - .06 * E.ioS(seg(t, 1.7, 2.0))).toFixed(4)})`; },
  },
  /* el cursor llega al boton, duda y se queda atras con la ficha cuando la camara se va */
  introCursor(h) { const bx = h.NOWX - 360 + 170, by = -1080 + 776; return { a: 0.3, b: 2.4, pos(t, toScreen) { const p = toScreen(bx, by, t), u = E.ioS(seg(t, .3, 1.45)); return { x: lerp(1010, p.x, u) + 5 * Math.sin(t * 9) * u, y: lerp(1780, p.y, u) }; } }; },
};
(function () { const r = document.documentElement.style, th = V.theme; r.setProperty("--ground", th.ground); r.setProperty("--ink", th.ink); r.setProperty("--note", th.note); r.setProperty("--label", th.label); r.setProperty("--stem", th.stem); })();
