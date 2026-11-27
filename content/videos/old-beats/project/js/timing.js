/* ============ TIEMPOS v3 (segundos de video) ============
   Anclado a audio medido (align_words.py / find_hits.py).
   Beat viejo (bosque.flp, 130 BPM, compas 1.846 s): desde 9.50 s del archivo (inicio de compas); bateria en 11.346. El audio repite
   una vez los compases 11.346-15.04 y el video se frena desde TS para llegar al final cuando la ventana ya salio de cuadro.
   Beat nuevo (bosque pero jerk.flp, 143 BPM, compas 1.678 s): desde 4.02 s; bateria en 7.384. Suena SIN locucion hasta el CTA.
   El hook es el modulo intercambiable (HOOK.*). */
const HOOK = { id: "H1", vo: "C-H1.wav", dur: 2.80, THREE: 1.23, YEARS: 1.47, AGO: 1.84 };
const OLD0 = 9.50, NEW0 = 4.02;
const T = (function () {
  const OLD = 6.45;
  const LOOP = OLD + (15.04 - OLD0);            // 11.99: el audio vuelve a 11.346
  const D = LOOP + (16.73 - 11.346);            // 17.37: se suelta el clip y arranca el beat nuevo
  const o = {
    PASS0: 1.2, PASS1: 1.95, FIRST0: 2.8, FIRST1: 3.7, TURN: 3.9, BACK: 4.6,     // viaje: pasa por 2023, llega al primer beat, vuelve
    GAL: 5.05, RCLICK: 5.38, OPEN: 5.78, SPLASH: 5.86, NOTE1: 5.92, NOTE2: 6.12,
    OLD, VO_C1A: HOOK.dur + 0.05,               // 2.85 -> 8.71
    OLDDROP: OLD + (11.346 - OLD0),             // 8.30: la bateria entra en "fire"
    LOOP, VO_C1B: D - 6.10,                     // 11.27 -> 14.55
    VO_C1C: D - 2.70,                           // 14.67 -> 17.27
    D, ARRIVE: D - 0.45,
    NEWDROP: D + (7.384 - NEW0),                // 20.73
    WH: D + (10.74 - NEW0),                     // 24.09: compas del beat nuevo; las portadas empiezan a llegar a la rueda
    WHEEL0: 1.22,
  };
  o.TS = o.VO_C1B; o.TE = o.VO_C1B + 3.45;      // video viejo frenado en ese tramo
  o.GRAB = o.VO_C1B + 1.70; o.LIFT = o.VO_C1B + 1.95;          // agarra en "pull one"
  o.OUT = o.WH - 1.25;                          // 22.84: la camara sale de FL
  o.VO_CTA = o.WH + 0.02;                       // 24.11 -> 27.56
  o.W = { COMMENT: o.VO_CTA, GALER: o.VO_CTA + 0.45, TO: o.VO_CTA + 1.21, ALL: o.VO_CTA + 1.65, BEAT: o.VO_CTA + 2.10, ONLINE: o.VO_CTA + 2.81 };
  o.END = o.WH + (4.30 - 1.22);                 // 27.17
  o.DUR = D + (15.40 - NEW0);                   // 28.75
  /* subtitulos mientras se ve FL: [inicio, texto] por frase, con su final */
  const sub = (t0, end, arr) => arr.map(([a, s], i) => [t0 + a, s, t0 + (i + 1 < arr.length ? arr[i + 1][0] : end)]);
  o.SUBS = [
    ...sub(o.VO_C1A, 5.95, [[3.21, "BUT SOME OF THOSE"], [3.87, "MELODIES"], [4.42, "WERE ACTUALLY"], [5.09, "FIRE"]]),
    ...sub(o.VO_C1B, 3.36, [[0, "NEXT TIME"], [0.46, "YOU'RE STUCK"], [0.87, "ON A MELODY"], [1.70, "PULL ONE"], [2.11, "FROM AN"], [2.36, "OLD PROJECT"]]),
    ...sub(o.VO_C1C, 2.70, [[0, "YOU MIGHT ALREADY"], [0.87, "HAVE THE"], [1.18, "INSPIRATION"], [1.73, "YOU'RE LOOKING FOR"]]),
  ];
  return o;
})();
window.T = T; window.HOOK = HOOK; window.OLD0 = OLD0; window.NEW0 = NEW0;
