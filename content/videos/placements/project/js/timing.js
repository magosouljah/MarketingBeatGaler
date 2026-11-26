/* ============ TIEMPOS ============
   Todo sale de js/variant.js (window.V), que escribe tools/sync.py a partir de audio medido:
   golpes del beat (find_hits) y palabras alineadas (align_words). No editar numeros a mano sin volver a medir.
   El hook es el modulo intercambiable (V.HOOK); el cuerpo cuelga de B = HOOK.DUR y de V.S. */
const V=window.V, HOOK=V.HOOK, B=HOOK.DUR;
/* Voz del cuerpo: tres tramos del mismo archivo (cortes en silencios medidos). [inicio, fin, T de entrada] */
const VOB=[[0.00,5.98,B],[5.98,9.20,B+6.28],[9.20,11.69,V.SEG3]];
const W={ HUNDREDS:B+1.77, FILES:B+2.39, ONE1:B+2.91, BY:B+3.25, ONE2:B+3.39,
  THATS:B+4.28, PACKS:B+5.08, READY1:B+5.52, ORGANIZE:B+7.02, GENRE:B+8.17, MOOD:B+8.90,
  WHEN:V.SEG3+.23, OPP:V.SEG3+.44, COMES:V.SEG3+1.02, IM:V.SEG3+1.69, READY2:V.SEG3+1.92 };
const S=V.S; S.FIN=B;
const C=V.C, DUR=V.DUR;
