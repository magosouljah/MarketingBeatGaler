# BeatGaler — Choreography Lab V2: rueda tipo rolodex (reconstrucción de Apple Music)

**Estado:** iteración 2 de la reconstrucción (`wheel-v3.mp4`) · **sin aprobación creativa** · no es el anuncio.

## Decisión del propietario (2026-11-05, en el chat)

Tras revisar el lab V1: «estamos intentando hacer lo más cercano a Apple», «en ningún momento se ponen todas las portadas en grid», «ninguna se parece realmente, tal vez A porque no están las portadas en posiciones aleatorias». Por eso V2:

- busca el **máximo parecido** con la referencia (esto sustituye, para este experimento, la regla 6 de `skillpack/README.md` sobre no copiar coreografías ajenas);
- **elimina la galería/grid**;
- parte de **A**: una sola estructura ordenada y rígida, sin posiciones aleatorias.

Se mantienen las portadas, el texto y la marca de BeatGaler; no se usa nada de Apple (ni logo, ni texto, ni arte).

Segunda revisión del propietario (2026-11-06): fondo **#0C0C0C**; texto «Free*» / «Unlimited» / «Cloud» y cierre con «for beats and projects»; letra pequeña permitida; corregir cómo aparecen las portadas, el ángulo y el centrado del círculo, y el barrido de ~3 s («en el de Apple gira hacia el lado contrario y se ve mega natural»).

## Qué es la estructura (inferida de la referencia, ver RESULTS.md)

Una **rueda de 28 portadas equiespaciadas**. Cada portada es una «página» radial: su plano contiene la dirección radial y el eje de la rueda (como un rolodex o una rueda de paletas), y está girada 35,5° sobre su propia línea radial (paso de pala). La rueda está inclinada ese mismo ángulo, de modo que a un lado las páginas se ven de canto (líneas) y al otro se abren en caras completas, como en Apple.

| Tiempo (s, reloj de Apple) | Qué pasa |
| --- | --- |
| 0–1,2 | Marca «BeatGaler» que se encoge (equivale al logo de Apple) |
| 1,22–1,72 | La rueda aparece **de canto** como una fila diagonal que sube a la derecha y se abre inclinándose hacia el lente |
| 1,6–3,0 | La rueda gira en sentido horario (≈ 2,6 rad/s) alrededor de «Free*» / «Unlimited» / «Cloud», con la pose ajustada a la silueta de Apple |
| 3,0–3,72 | **La misma rueda se inclina** (su borde inferior izquierdo viene hacia el lente), las páginas se tumban sobre su línea radial y la fila de abajo se desliza a la izquierda; el giro nunca cambia de sentido ni el eje se tuerce de lado |
| 3,72–4,3 | **Riffle**: las páginas pasan junto al lente, ≈ 1 página por fotograma (6–6,5 rad/s) |
| 4,3–4,5 | La rueda sale por arriba; el cuadro queda limpio |
| 4,37–6,0 | Cierre «BeatGaler / Free* Unlimited Cloud / for beats and projects» + letra pequeña (**provisional**: «*Terms and conditions apply.» hasta tener las condiciones reales) |

Todos los parámetros están en `RIG` (incluye `tip`: inclinación rígida de toda la rueda, y `pitch`: giro de cada página sobre su línea radial) dentro de [`hyperframes/src/wheel.js`](hyperframes/src/wheel.js): número de páginas, tamaño, radio, paso de pala, lente, abanico (`spread`), velocidad angular (`omega`), posición, rotación y escala de la rueda como pistas Hermite por tiempo. Todo depende solo de `t`.

## Ver, editar, renderizar

- Render actual: `evidence/renders/wheel-v3.mp4` (HyperFrames 0.9.17, 720×1280, 30 fps, 6 s). Anterior: `wheel-v2.mp4` (fondo claro, copy «Create ur Galer»).
- Comparativas con Apple **solo locales** (contienen fotogramas de Apple; no se versionan): `reference-runs/apple-music/ref-vs-wheel-v3-LOCAL-ONLY.mp4` y `ref-vs-wheel-v2-LOCAL-ONLY.mp4`.

```powershell
cd account-1/creative-assets/choreography-lab-v2/hyperframes
npx --yes hyperframes@0.9.17 preview
npx --yes hyperframes@0.9.17 render --quality draft -o ../evidence/renders/wheel-v2.mp4
# comparativa local fotograma a fotograma (necesita playwright + Chrome; no subir el resultado)
python ../tools/compare_frames.py ../../../../reference-runs/apple-music/instagram-original.mp4 compare.jpg --at 1.3,1.6,2.2,2.9,3.5,3.8,4.1
```

Three.js 0.184.0, GSAP 3.15.0 y Archivo Black (OFL, `assets/fonts/`) van incluidos: el render no usa red.
