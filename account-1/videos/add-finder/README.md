# add-finder

Anuncio vertical de BeatGaler para Instagram (cuenta 1). Un productor busca un beat entre cientos de archivos en el Finder; los archivos se mudan volando a una Gallery de BeatGaler, y un clic en un tag lleva directo al CTA.

| | |
| --- | --- |
| **Estado** | **Cerrado.** Entregado el 2026-11-14; la v5 fue aprobada («me encanta») y el 2026-11-15 el propietario cerró la final v2: «No hagas otra versión, es suficientemente buena». Calificación: 7.0 de 10. |
| **Formato** | 1080×1920, 30 fps, 11.9 s (357 frames), solo orgánico, inglés |
| **Versiones** | `negro`: beat + voz + efectos. `blanco`: mismo video sobre blanco, solo voz. |
| **Herramienta** | [HyperFrames](../../../shared/hyperframes/README.md) 0.9.44 (HTML/CSS/JS), audio mezclado aparte con FFmpeg |
| **Fuente** | [`project/index.html`](project/index.html): una sola función `frame(t)` dibuja todo el anuncio |

## Documentos

- [BRIEF.md](BRIEF.md): el concepto acordado y qué se cortó por el camino.
- [LEARNINGS.md](LEARNINGS.md): **todo lo que aprendimos**, creativo, técnico y de proceso.
- [HISTORY.md](HISTORY.md): las 11 entregas con el feedback textual del propietario.
- Reglas validadas: [`learning/lessons/account-1/`](../../../learning/lessons/account-1/) (22). Casos: `learning/cases/add-finder-*.json`.

## Renderizar

```bash
# 1. Poner el beat, las 4 voces y las 2 capturas de iconos en inputs/  (ver inputs/README.md)
# 2. Desde la raíz del repo:
bash account-1/videos/add-finder/tools/render.sh
# -> account-1/videos/add-finder/out/add-finder-negro.mp4 y add-finder-blanco.mp4
```

Requiere Node 22+, FFmpeg, Python 3.10+ con Pillow y numpy. Tarda unos 12 minutos en 2 CPU. Una sola versión: `THEMES=dark bash …/render.sh`. Copia de revisión con contador de frames: `bash shared/ffmpeg/review_copy.sh out/add-finder-negro.mp4`.

`inputs/`, `out/`, `project/node_modules/` y los assets que copia `tools/prepare.py` están ignorados por Git. El repositorio es público: el beat, las voces y los recortes de iconos **no** se versionaron.

## Línea de tiempo final

Frames a 30 fps; el frame 0 es el inicio del anuncio. La música (versión negra) entra desde 0.546 s del archivo para que su primer kick caiga en el clic.

| Frames | Segundos | Qué pasa | Ancla |
| --- | --- | --- | --- |
| F0–F16 | 0.00–0.55 | La ventana del Finder se asienta; las filas caen en cascada y el contador sube a 847 | |
| F6–F29 | 0.20–0.95 | Entra el cursor y espera abajo | |
| F25–F88 | 0.84–2.94 | Un solo scroll largo con inercia | |
| F25 / F44 / F49 | 0.82 / 1.45 / 1.64 | Bloques HUNDREDS ×3, OF ×8, BEATS ×4 | voz: F26 / F46 / F50 |
| F71–F78 | 2.36–2.60 | Los tres bloques salen hacia arriba | |
| F81 / F107 / F115 / F123 | 2.70 / 3.57 / 3.83 / 4.11 | NO IDEA, WHICH, ONE'S, WHICH | voz |
| F87–F135 | 2.90–4.50 | El cursor visita dos archivos y llega al protagonista | |
| **F144** | **4.80** | **Clic** en `beat_final_v3 (2).wav`: despegan los archivos | kick |
| F160 / F170 | 5.34 / 5.66 | A BETTER, WAY. | voz |
| F168 | 5.60 | Acento en pleno vuelo | caja |
| **F181** | **6.03** | Todo cae en la cuadrícula | kick |
| F184–F224 | 6.14–7.46 | Cada beat muta por su cuenta: portada y luego datos | redoble de caja |
| F218 | 7.25 | Se enciende «BeatGaler» | |
| F229 | 7.645 | Entra la barra de tags; aterriza el cursor | caja |
| F235 | 7.845 | El cursor está sobre «trap» | caja |
| **F242** | **8.07** | **Clic** en el tag: las portadas se dispersan | kick |
| F250–F260 | 8.33–8.68 | Zoom hacia el centro | |
| **F260** | **8.68** | «BeatGaler» del cierre | kick |
| F266 | 8.87 | Píldora «Comment GALER» | caja |
| F293–F328 | 9.77–10.93 | to · try · it · for · **free** | voz |
| **F328** | **10.93** | El cursor toca la píldora | kick y «free» |
| F357 | 11.90 | Fin (fundido de música F340–F357) | |

Voces: `l1a` en 0.30 s, `l1b` en 2.50 s, `l2` en 5.02 s, `l3` en 8.63 s. Clics en 4.785, 8.056 y 10.915 s. Whooshes en 0.80 y 8.12 s.

## Composición para el teléfono

- Ventana del Finder flotante: x 80–1000, y 270–1790, con el fondo visible alrededor.
- Palabras del inicio: mismo margen (x=80) y mismo ancho (920 px) que la ventana.
- Galería a 0.944× y plano abierto a 0.561× para quedar dentro del recorte lateral.
- CTA: marca en y≈470–660, píldora en y≈750–886, frase en y≈1040, cursor centrado en x=540.

Medidas y motivo: [`shared/technical-qa/INSTAGRAM-SAFE-ZONES.md`](../../../shared/technical-qa/INSTAGRAM-SAFE-ZONES.md).
