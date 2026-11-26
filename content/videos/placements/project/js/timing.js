/* ============ TIEMPOS — todo anclado a audio medido ============
   Musica: inputs/beat.wav (150 BPM, negra = 0.4 s) entra en T=0 desde 6.0 s del archivo.
   808 medidos (T): .46 1.66 5.66 6.26 6.86 8.06 12.66 13.26 14.46 18.46 19.06 19.66(flojo, con caja) 20.86
   Cajas medidas (T): 9.25 10.85 14.05 15.65 17.25
   Palabras: alineacion forzada (shared/transcription/align_words.py).

   MODULARIDAD: el hook vive en HOOK. Para cambiar de hook se reemplazan HOOK y js/hook-*.js;
   el cuerpo usa tiempos relativos a B = HOOK.DUR y no se toca. */
const M=0.40; // el hook se alargo 0.4 s (un tiempo) para dar aire a los tres puntitos; la musica entra desde 6.0 s del archivo
const HOOK={ DUR:5.10, VO:0.85,
  TYPE0:0.40, TYPE1:0.95, SEND:1.05, MORPH:1.40, DOTS:1.22, MSG:2.20,
  ASAP:2.21, PULL:3.10, FIRST:3.65, TO:3.98, SENDW:4.05, YOURS:4.31, WHIP:4.80 };
const B=HOOK.DUR;
/* Voz del cuerpo: tres tramos del mismo archivo (cortes en silencios medidos).
   [inicio en archivo, fin en archivo, T de entrada] */
const VOB=[[0.00,5.98,B+0.00],[5.98,9.20,B+6.28],[9.20,11.69,B+12.02]];
const W={ // T de cada palabra clave
  HUNDREDS:B+1.77, FILES:B+2.39, ONE1:B+2.91, BY:B+3.25, ONE2:B+3.39,
  THATS:B+4.28, PACKS:B+5.08, READY1:B+5.52,
  ORGANIZE:B+7.02, GENRE:B+8.17, MOOD:B+8.90,
  WHEN:B+12.25, OPP:B+12.46, COMES:B+13.04, IM:B+13.71, READY2:B+13.94 };
const S={ // cuerpo
  FIN:B, TAKE:8.85+M, LAND:10.45+M, TAG1:12.86+M, TAG2:13.65+M,
  SEL0:14.06+M, SEL1:14.66+M, SEL2:15.05+M, SEL3:15.45+M, PACK:15.85+M, COPY:16.45+M, BACK:16.85+M,
  PASTE:17.22+M, SENDL:17.74+M, DOTS2:18.20+M, FIRE:19.26+M, ACC:20.46+M };
/* CTA: entra tras el acento final (808 de 20.86); FREE termina sobre la caja de 23.65 */
const C={ T:21.00, VO:21.15, COMMENT:21.15, GALER:21.61, TO:22.61, FOR:22.98, END:23.65 };
const DUR=24.10;
