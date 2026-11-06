# BeatGaler — Choreography Lab V2: rueda tipo rolodex (reconstrucción de Apple Music)

**Estado:** iteración 1 de la reconstrucción · **sin aprobación creativa** · no es el anuncio.

## Decisión del propietario (2026-11-05, en el chat)

Tras revisar el lab V1: «estamos intentando hacer lo más cercano a Apple», «en ningún momento se ponen todas las portadas en grid», «ninguna se parece realmente, tal vez A porque no están las portadas en posiciones aleatorias». Por eso V2:

- busca el **máximo parecido** con la referencia (esto sustituye, para este experimento, la regla 6 de `skillpack/README.md` sobre no copiar coreografías ajenas);
- **elimina la galería/grid**;
- parte de **A**: una sola estructura ordenada y rígida, sin posiciones aleatorias.

Se mantienen las portadas, el texto y la marca de BeatGaler; no se usa nada de Apple (ni logo, ni texto, ni arte).

## Qué es la estructura (inferida de la referencia, ver RESULTS.md)

Una **rueda de 28 portadas equiespaciadas**. Cada portada es una «página» radial: su plano contiene la dirección radial y el eje de la rueda (como un rolodex o una rueda de paletas), y está girada 35,5° sobre su propia línea radial (paso de pala). La rueda está inclinada ese mismo ángulo, de modo que a un lado las páginas se ven de canto (líneas) y al otro se abren en caras completas, como en Apple.

| Tiempo (s, reloj de Apple) | Qué pasa |
| --- | --- |
| 0–1,2 | Marca «BeatGaler» que se encoge (equivale al logo de Apple) |
| 1,22–1,75 | Las páginas aparecen juntas como un mazo y se abren en abanico hasta formar la rueda |
| 1,6–3,0 | La rueda gira en sentido horario (≈ 2,6 rad/s) alrededor de «Create» / «ur» / «Galer» |
| 3,0–3,68 | La rueda crece y gira su eje hacia un lado |
| 3,68–4,3 | **Riffle**: las páginas pasan junto al lente en pila diagonal, ≈ 1 página por fotograma (6–6,5 rad/s) |
| 4,3–4,5 | La rueda sale por arriba; el cuadro queda limpio |
| 4,37–6,0 | Cierre «BeatGaler / Create ur Galer» |

Todos los parámetros están en `RIG` dentro de [`hyperframes/src/wheel.js`](hyperframes/src/wheel.js): número de páginas, tamaño, radio, paso de pala, lente, abanico (`spread`), velocidad angular (`omega`), posición, rotación y escala de la rueda como pistas Hermite por tiempo. Todo depende solo de `t`.

## Ver, editar, renderizar

- Render: `evidence/renders/wheel-v2.mp4` (HyperFrames 0.9.17, 720×1280, 30 fps, 6 s).
- Comparativa con Apple **solo local** (contiene fotogramas de Apple; no se versiona): `reference-runs/apple-music/ref-vs-wheel-v2-LOCAL-ONLY.mp4`.

```powershell
cd account-1/creative-assets/choreography-lab-v2/hyperframes
npx --yes hyperframes@0.9.17 preview
npx --yes hyperframes@0.9.17 render --quality draft -o ../evidence/renders/wheel-v2.mp4
# comparativa local fotograma a fotograma (necesita playwright + Chrome; no subir el resultado)
python ../tools/compare_frames.py ../../../../reference-runs/apple-music/instagram-original.mp4 compare.jpg --at 1.3,1.6,2.2,2.9,3.5,3.8,4.1
```

Three.js 0.184.0, GSAP 3.15.0 y Archivo Black (OFL, `assets/fonts/`) van incluidos: el render no usa red.
