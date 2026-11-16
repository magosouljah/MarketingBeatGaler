# llama

Video vertical de BeatGaler para Instagram (cuenta 1), sobre la plantilla del reel «transición de fuego»: un escritorio lleno de proyectos sin orden, un productor frustrado que no encuentra su archivo, un encendedor y un perfume, una explosión de fuego en el drop, y al otro lado BeatGaler en doce tomas que cambian de perspectiva y de forma en cada golpe de la música.

El propietario lo llama «video de llama chico frustrado».

| | |
| --- | --- |
| **Estado** | **Entregado, sin cerrar.** Seis entregas el 2026-11-12; la última es la v5. No hubo feedback sobre la v5, ni aprobación explícita, ni cuestionario 1-10. |
| **Formato** | 1080×1920, 30 fps, 14.7 s (441 frames), solo orgánico, sin voz ni texto |
| **Herramienta** | Python + OpenCV + Pillow, cuadro por cuadro, y FFmpeg. **No** usa HyperFrames (ver [por qué](LEARNINGS.md#6-python--opencv-cuándo-sí-y-cuándo-no)). Un clip de 6 s generado con Higgsfield (Seedance 2.5). |
| **Fuente** | [`project/`](project/): una función `frame(t)` por escena (`desk.py`, `guy.py`, `bg.py`) y constantes de tiempo en `common.py` |
| **Origen** | Se hizo en un chat de claude.ai fuera del repositorio, dos días antes de [add-finder](../add-finder/). Se trajo y documentó aquí el 2026-11-16 a petición del propietario; por eso no siguió las reglas del repo que nacieron después (ver [LEARNINGS.md, sección 8](LEARNINGS.md#8-lo-que-este-video-no-cumple)). |

## Documentos

- [BRIEF.md](BRIEF.md): lo que pidió el propietario y lo que decidió el agente.
- [LEARNINGS.md](LEARNINGS.md): **todo lo aprendido**, creativo, técnico y de proceso.
- [HISTORY.md](HISTORY.md): las seis entregas con el feedback textual.
- Casos: `learning/cases/llama-*.json`. Tres propuestas en `learning/proposals/llama-*`; ninguna lección validada.
- Notas reutilizables: [`shared/rendering/README.md`](../../../shared/rendering/README.md) (render en Python) y [`shared/ai-video/README.md`](../../../shared/ai-video/README.md) (clips de Higgsfield).

## Renderizar

```bash
# 1. Poner los seis archivos fuente en inputs/  (ver inputs/README.md)
# 2. Desde la raíz del repo:
bash account-1/videos/llama/tools/render.sh
# -> account-1/videos/llama/out/llama.mp4
```

Requiere Python 3.10+ con numpy, opencv-python y Pillow, FFmpeg y la fuente Inter (`INTER_DIR=/ruta` si no está en `/usr/share/fonts/opentype/inter`). Tarda 1 min 25 s en 2 CPU: las tres escenas se renderizan en paralelo. Comprobado el 2026-11-16 desde este repo: reproduce la v5 (14.7 s, 15.6 MB).

Un frame suelto de cualquier escena, para revisar sin renderizar todo: `python project/bg.py 9.3 11.2` escribe `out/pv_bg.jpg`; igual con `desk.py` y `guy.py`.

`inputs/` y `out/` están ignorados por Git. El repositorio es público: las capturas de la app, la grabación de referencia con su música, el clip generado y los iconos de FL Studio y Ableton **no** se versionaron.

## Línea de tiempo (v5)

Frames a 30 fps. Todos los cortes están en `common.py`: `PUL` (pulsos del buildup), `T_GUY`, `T_CLICK` y `B` (golpes desde el drop).

| Frames | Segundos | Qué pasa | Ancla en el audio |
| --- | --- | --- | --- |
| F0–F84 | 0.00–2.83 | **Escritorio.** 40 archivos al inicio; 8 más en cada pulso hasta 104 (50 `.flp`, 18 `.als`, 18 `.mp3`, 18 `.wav`). Buscador que escribe `beat final FINAL v3.flp`; cursor nervioso; la cámara empuja y tiembla más cada vez | pulsos cada 0.327 s desde 0.216 |
| F55 | 1.85 | «0 resultados» en rojo, con sacudida | |
| F81–F84 | 2.70–2.83 | Barrido vertical: la cámara sube a la cara | pulso 9 (2.83) |
| F85–F114 | 2.83–3.81 | **Chico.** Se tapa la cara y la arrastra hacia abajo (clip a 2.7×) | |
| F114–F134 | 3.81–4.46 | Cara seria; suben el perfume y el encendedor (1.9×) | pulso 12 (3.81) |
| F134 | 4.46 | Prende la llama | último pulso; empieza el silencio |
| F146 | 4.85 | Rocía | golpecito previo al drop |
| F146–F153 | 4.85–5.12 | El fuego llena el cuadro hasta blanco (fuego del clip + fuego procedural encima) | silencio |
| **F154** | **5.123** | **Drop.** Blanco; el fuego se quema hacia afuera 0.75 s y deja ver la marca | golpe 1 |
| F154 | 5.123 | Anillo de portadas con «BeatGaler» | golpe 1 |
| F174 | 5.794 | El mismo anillo, tumbado y cerca | golpe 2 |
| F193 | 6.446 | Muro de tarjetas en isométrico | golpe 3 |
| F213 | 7.089 | Muro de lado, fugando | golpe 4 |
| F233 | 7.750 | Una tarjeta grande que gira hasta quedar de frente | golpe 5 |
| F253 | 8.443 | Tres tiras inclinadas en sentidos opuestos | golpe 6 |
| F272 | 9.060 | Portada en círculo girando como vinilo | golpe 7 |
| F291 | 9.687 | Filas de géneros en marquesina | golpe 8 (inicio del segundo bucle) |
| F311 | 10.358 | Suelo de tarjetas viniendo a cámara | golpe 9 |
| F330 | 11.010 | Abanico de cinco tarjetas | golpe 10 |
| F350 | 11.653 | Portada + barra del reproductor | golpe 11 |
| F369 | 12.314 | Mosaico en rombos | golpe 12 |
| F390 / F409 / F428 | 13.007 / 13.624 / 14.251 | Cierre: anillo + «BeatGaler» + «Create ur Galer», en tres perspectivas | golpes 13, 14 y 15 |
| F441 | 14.70 | Fin (fundido de audio los últimos 0.35 s) | |

Cada toma entra con 0.2 s de golpe: zoom, barrido o giro, desenfoque de movimiento, separación RGB y un destello.

## En el teléfono

Pasado por `shared/technical-qa/phone_guide.py` el 2026-11-16, **después** de entregar: el buscador y «0 resultados» (y ≈ 150–380) quedan bajo la barra superior de Instagram; la barra del reproductor (x 50–1030) se corta en los lados y su ecualizador cae bajo los botones de la derecha. El cierre sí queda dentro. No se corrigió: el video ya estaba entregado.
