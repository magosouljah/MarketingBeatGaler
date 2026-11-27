/* ============ TIEMPOS (segundos de video) — comunes a las variantes; lo que cambia viene de js/variant.js (V.time, V.hook) ============
   Anclado a audio medido (align_words.py / find_hits.py).
   Beat viejo (bosque.flp, 130 BPM, compas 1.846 s): se usa desde OLD0 (inicio de compas); bateria en 11.346. El audio repite una
   vez los compases 11.346-15.04 y el video se frena desde TS para llegar al final cuando la ventana ya salio de cuadro.
   Beat nuevo (bosque pero jerk.flp, 143 BPM, compas 1.678 s): desde NEW0; bateria en 7.384. Suena SIN locucion hasta el CTA. */
const HOOK = { id: V.id, vo: V.hook.vo, dur: V.hook.dur };
const OLD0 = V.time.OLD0, NEW0 = V.time.NEW0;
const T = (function () {
  const OLD = V.time.OLD;
  const LOOP = OLD + (15.04 - OLD0);            // el audio vuelve a 11.346
  const D = LOOP + (16.73 - 11.346);            // se suelta el clip y arranca el beat nuevo
  const o = {
    BACK: V.time.BACK, GAL: V.time.GAL, RCLICK: V.time.RCLICK, OPEN: V.time.OPEN, SPLASH: V.time.SPLASH, NOTE1: V.time.NOTE1, NOTE2: V.time.NOTE2,
    OLD, VO_C1A: HOOK.dur + 0.05,               // la frase entra pegada al hook
    OLDDROP: OLD + (11.346 - OLD0),             // la bateria entra en "fire"
    LOOP, VO_C1B: D - 6.10, VO_C1C: D - 2.70,
    D, ARRIVE: D - 0.45,
    NEWDROP: D + (7.384 - NEW0),
    WH: D + (10.74 - NEW0),                     // compas del beat nuevo; la lider llega a la rueda
    WHEEL0: 1.22,
  };
  o.TS = o.VO_C1B; o.TE = o.VO_C1B + 3.45;      // video viejo frenado en ese tramo
  o.GRAB = o.VO_C1B + 1.70; o.LIFT = o.VO_C1B + 1.95;          // agarra en "pull one"
  o.OUT = o.WH - 1.25;
  o.VO_CTA = o.WH + 0.02;
  o.W = { COMMENT: o.VO_CTA, GALER: o.VO_CTA + 0.45, TO: o.VO_CTA + 1.21, ALL: o.VO_CTA + 1.65, BEAT: o.VO_CTA + 2.10, ONLINE: o.VO_CTA + 2.81 };
  o.END = o.WH + (4.30 - 1.22);
  o.DUR = D + (15.40 - NEW0);
  /* subtitulos mientras se ve FL: [inicio, texto, final] */
  const sub = (t0, end, arr) => arr.map(([a, s], i) => [t0 + a, s, t0 + (i + 1 < arr.length ? arr[i + 1][0] : end)]);
  o.SUBS = [
    ...sub(o.VO_C1A, 5.95, [[0, "YOUR MIXING"], [0.55, "MIGHT HAVE SUCKED"], [1.42, "YOUR DRUMS"], [2.10, "MIGHT HAVE BEEN"], [2.47, "TERRIBLE"], [3.21, "BUT SOME OF THOSE"], [3.87, "MELODIES"], [4.42, "WERE ACTUALLY"], [5.09, "FIRE"]]),
    ...sub(o.VO_C1B, 3.36, [[0, "NEXT TIME"], [0.46, "YOU'RE STUCK"], [0.87, "ON A MELODY"], [1.70, "PULL ONE"], [2.11, "FROM AN"], [2.36, "OLD PROJECT"]]),
    ...sub(o.VO_C1C, 2.70, [[0, "YOU MIGHT ALREADY"], [0.87, "HAVE THE"], [1.18, "INSPIRATION"], [1.73, "YOU'RE LOOKING FOR"]]),
  ];
  return o;
})();
window.T = T; window.HOOK = HOOK; window.OLD0 = OLD0; window.NEW0 = NEW0;
