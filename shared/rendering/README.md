# Render cuadro por cuadro en Python

Notas para hacer un video con Python + OpenCV + Pillow + FFmpeg, sin navegador. Salieron de [llama](../../content/videos/llama/) (2026-11-12): 441 frames de 1080×1920 en 85 s con 2 CPU.

**No sustituye a HyperFrames**, que es la herramienta elegida en `FASE-0.md`. Sirve cuando el video necesita lo que el HTML hace mal: metraje real remapeado en el tiempo, efectos por píxel (fuego, ruido) o muchos planos 3D con textura. Para interfaz real de la app, tipografía y CSS, usar [HyperFrames](../hyperframes/README.md).

## Estructura

```
project/common.py   constantes de tiempo, helpers (texto, planos 3D, transiciones, fuego)
project/<escena>.py una función pura frame(t) -> imagen BGR uint8 de 1080x1920
project/render.py   escena + rango de frames -> out/<escena>.mp4
tools/prepare.py    inputs/ -> out/assets/ (texturas, audio)
tools/render.sh     prepare, escenas en paralelo, unión, audio
```

- **`frame(t)` pura**: depende solo de `t`. Cualquier frame se dibuja suelto y las escenas se renderizan en paralelo.
- **Tiras de frames sueltos**: cada escena, ejecutada con una lista de segundos, escribe una tira reducida (`python project/bg.py 9.3 9.9`). Mirar 8 instantes cuesta ~1.5 s; es la forma de revisar antes de un render.
- **Tiempos como constantes con nombre** en `common.py`, derivados de los golpes medidos del audio. Mover un golpe es cambiar un número.

## Render

- Cada escena envía sus frames en crudo por tubería a FFmpeg (`-f rawvideo -pix_fmt bgr24`), sin PNG intermedios.
- Un archivo por escena, todos con el mismo tamaño, fps, códec y `-video_track_timescale`. Se unen con el demuxer `concat` y `-c copy`; el audio se añade después.
- Si cambia una escena, se vuelve a renderizar solo esa.
- Escribir a un nombre temporal que termine en `.mp4` y renombrar cuando FFmpeg sale con 0: un render interrumpido deja un archivo corto que aun así se reproduce.
- Entrega para teléfono: `-crf 22 -maxrate 8M -bufsize 12M -g 30 -movflags +faststart`. A 16 Mbps el propietario lo vio trabado.
- El grano encarece: σ 5 daba 30 MB en 14.7 s; σ 3, 15.6 MB.

## Planos 3D

`plane()` rota las cuatro esquinas de una textura, las proyecta con una cámara de agujero (`x' = f·X/(f+Z)`) y dibuja con `cv2.getPerspectiveTransform` + `warpPerspective` solo dentro de la caja que ocupa el plano.

- El borde cercano tiene que quedar **delante de la cámara**: si su profundidad llega a `-f`, el resultado es basura. Alejar el plano, reducirlo o alargar `f`.
- Comprobar el signo de la inclinación con un frame suelto: un suelo puede salir como techo.
- Varios planos: ordenar por profundidad media y pintar del más lejano al más cercano.
- Scroll sobre una textura repetible: `np.roll`.

## Transición de golpe

Durante los primeros 0.2 s de cada toma, con `q = 1 − easeOut(t/0.2)`: zoom `1 + 0.20·q`, desplazamiento o giro según el tipo, desenfoque en la dirección del movimiento, separación de los canales rojo y azul de `16·q` px y brillo `1 + 0.5·q`. En los últimos 0.07 s, un zoom que acelera. Rotar el tipo (zoom, barrido ×4, giro) para que dos tomas seguidas no entren igual.

## Fuego procedural

`fire()` en `common.py`:

1. Tres texturas de ruido repetibles (ruido blanco desenfocado con σ 22, 10 y 4) que suben a velocidades distintas.
2. Máscara radial desde un origen: `grow` 0→1 la hace crecer hasta llenar el cuadro; a partir de 0.85 se suma blanco.
3. `hole` 0→1 abre un agujero desde el centro para revelar lo que hay debajo.
4. Tabla de color negro → rojo → naranja → amarillo → blanco.
5. Todo a 270×480, ampliado ×4.

Muestrear el ruido con `cv2.remap(..., borderMode=cv2.BORDER_WRAP)`. Envolver las coordenadas con `%` antes de interpolar deja costuras rectas.

## Texto y logotipos desde capturas

- Texto nuevo: Pillow a 2× o 3× y reducir con Lanczos.
- Un logotipo blanco sobre negro sacado de una captura pequeña: ampliar ×5 (bicúbico), desenfocar σ 2.5 y aplicar un umbral suave (`clip((v−118)/22 + 0.5, 0, 1)`). Sirve como máscara nítida a cualquier tamaño.
- El texto pequeño de interfaz de una captura no aguanta ampliarse: se vuelve a escribir. Mejor aún, leer el componente real (lección `real-product-ui-components`).

## Metraje dentro del video

- Leer todos los frames del clip a memoria y elegirlos con una tabla «segundo del video → segundo del clip» (`np.interp`).
- Al acelerar, **promediar** los cuadros fuente que cubre cada cuadro de salida. Tomar el más cercano se ve a tirones.
- Ampliar con Lanczos y máscara de enfoque (`addWeighted(f, 1.6, blur σ4, −0.6)`). Un clip de 480p recortado y ampliado 3× se nota blando al lado de gráficos nítidos.
