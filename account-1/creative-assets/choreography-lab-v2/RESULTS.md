# Lab V2 — resultados

**No es aprobación creativa.** Medición técnica y autoevaluación del agente. Casos: `choreography-lab-v2-wheel` (iteración 1), `choreography-lab-v3-wheel` (iteración 2) y `choreography-lab-v4-wheel` (iteración 3).

## Iteración 3 (`wheel-v4.mp4`, 2026-11-06)

Observaciones del propietario sobre v3: (1) las portadas salían todas a la vez desde un centro y se iban separando, mientras que en Apple van saliendo una tras otra; (2) en Apple el texto está cargado a la derecha dentro del círculo para que *se sienta* centrado; (3) en el barrido las portadas se aplanan; (4) girar todas las portadas 180° para que su parte de arriba apunte al centro.

Cambios:
1. **Aparición página a página.** Conté en la referencia cuántas páginas hay visibles en cada fotograma (1,233 s: 1; 1,267: 3; 1,300: 12; 1,333: 16; 1,400: 20; 1,500: 26; 1,567: todas) y cada página aparece en ese orden a lo largo de la rueda (`reveal`), creciendo en 0,05 s. Las páginas ya no se separan: ocupan su lugar definitivo desde el primer fotograma. La página inicial y la posición se ajustaron por IoU de silueta en 1,27–1,53 s.
2. **Texto:** centrado en el punto medido de Apple (0,52 W; 0,41 H), es decir, desplazado a la derecha dentro del círculo.
3. **Barrido sin aplanar:** el giro de cada página sobre su línea radial pasa de −0,55 a −0,8 (antes llegaba a −1,45 y quedaban planas). La cámara termina junto al borde izquierdo de la rueda, mirando a lo largo de él: las páginas se apilan de frente y el giro horario las sube y aleja.
4. **Portadas giradas 180°** (`coverFlip`): la parte de arriba de cada portada apunta al centro de la rueda.

Comparación fotograma a fotograma (`tools/frame_iou.py`: IoU de silueta en cada fotograma de 1,23 a 4,4 s; `evidence/frame-iou-v4.json` y `frame-iou-v3.json`):

| Fase | v3 | v4 |
| --- | ---: | ---: |
| Aparición 1,2–1,6 | 0,29 | **0,36** |
| Rueda 1,6–3,0 | 0,50 | 0,49 |
| Acercamiento 3,0–3,65 | 0,31 | **0,34** |
| Riffle 3,65–4,35 | 0,18 | **0,25** |
| Media | 0,36 | **0,38** |

Mismo reloj, medición de movimiento (`evidence/reference-comparison-v4.json`): la oclusión del riffle iguala la de Apple (0,78 contra 0,78) y la del acercamiento sube de 0,17 a 0,30 (Apple 0,58). **Hay dos retrocesos:**
- **Arco de energía:** el pico pasa al acercamiento (1,00) y el riffle queda en 0,83, porque nuestra pila cubre la mitad que la de Apple (cobertura 0,16 contra 0,32).
- **Giro durante la aparición:** curl 3,7 contra 0,56 de Apple (v3: 1,36). Como las páginas ya están en su sitio definitivo, el giro de la rueda se ve mientras van apareciendo.

## Iteración 2 (`wheel-v3.mp4`, 2026-11-06)

Lo que cambió, a partir de las observaciones del propietario y del análisis fotograma a fotograma:

- **Aparición:** en Apple, la rueda aparece de canto (fila diagonal que sube a la derecha, 1,27–1,33 s) y se abre inclinándose hacia el lente. Antes nuestro mazo se abría girando. Ahora la rueda abre con una inclinación rígida (`tip`), sin giro de pantalla añadido.
- **Ángulo y centrado del círculo:** la pose de la rueda se ajustó buscando la silueta de Apple a 1,9 / 2,2 / 2,6 s (coincidencia de máscaras, IoU, sin la caja del texto). **IoU 0,485, contra 0,338 de la iteración 1.**
- **Barrido de ~3 s:** en Apple, la fila de abajo se desliza a la izquierda mientras las páginas se tumban (3,33–3,73 s), siguiendo el mismo giro horario. Antes torcíamos el eje de la rueda hacia un lado, con un giro de pantalla de +1,5 rad en sentido contrario al giro de las portadas; por eso se veía antinatural. Ahora la misma rueda solo se inclina (su borde inferior izquierdo viene hacia el lente) y cada página gira sobre su línea radial (`pitch` de −0,55 a −1,45). El sentido del giro no cambia.
- Fondo #0C0C0C, «Free*» / «Unlimited» / «Cloud», cierre con «for beats and projects» y letra pequeña **provisional**.

Mismo reloj que Apple (`evidence/reference-comparison-v3.json`; iteración 1: `evidence/reference-comparison.json`):

| Fase | Métrica | Apple | v3 | v2 |
| --- | --- | ---: | ---: | ---: |
| Aparición 1,2–1,6 | Curl (giro en pantalla) | +0,56 | **+1,36** | −4,81 |
| Aparición | Energía relativa | 0,24 | **0,23** | 0,18 |
| Rueda 1,6–3,0 | Velocidad / curl | 0,62 / 5,75 | 0,61 / 5,46 | 0,63 / 5,36 |
| Rueda | Cobertura / oclusión | 0,17 / 0,13 | **0,19 / 0,14** | 0,14 / 0,09 |
| Acercamiento 3,0–3,65 | Energía relativa | 0,65 | **0,70** | 0,42 |
| Acercamiento | Proxy de oclusión | 0,58 | 0,17 | 0,15 |
| Riffle 3,65–4,35 | Cobertura / oclusión | 0,32 / 0,78 | 0,37 / 0,63 | 0,35 / 0,78 |

Sigue abierto: en el riffle (3,6–4,05 s) nuestras páginas forman una banda curva en la mitad inferior; en Apple, una pila de 3–4 páginas grandes centrada. La oclusión del acercamiento sigue baja (0,17 contra 0,58).

## Iteración 1 (`wheel-v2.mp4`)

## Hallazgo de estructura

Viendo los fotogramas a resolución completa del archivo de Instagram (§ «Fuente» abajo) se ve que las portadas son **páginas radiales de una rueda**: a la izquierda e izquierda-abajo son líneas que apuntan al centro; a la derecha muestran la cara; y en 3,7–4,3 s la «pila» que sube es **la misma rueda vista desde su borde**, con las páginas pasando como un rolodex. Esto unifica las dos hipótesis del riffle (`PHASE2-RERUN.md`): es una cinta continua (H1), la rueda girando ≈ 1 página por fotograma junto al lente. También explica por qué A (estructura rígida y ordenada) era la variante más parecida, tal como dijo el propietario.

## Misma medición, mismo reloj (`evidence/reference-comparison.json`)

| Fase (s de Apple) | Métrica | Apple | V2 | V1-B (antes) |
| --- | --- | ---: | ---: | ---: |
| todas | Arco de energía (abanico / rueda / acercamiento / riffle / final) | 0,24 / 0,45 / 0,65 / **1,00** / 0,06 | 0,18 / 0,30 / 0,42 / **1,00** / 0,00 | invertido (pico en la entrada) |
| Rueda 1,6–3,0 | Velocidad (alturas/s) | 0,62 | **0,63** | 0,23 |
| Rueda | Curl (giro en pantalla, 1/s) | 5,75 | **5,36** | −0,14 |
| Rueda | Cobertura | 0,17 | 0,14 | 0,30 |
| Riffle 3,65–4,35 | Cobertura | 0,32 | 0,35 | — |
| Riffle | Proxy de oclusión | 0,78 | **0,78** | 0,19 (clímax) |
| Riffle | Velocidad | 0,82* | 0,94 | — |
| Acercamiento 3,0–3,65 | Proxy de oclusión | 0,58 | **0,15** | — |
| Abanico 1,2–1,6 | Curl | +0,56 | **−4,81** | — |

\* subestimada en la referencia (desplazamientos demasiado grandes para el flujo óptico).

## Qué ya se parece

1. El arco de energía tiene la forma de Apple: el pico es el riffle y el final queda limpio.
2. La rueda gira en el mismo sentido y casi a la misma velocidad (curl 5,4 contra 5,8; velocidad 0,63 contra 0,62).
3. Caras a la derecha y líneas a la izquierda, con el texto en el hueco central.
4. El riffle tiene la misma cobertura y la misma oclusión que Apple, y la rueda sale por arriba hacia 4,4 s.
5. No hay grid ni posiciones aleatorias.

## Qué todavía no se parece (próxima iteración)

1. **Abanico (1,22–1,6 s):** el nuestro gira en sentido contrario y demasiado (curl −4,8 contra +0,6). En Apple es una fila diagonal que se abre casi sin girar, ligeramente arriba del centro.
2. **Acercamiento (3,0–3,65 s):** en Apple las páginas grandes de abajo a la derecha se van superponiendo (oclusión 0,58); en la nuestra la rueda gira el eje y por un instante casi no hay caras (0,15). Se nota como un salto alrededor de 3,5 s.
3. **Pose del riffle:** nuestras páginas quedan más verticales; las de Apple están más tumbadas hacia atrás (vistas desde arriba) y centradas.
4. **Rueda:** la nuestra cubre un poco menos (0,14 contra 0,17), con páginas algo más pequeñas.
5. Fondo y tipografía: aproximados (Archivo Black, fondo #f3f3f3). No se igualó la fuente de Apple.

## Fuente

Archivo de Instagram que pasó el propietario el 2026-11-05: SHA-256 `515901fe…a74a`, 720×1280, 180 fotogramas a 29,97 fps, 6,006 s. **No es byte-idéntico al original documentado** (`74301c7f…`, 512×910, 181 fotogramas): a este le falta el primer fotograma (desfase −1, SSE 0,000155) y sus tres picos caen en 122/127/116 como en el documentado. El `source.MP4` local anterior es **una recodificación de este archivo** (PSNR mediano 45,7 dB con desfase de 2 fotogramas). Es la mejor fuente disponible y se usa como referencia principal. No se versiona.
