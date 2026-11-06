# Lab V2 — resultados

**No es aprobación creativa.** Medición técnica y autoevaluación del agente. Casos: `choreography-lab-v2-wheel` (iteración 1), `choreography-lab-v3-wheel` (iteración 2), `choreography-lab-v4-wheel` (iteración 3), `choreography-lab-v5-wheel` (iteración 4), `choreography-lab-v6-wheel` (iteración 5) y `choreography-lab-v7-wheel` (iteración 6).

## Iteración 6 (`wheel-v7.mp4`, 2026-11-06)

Observaciones del propietario sobre v6 (los números de fotograma son aproximados):
1. En Apple las portadas salen rápido, se frenan hacia el fotograma ~50 y vuelven a acelerar hacia el ~93.
2. En el ~116 los ángulos de las portadas siguen mal.
3. El cambio de ángulo del círculo (94–102) no se siente tan suave como en Apple.
4. En Apple ningún texto se queda quieto.
5. Cambiar el texto inferior a «for your beats / and projects» y subirlo, como en Apple.

Además dio la oferta: 1 mes gratis con código, luego $11/mes en USD, con renovación automática; pidió que el código vaya en una pill como el «Activar ahora» de Apple y un «1 month of» encima del titular.

Cambios:
1. **Velocidad:** la velocidad angular de la rueda se volvió a trazar sobre el giro en pantalla de Apple (rotacional del flujo óptico), fotograma a fotograma. La rueda queda casi quieta hasta 1,4 s, tiene su pico a 1,6 s (fotograma 48), va más lenta a 2,45 s (~75) y vuelve a acelerar entre 2,8 y 3,15 s. La velocidad mediana por fotograma (`evidence/speed-curve-v7.json`, px/fotograma a 360 px de alto) da:

| Fotograma | 45 | 48 | 51 | 72 | 75 | 90 | 96 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Apple | 0,75 | 0,87 | 0,77 | 0,54 | 0,55 | 0,89 | 1,11 |
| v6 | 0,54 | 0,61 | 0,61 | 0,56 | 0,57 | 0,87 | 1,08 |
| v7 | 0,77 | 0,76 | 0,78 | 0,49 | 0,51 | 0,95 | 1,04 |

   v6 se movía casi a velocidad constante; v7 tiene el arranque rápido, el freno y la segunda aceleración.
2. **Ángulos del ~116:** en v6, la portada cercana tenía un borde lateral a ~30° y el otro a ~80°, porque estaba muy cerca de un lente gran angular. En Apple ambos bordes van a ~55°, y la pila se ve como capas casi del mismo tamaño, como con un teleobjetivo. v7 cierra el lente de 62° a 50° durante el acercamiento (`fovTrack`, nuevo en `wheel.js`) mientras la rueda se queda más atrás (efecto *dolly zoom*): el tamaño en pantalla se mantiene y la perspectiva se aplana. La pila también sube y se corre a la izquierda, donde está la de Apple: en los fotogramas 110–130, el IoU de silueta sube de 0,36 a 0,47. Al final la rueda acelera para que las últimas portadas salgan a ~4,45 s (Apple ~4,47 s).
3. **Giro del círculo:** el giro de pantalla ya no hace la pausa de 3,4–3,5 s que tenía v6, y el anillo sube un poco mientras gira, de modo que su arco cercano se acerca a la palabra, como en Apple (fotogramas 100–108). «Storage» entra a 3,03 s (Apple: fotograma 91); en v6 entraba a 3,07 s, dos fotogramas tarde.
4. **Texto siempre en movimiento** (medido en Apple): cada palabra del centro entra al ~85 %, abajo y ladeada, llega al ~95 % en ~5 fotogramas y después nunca se detiene. Sigue creciendo hasta el 100 % (+5 %) y subiendo ~26 px, cada vez más despacio, y todavía se mueve cuando la reemplaza la siguiente («1 mes»: de 212 a 223 px de ancho y 23 px hacia arriba en los fotogramas 71–87). En el cierre, el titular entra al 86 % y hace un zoom lento en su lugar (Apple: del 93 % al 100 % de su ancho final); el texto inferior, la pill y la letra pequeña suben ~14 px; la marca y «1 month of» crecen un 3 %. En Apple el logo es lo único que se queda quieto; aquí también se mueve, por indicación del propietario.
5. **Cierre:** marca, titular, texto inferior en dos líneas, pill y letra pequeña colocados en las posiciones medidas en Apple: 0,158 / 0,27–0,40 / 0,51–0,54 / 0,59 / 0,64 del alto. «1 month of» va entre la marca y el titular. La pill dice «CODE: FREEGALER». Letra pequeña: «*New users only. Use code FREEGALER at sign-up for 1 month free, then $11/month (USD). Renews automatically until canceled. Terms apply.» **FREEGALER es un código inventado para el laboratorio: hay que darlo de alta en BeatGaler antes de publicar.**

| Medida | v6 | v7 |
| --- | ---: | ---: |
| IoU por fotograma, media 1,23–4,4 s | 0,45 | **0,46** |
| — aparición / rueda / acercamiento / riffle | 0,37 / 0,52 / 0,36 / 0,47 | 0,36 / 0,53 / **0,42** / 0,46 |
| Puntaje de pose 1,3–4,3 s (IoU, orientación de bordes) | 0,44 (0,45, 0,87) | **0,47** (0,46, 0,88) |
| Oclusión en el acercamiento (Apple 0,58) | 0,43 | **0,45** |
| Arco de energía (Apple 0,24 / 0,45 / 0,65 / 1,00) | 0,19 / 0,49 / 0,73 / 1,00 | 0,23 / 0,56 / 0,79 / 1,00 |

Sigue abierto:
- **El giro durante la aparición no venía de la rueda.** Con la rueda casi quieta hasta 1,4 s, el rotacional del flujo en la aparición sigue en 4,0 (Apple 0,56). La hipótesis de v6 queda descartada; ahora la sospecha es cómo crecen las portadas al aparecer.
- **El giro en pantalla después del cambio de ángulo no se apaga del todo** (fotogramas 99–108: rotacional 2,1–3,5; Apple ~0). Bajar o subir la velocidad de la rueda en ese tramo no lo corrige de forma monótona.
- **Riffle:** en v7 es relativamente más lento que en Apple: el arco de energía de rueda y acercamiento queda más alto que el de Apple.

## Iteración 5 (`wheel-v6.mp4`, 2026-11-06)

Observaciones del propietario sobre v5: (1) los fotogramas 41–50 se veían mejor en v4; (2) las palabras del centro entran con una animación que hay que replicar; texto nuevo «Unlimited» / «Free*» / «Storage»; (3) en el fotograma ~94 el cambio de ángulo es brusco; (4) en el ~94 las portadas están más planas que en Apple (v4 se parecía más) y en el ~116 más horizontales.

Cambios:
1. **Entrada:** vuelve a la inclinación de v4 y a sus planos de página (paso de pala 2,59 rad, que equivale al −0,55 de v4 pero con la otra cara hacia la cámara).
2. **Las dos caras de cada página imprimen la misma portada**, con el mismo brillo y la misma orientación. Ninguna página se lee como vista «por detrás». Qué tanto se inclinan los planos lo deciden el paso de pala y el giro (en v5 vimos que la inclinación de v4 estaba al revés).
3. **Ángulo del círculo:** el giro empieza antes (2,9 s) y termina después (3,4 s). Por fotograma, el eje mayor ahora da 1° / −8° / −30° / −52° a 3,0 / 3,1 / 3,2 / 3,3 s, frente a 10° / −15° / −34° / −54° de Apple. v5 daba 31° / 29° / −4° / −57°: un salto de 53° en 0,1 s, que es lo brusco que viste.
4. **Clímax:** paso de pala 2,35, elegido comparando lado a lado contra 2,2, 2,5 y 2,7; con 2,5 (v5) las portadas quedaban más horizontales. El giro de pantalla se mantiene en −1,1, porque con −1,0 la pila sale del cuadro antes de 4,0 s.
5. **Texto:** «Unlimited» / «Free*» / «Storage» y cierre «Unlimited Free* Storage / for beats and projects». Animación medida en Apple fotograma a fotograma: cada palabra entra por corte unos 26 px abajo y con −3,5° de inclinación, sube a su lugar en unos 4 fotogramas (ease-out) y sigue subiendo despacio hasta que entra la siguiente. En el cierre, la marca y la línea inferior aparecen primero (4,3 s) y las tres líneas del titular entran juntas a 4,37 s, asentándose hacia arriba. La primera palabra entra a 1,53 s, como en Apple.

| Medida | v4 | v5 | v6 |
| --- | ---: | ---: | ---: |
| IoU por fotograma, media 1,23–4,4 s | 0,38 | 0,43 | **0,45** |
| — aparición / rueda / acercamiento / riffle | 0,36 / 0,49 / 0,34 / 0,25 | 0,32 / 0,49 / 0,33 / 0,46 | **0,37 / 0,52 / 0,36 / 0,47** |
| Orientación de bordes (1 = igual) | — | 0,83 | **0,87** |
| Error medio del eje mayor | 0,36 | 0,13 | **0,12** |
| Arco de energía (Apple 0,24/0,45/0,65/1,00) | 0,33/0,98/1,00/0,83 | 0,14/0,51/0,76/1,00 | **0,19/0,49/0,73/1,00** |
| Oclusión en el acercamiento (Apple 0,58) | 0,30 | 0,34 | **0,43** |

En el 19 % del área visible se ve la cara trasera de una página; como ahora imprime la misma portada con el mismo brillo y la misma orientación, se ve igual que el frente.

Sigue abierto: la rueda gira durante la aparición (curl 4,0 contra 0,56 de Apple).

## Iteración 4 (`wheel-v5.mp4`, 2026-11-06)

Observaciones del propietario sobre v4: (1) hacia el fotograma 99 el ángulo del círculo de Apple está entre 45° y 90° y el nuestro en casi −45°; (2) en los fotogramas 106–108 se ve el reverso de las portadas, algo que en Apple nunca pasa; (3) desde el fotograma 120 subía todo el círculo para compensar el ángulo; en Apple las portadas salen solas y las que salen del cuadro no vuelven a entrar por abajo.

Qué medí y qué encontré:
- **Ángulo:** el eje mayor de la silueta (por momentos de segundo orden, con y hacia arriba) en Apple pasa de +28° a 1,9 s a **−54° a 3,3 s (fotograma 99)** y −60° a 3,8 s. El de v4 se quedaba en +15° a +31° todo el tiempo. Nuestra medición confirma la diferencia que viste.
- **Reversos:** la geometría exacta de v4 mostraba la cara de atrás en el **60 % del área visible** (86 % en la rueda). La métrica de silueta no lo podía ver, porque el reverso ocupa exactamente la misma forma.

Cambios:
1. Nueva herramienta `tools/fit_pose.py`, que puntúa cada pose con cuatro medidas: silueta (IoU), orientación de los bordes de las portadas, área de reverso visible (desde la geometría) y error del ángulo del eje mayor.
2. Paso de pala 2,2 rad (= π − 0,94): toda página visible muestra su frente (reverso visible 0,1 % en la rueda). Las páginas son de una sola cara; una página que gira su espalda hacia la cámara desaparece justo cuando está de canto, así que nunca se ve un reverso ni hay saltos.
3. El círculo gira sobre el eje de la vista hacia −0,8 rad entre 3,0 y 3,3 s y hacia −1,1 rad en el clímax, ajustado para que el ángulo siga al de Apple: **−56,8° contra −53,6° en el fotograma 99** (v4: +15,6°).
4. **La rueda ya no sube.** Se queda en su sitio y el giro saca las portadas del cuadro. Cada portada que sale del cuadro desde 3,55 s se retira para siempre, calculado una sola vez al cargar, así que no vuelve a entrar por abajo.

| Medida | v4 | v5 |
| --- | ---: | ---: |
| IoU de silueta por fotograma, media 1,23–4,4 s | 0,38 | **0,43** |
| — aparición / rueda / acercamiento / riffle | 0,36 / 0,49 / 0,34 / 0,25 | 0,32 / 0,49 / 0,33 / **0,46** |
| Reverso visible (área) | 60 % | **0 %** |
| Error medio del eje mayor | 0,36 | **0,13** |
| Arco de energía (aparición/rueda/acercamiento/riffle; Apple 0,24/0,45/0,65/1,00) | 0,33/0,98/1,00/0,83 | **0,14/0,51/0,76/1,00** |
| Cobertura / oclusión en el riffle (Apple 0,32 / 0,78) | 0,16 / 0,78 | **0,31 / 0,78** |

Sigue abierto: durante la aparición la rueda gira más que la de Apple (curl 3,7 contra 0,56) y las páginas se ven más de canto, con menos caras (IoU 0,32 contra 0,36 en v4); la oclusión del acercamiento sigue en 0,34 contra 0,58.

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
