# Videos — cuenta 1

Un video por carpeta, con su fuente, su brief y lo aprendido.

| Video | Estado | Qué es |
| --- | --- | --- |
| [add-finder](add-finder/) | Cerrado 2026-11-15; calificación 7.0 de 10 | Anuncio de 11.9 s: del caos del Finder a la Gallery y al CTA |
| [llama](llama/) | Entregado el 2026-11-12 (v5), sin cerrar ni calificar; documentado el 2026-11-16 | Plantilla del reel de fuego, 14.7 s: escritorio desordenado, chico frustrado (clip de IA), explosión en el drop y 12 tomas de BeatGaler. Python + OpenCV. [Todo lo aprendido](llama/LEARNINGS.md) |
| [wheel](wheel/) | v7 aprobado el 2026-11-06; 8 versiones con canciones entregadas el 2026-11-07 | Rueda de portadas tipo rolodex (reconstrucción de Apple Music), 6 s, más cierre con oferta. [Todo lo aprendido](wheel/LEARNINGS.md) |
| [orbit](orbit/) | Archivado; rechazado, nunca aprobado | Primeros prototipos de la órbita 3D; la línea siguió en [wheel](wheel/) |

## Video nuevo

1. Leer [`learning/lessons/account-1/`](../../learning/lessons/account-1/) y el [LEARNINGS.md de add-finder](add-finder/LEARNINGS.md).
2. Crear `videos/<nombre>/` con `BRIEF.md`, `project/` y `tools/`. Copiar de add-finder el patrón de `frame(t)`, `prepare.py` y `render.sh`.
3. Medir el audio antes de animar: [`shared/editing/find_hits.py`](../../shared/editing/find_hits.py) y [`shared/transcription/align_words.py`](../../shared/transcription/align_words.py).
4. Componer dentro de las [zonas seguras de Instagram](../../shared/technical-qa/INSTAGRAM-SAFE-ZONES.md).
5. Cada entrega al propietario lleva copia con contador de frames ([`shared/ffmpeg/review_copy.sh`](../../shared/ffmpeg/review_copy.sh)) y se registra como caso en `learning/cases/`.
6. Al cerrar el video, pedir el [cuestionario 1-10](../../learning/scorecard/README.md) y registrarlo.

Material común: portadas en [`../creative-assets/covers/`](../creative-assets/covers/) (60, `cover-002` a `cover-061`; no renumerar, add-finder depende de esos números).
