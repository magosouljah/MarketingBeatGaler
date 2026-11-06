# BeatGaler — Choreography Lab V2: rueda tipo rolodex (reconstrucción de Apple Music)

**Estado:** iteración 6 de la reconstrucción (`wheel-v7.mp4`) · **sin aprobación creativa** · no es el anuncio.

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
| 1,22–1,72 | Las páginas aparecen **una tras otra** a lo largo de la rueda (conteo medido en Apple); la rueda empieza casi de canto y se abre inclinándose hacia el lente |
| 1,53–3,65 | La rueda gira en sentido horario alrededor de «Unlimited» / «Free*» / «Storage» (rápido–lento–rápido, como Apple); cada palabra entra con la animación medida en Apple y nunca se queda quieta |
| 3,0–3,75 | El círculo gira sobre el eje de la vista hasta el ángulo de Apple (−54° en el fotograma 99) y se acerca; las páginas muestran siempre su frente |
| 3,75–4,5 | **Riffle**: la rueda **no se mueve**; el giro (6–6,5 rad/s) apila las páginas y las saca por arriba. Cada página que sale del cuadro se retira y no vuelve a entrar |
| 4,3–6,0 | Cierre «BeatGaler / 1 month of (regular) / Unlimited Free* Storage / for your beats and projects», pill «CODE: FREEGALER» y letra pequeña con la oferta (1 mes gratis con código, luego $11/mes USD, renovación automática). **FREEGALER es un código inventado: darlo de alta antes de publicar** |

Todos los parámetros están en `RIG` (incluye `retireFrom`: desde cuándo se retiran las páginas que salen del cuadro; `showBacks`: páginas de una sola cara; `tip`: inclinación rígida de toda la rueda, y `pitch`: giro de cada página sobre su línea radial) dentro de [`hyperframes/src/wheel.js`](hyperframes/src/wheel.js): número de páginas, tamaño, radio, paso de pala, lente, abanico (`spread`), velocidad angular (`omega`), posición, rotación y escala de la rueda como pistas Hermite por tiempo. Todo depende solo de `t`.

## Ver, editar, renderizar

- Render actual: `evidence/renders/wheel-v7.mp4`. Anteriores: `wheel-v6.mp4`, `wheel-v5.mp4`, `wheel-v4.mp4` (aparición escalonada, portadas giradas 180°), `wheel-v3.mp4` (fondo #0C0C0C) y (HyperFrames 0.9.17, 720×1280, 30 fps, 6 s). `wheel-v2.mp4` (fondo claro, copy «Create ur Galer»).
- Comparativas con Apple **solo locales** (contienen fotogramas de Apple; no se versionan): `reference-runs/apple-music/ref-vs-wheel-v7-LOCAL-ONLY.mp4` (Apple | v7 | v6, con número de fotograma), `ref-vs-wheel-v7-LOCAL-ONLY-slow4x.mp4` (a 1/4 de velocidad) y las de v3 y v2.

```powershell
cd account-1/creative-assets/choreography-lab-v2/hyperframes
npx --yes hyperframes@0.9.17 preview
npx --yes hyperframes@0.9.17 render --quality draft -o ../evidence/renders/wheel-v2.mp4
# comparativa local fotograma a fotograma (necesita playwright + Chrome; no subir el resultado)
python ../tools/compare_frames.py ../../../../reference-runs/apple-music/instagram-original.mp4 compare.jpg --at 1.3,1.6,2.2,2.9,3.5,3.8,4.1
```

Three.js 0.184.0, GSAP 3.15.0 y Archivo Black (OFL, `assets/fonts/`) van incluidos: el render no usa red.
