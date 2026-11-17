# fuck

Anuncio vertical de BeatGaler para Instagram (cuenta 1), motion graphics sobre un solo canvas con la cámara viajando: los logos de Dropbox, Google Drive y Untitled caen a un bote de basura; unas notas forman un archivo, una nube se lo traga junto con una avalancha de beats, explota en el drop y de ahí sale la Gallery; clic derecho, Share, y un avión de papel vuela al CTA.

El propietario lo llama «guion fuck».

| | |
| --- | --- |
| **Estado** | **Cerrado y aprobado el 2026-11-16** («perfecto ok quedo bien»). Siete entregas en una tarde. Evaluación ponderada: **50.0 de 100** (Animación 3, Estética 2, Originalidad 1, Consistencia 3, B-roll 2, Realismo 4, Acabado 3), sin comentarios por criterio. |
| **Formato** | 1080×1920, 30 fps, 12.9 s (387 frames), solo orgánico, con voz y beat del propietario |
| **Herramienta** | Un solo `index.html` con Canvas 2D y una función `render(t)`; Chrome (Playwright) lo filma cuadro por cuadro y FFmpeg une y mezcla. **No** usa HyperFrames (ver [por qué](LEARNINGS.md#5-técnica)). |
| **Fuente** | [`project/index.html`](project/index.html): cámara por keyframes (`K`), una función por escena (`scene1`…`scene5`) y `renderT` para el retiming |

## Documentos

- [BRIEF.md](BRIEF.md): el guion del propietario y lo que se cerró preguntando.
- [LEARNINGS.md](LEARNINGS.md): **todo lo aprendido**, creativo, técnico y de proceso.
- [HISTORY.md](HISTORY.md): las siete entregas con el feedback textual.
- Casos: `learning/cases/fuck-*.json`. Ocho lecciones validadas con la aprobación de la final y dos propuestas abiertas.

## Renderizar

```bash
# 1. Poner los siete archivos fuente en inputs/  (ver inputs/README.md)
# 2. Desde la raíz del repo:
BEATGALER_REPO=/ruta/a/beatgaler bash account-1/videos/fuck/tools/render.sh
# -> account-1/videos/fuck/out/fuck.mp4 y fuck-frames.mp4 (copia con contador)
```

Requiere Python 3.10+ con Pillow, numpy, scipy y playwright, Chrome (`CHROME=/ruta` si Playwright no trae el suyo), FFmpeg y la fuente Inter Display instalada. Tarda unos 2 minutos: los cinco tramos se filman en paralelo. Comprobado el 2026-11-16 desde este repo: reproduce la final cuadro por cuadro (PSNR infinito en video, mismo MD5 en audio).

Para rehacer una sola escena: `SEGMENTS="s4" bash …/render.sh`. Frames sueltos para revisar antes de renderizar: `python tools/render.py frames out 0.3 6.2 9.45` (tiempos de video; el servidor local debe estar corriendo en `project/`).

`inputs/`, `out/` y `project/assets/` están ignorados por Git. El repositorio es público: los logos de terceros, las fotos del bote, la voz y el beat **no** se versionaron.

## Línea de tiempo (final)

Frames a 30 fps, en tiempo de video.

| Frames | Segundos | Qué pasa | Voz / texto |
| --- | --- | --- | --- |
| 0–72 | 0–2.4 | Fichas sobre negro: Untitled, Drive, Dropbox, una a una | «Fuck Dropbox, Google Drive and Untitled» / F\*\*K |
| 72–99 | 2.4–3.3 | Sube el bote con basura y la tapa abierta; caen las tres; la tapa azota (F87–89) y el bote sale disparado (F92–97) | |
| 99–134 | 3.3–4.45 | Notas forman el archivo; nace la nube y se lo traga | |
| 134–180 | 4.45–6.0 | Avalancha de archivos desde abajo; la nube se infla sobre el silencio del beat | «Upload» / UPLOAD |
| 180 | 6.0 | **Drop:** la nube explota | |
| 180–228 | 6.0–7.6 | Dispersión rápida y cámara lenta con las portadas girando en 3D | «Store» / STORE |
| 228–258 | 7.6–8.6 | Cada beat cae en su lugar en la Gallery real | «Organize» / ORGANIZE |
| 258–291 | 8.6–9.7 | El cursor llega, se queda quieto, clic derecho (F272), menú, va a Share, quieto, clic (F291) | «And share your music…» / PROPER (F283) |
| 291–318 | 9.7–10.6 | El avión despega y cruza el canvas | «…the proper way» / WAY (F294) |
| 318–387 | 10.6–12.9 | El avión se pliega en el logo; CTA | «Comment GALER to try it for free» |
