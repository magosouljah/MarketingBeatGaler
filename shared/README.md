# Shared — motor técnico común

Recursos reutilizables para ambas cuentas; **no contiene** gusto creativo, hooks, design guidelines ni feedback que puedan contaminar el perfil editorial de otra cuenta.

| Carpeta | Qué hay |
| --- | --- |
| [`hyperframes/`](hyperframes/README.md) | Cómo usamos HyperFrames 0.9.44: comandos, patrón `frame(t)`, render por tramos, tropiezos |
| [`ffmpeg/`](ffmpeg/README.md) | `review_copy.sh` (contador de frames) y recetas de unión y mezcla |
| [`editing/`](editing/find_hits.py) | `find_hits.py`: kicks y cajas reales de un beat |
| [`transcription/`](transcription/align_words.py) | `align_words.py`: tiempo exacto de cada palabra de una locución |
| [`technical-qa/`](technical-qa/INSTAGRAM-SAFE-ZONES.md) | Zonas seguras de Instagram medidas y `phone_guide.py` |
| [`tools/`](tools/crop_and_rename.py) | `crop_and_rename.py`: recorte cuadrado y numeración de portadas |
| [`reference_analysis/`](reference_analysis/README.md) | Preparación de evidencia de video, reportes y cinemática 2D estimada. No hace visión semántica ni aprobación artística |
| [`research/`](research/README.md) | Contrato de referencias y criterios para verificar outliers |
| [`rendering/`](rendering/README.md) | Render cuadro por cuadro en Python + OpenCV: estructura, planos 3D, transición de golpe, fuego procedural. Complemento de HyperFrames, no sustituto |
| [`ai-video/`](ai-video/README.md) | Clips generados con Higgsfield: costos, el prompt que funcionó, cómo traerlos y montarlos |
| `product-source-assets/` | Reservada (`.gitkeep`); sin funcionalidad todavía |

Dependencias de las utilidades: Python 3.10+, FFmpeg, `numpy`, `librosa` (golpes), `pocketsphinx` (palabras), `Pillow` (guía de teléfono), `opencv-python` (render en Python).
