# Zonas seguras de Instagram (Reels) — medidas reales

Medido el 2026-11-14 sobre una captura del iPhone del propietario (pantalla alta con isla dinámica, Reel abierto desde un mensaje), con un video de 1080×1920. Coordenadas en píxeles del video.

Instagram escala el video hasta llenar el alto de la pantalla. Como la pantalla es más alta que 9:16, **recorta los lados**.

| Zona | Medida | Qué hay |
| --- | --- | --- |
| Lados | ~49 px por lado; visible x = 49–1031 | Fuera de pantalla |
| Arriba | y < ~250 | Isla dinámica (x 390–695, y 33–154) y barra superior de Instagram |
| Derecha | x 915–990, y 1208–1858 | Me gusta, comentar, compartir, guardar |
| Abajo | y > ~1683 | Usuario y descripción |

## Reglas de composición

- Nada legible en los primeros 250 px ni en los 49 px de cada lado. Margen cómodo: x = 80–1000.
- Texto y CTA entre y ≈ 270 y y ≈ 1200 si deben verse completos; lo que quede bajo los botones o la descripción puede ser imagen, no mensaje.
- Una ventana de interfaz se muestra **flotando completa**, con sus bordes y el fondo alrededor. No se agranda su barra de título para esquivar la isla.
- El fondo sí va a sangre: lo recortado tiene que ser fondo.

## Comprobar

```bash
python shared/technical-qa/phone_guide.py frame.png      # -> frame-phone.jpg
```

Pinta en rosa lo que no se ve o queda bajo la interfaz. Pasarlo por los frames clave antes de un render largo.

## Límites de esta medida

Es un solo teléfono y una sola vista (Reel abierto desde un mensaje). El feed, la pestaña de Reels y otros modelos pueden diferir unos píxeles. Regla en estado de **propuesta** (`instagram-safe-zones-measured`): falta que el propietario confirme la última entrega en su teléfono.
