# Lab V2 — resultados de la iteración 1

**No es aprobación creativa.** Medición técnica y autoevaluación del agente. Caso: `choreography-lab-v2-wheel`.

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
