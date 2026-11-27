/* ============ VARIANTE C-C1-H3 — «Go listen to the beats you were making two years ago.» ============
   Todo lo que distingue a esta version vive aqui; el resto de modulos es comun a las variantes.
   Intro: plano abierto de la linea del tiempo; una flecha manuscrita salta dos anos hacia atras desde hoy y la camara se lanza
   en picado hasta el beat de 2024 (dos anos, no tres), que queda junto a la marca de 2024. Escala de la regla mas corta para que los dos anos quepan en cuadro.
   Fondo blanco (el del original), Gallery con bosque en la columna derecha (menu hacia la izquierda), clip rapido y seco, subtitulos en caja, cierre grande. */
const V = {
  id: "H3", hook: { vo: "C-H3.wav", dur: 2.38 },
  theme: { ground: "#F3F1EC", ink: "#0C0C0C", note: "#E3261B", label: "#3a3a3a", stem: "rgba(12,12,12,.2)" },
  YS: 1700, seed: 5150, target: { year: 2024, off: .3, cover: "034" },
  time: { OLD: 4.10, OLD0: 7.65, NEW0: 5.70, LANEX: 712, BACK: 2.35, GAL: 2.80, RCLICK: 3.10, OPEN: 3.45, SPLASH: 3.52, NOTE1: 3.57, NOTE2: 3.77 },
  gallery: { col: 2, row: 1, menuDx: -378,
    covers: ["022", "055", "002", "039", "031", "034", "010", "057", "042", "033", "006", "045"],
    names: ["Plaid", "Fawn", "Graveyard", "Blur", "No Hands", "bosque", "Toad", "Laundry", "Teeth", "Yolk", "Fiesta", "Spiral"] },
  pool: ["006", "011", "017", "022", "023", "026", "027", "029", "031", "034", "035", "039", "041", "045", "053", "055", "059", "002", "010", "033", "042", "057"],
  drag: { arc: -60, wob: 10, K: 150, C: 15, dip: 1.2, tilt: .008 },       // viaje tenso y casi recto, plano mas abierto
  sub: "box", end: "big",
  notes(h) { return [["First beat", h.XF + 500, -1, -5, h.XF + 900], ["Rage era", h.X(2023) - 300, 1, 5, h.X(2023) + 250], ["Favorite beat", h.TX - 60, 1, 4, h.TX + 560], ["First placement", h.X(2025) + 1150, -1, -4, h.X(2025) + 420]]; },
  zones(h) { return []; }, coverP: .86,                                   // GO LISTEN va por debajo de los carriles: no quita sitio a las portadas
  words(h) { const L = h.TX - 390, top = h.TY - h.CSZ / 2 - 70 - 3 * 203, mid = (h.TX + h.NOWX) / 2;
    return [{ s: "GO", t: 0.0, x: mid - 1560, y: 1290, fs: 600, out: 1.2 }, { s: "LISTEN", t: 0.16, x: mid - 560, y: 1290, fs: 600, out: 1.2 },
      { s: "TWO", t: 1.44, x: L, y: top }, { s: "YEARS", t: 1.75, x: L, y: top + 203 }, { s: "AGO", t: 2.02, x: L, y: top + 406 }]; },
  cam(h) { const B = this.time.BACK, mid = (h.TX + h.NOWX) / 2 - 80;
    return { cx: t => kf(t, [[0, mid + 60], [.9, mid, E.ioS], [B, h.TX, E.ioC]]), cy: t => kf(t, [[0, -330], [.9, -350, E.ioS], [B, h.TY, E.ioC]]), z: t => kf(t, [[0, .186], [.9, .2, E.lin], [B, .64, E.ioC]]) }; },
  /* flecha manuscrita: dos anos hacia atras, de hoy a bosque */
  extra: {
    init(h) { const x0 = h.NOWX - 40, x1 = h.TX + 30, y = h.TY - h.CSZ / 2 - 70 - 3 * 203 - 90, pk = y - 1050, mx = (x0 + x1) / 2, c = V.theme.note;
      const el = document.createElementNS("http://www.w3.org/2000/svg", "svg"); el.setAttribute("width", 10); el.setAttribute("height", 10); el.style.cssText = "position:absolute;left:0;top:0;overflow:visible";
      el.innerHTML = `<path id="arcp" pathLength="1" d="M${x0} ${y} C${x0 - 500} ${pk} ${x1 + 700} ${pk - 80} ${x1} ${y}" fill="none" stroke="${c}" stroke-width="34" stroke-linecap="round" stroke-dasharray="1" stroke-dashoffset="1"/><path id="arch" d="M${x1 + 250} ${y - 170} L${x1} ${y} L${x1 - 40} ${y - 300}" fill="none" stroke="${c}" stroke-width="34" stroke-linecap="round" stroke-linejoin="round"/>`;
      const lb = document.createElement("div"); lb.className = "note"; lb.textContent = "2 years back"; lb.style.cssText = `left:${mx}px;top:${pk + 120}px;font-size:420px;transform:translate(-50%,-50%) rotate(-3deg)`;
      $("vx").appendChild(el); $("vx").appendChild(lb); V._arc = el.querySelector("#arcp"); V._head = el.querySelector("#arch"); V._lb = lb; V._g = el; },
    frame(t, h, st) { const on = st.s1 && t < V.time.BACK + .4; V._g.style.visibility = V._lb.style.visibility = on ? "visible" : "hidden"; if (!on) return;
      const o = 1 - seg(t, V.time.BACK + .1, V.time.BACK + .3); V._arc.style.strokeDashoffset = (1 - E.ioS(seg(t, .12, 1.3))).toFixed(4); V._arc.style.opacity = o; V._head.style.opacity = (seg(t, 1.24, 1.34) * o).toFixed(3);
      V._lb.style.opacity = (seg(t, .5, .68) * (1 - seg(t, 1.9, 2.2))).toFixed(3); },
  },
};
(function () { const r = document.documentElement.style, th = V.theme; r.setProperty("--ground", th.ground); r.setProperty("--ink", th.ink); r.setProperty("--note", th.note); r.setProperty("--label", th.label); r.setProperty("--stem", th.stem); })();
