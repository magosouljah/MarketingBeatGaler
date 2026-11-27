# Videos — BeatGaler Marketing

Un video por carpeta, con su fuente, su brief y lo aprendido.

| Video | Estado | Qué es |
| --- | --- | --- |
| [old-beats](old-beats/) | Versión final entregada el 2026-11-26; sin evaluación ni caso registrado todavía | Guion C-C1-H1, 28.75 s: línea del tiempo 2022–2027, Gallery, grabaciones reales de FL Studio a pantalla completa con drag & drop de la melodía y cierre en el que las portadas de la línea forman la rueda. Filmado con Chrome (función pura de `t`), sin HyperFrames. Variantes de hook como proyectos independientes: [old-beats-h2](old-beats-h2/) (fondo negro, intro del melody pack, 29.23 s) y [old-beats-h3](old-beats-h3/) (fondo gris, beat en 2024, 26.57 s); lo que cambia vive en `project/js/variant.js`. [Decisiones y feedback](old-beats/LEARNINGS.md) · [técnicas](../../pipeline/video/TECNICAS.md) |
| [placements](placements/) | Versión final entregada el 2026-11-25; sin evaluación ni caso registrado todavía | Guion A-C1-H1, 23.4 s con CTA; variantes de hook en [placements-h2](placements-h2/) y [placements-h3](placements-h3/): un artista pide beats en una Story, Finder caótico, Gallery filtrada por `rnb` + `dark`, Quick Pack y link al chat, «FIRE 🔥». HyperFrames por módulos (hook intercambiable, cursor y tipografía reutilizables). [Decisiones y feedback](placements/LEARNINGS.md) |
| [fuck](fuck/) | Cerrado y aprobado el 2026-11-16; evaluación 50.0 de 100 | Anuncio de 12.9 s: los logos de la competencia al bote de basura, la nube que absorbe los beats y explota en la Gallery, Share y avión de papel al CTA. Canvas 2D filmado con Chrome. [Todo lo aprendido](fuck/LEARNINGS.md) |
| [add-finder](add-finder/) | Cerrado 2026-11-15; calificación 7.0 de 10 | Anuncio de 11.9 s: del caos del Finder a la Gallery y al CTA |
| [llama](llama/) | Entregado el 2026-11-12 (v5), sin cerrar ni calificar; documentado el 2026-11-16 | Plantilla del reel de fuego, 14.7 s: escritorio desordenado, chico frustrado (clip de IA), explosión en el drop y 12 tomas de BeatGaler. Python + OpenCV. [Todo lo aprendido](llama/LEARNINGS.md) |
| [wheel](wheel/) | v7 aprobado el 2026-11-06; 8 versiones con canciones entregadas el 2026-11-07 | Rueda de portadas tipo rolodex (reconstrucción de Apple Music), 6 s, más cierre con oferta. [Todo lo aprendido](wheel/LEARNINGS.md) |
| [orbit](orbit/) | Archivado; rechazado, nunca aprobado | Primeros prototipos de la órbita 3D; la línea siguió en [wheel](wheel/) |

## Video nuevo

1. Leer las lecciones pertinentes de [`learning/lessons/`](../../learning/lessons/) (con etiquetas históricas) y los LEARNINGS.md de [fuck](fuck/LEARNINGS.md) (el más reciente) y [add-finder](add-finder/LEARNINGS.md).
2. Crear `videos/<nombre>/` con `BRIEF.md`, `project/` y `tools/`. Copiar de add-finder el patrón de `frame(t)`, `prepare.py` y `render.sh`.
3. Medir el audio antes de animar: [`shared/editing/find_hits.py`](../../shared/editing/find_hits.py) y [`shared/transcription/align_words.py`](../../shared/transcription/align_words.py).
4. Componer dentro de las [zonas seguras de Instagram](../../shared/technical-qa/INSTAGRAM-SAFE-ZONES.md).
5. Cada entrega al propietario lleva copia con contador de frames ([`shared/ffmpeg/review_copy.sh`](../../shared/ffmpeg/review_copy.sh)) y se registra como caso en `learning/cases/`.
6. Al cerrar el video, pedir la [evaluación ponderada](../../learning/scorecard/README.md) (siete criterios, 0 a 5, total sobre 100) y registrarla.

Material común: portadas en [`../assets/covers/`](../assets/covers/) (60, `cover-002` a `cover-061`; no renumerar, add-finder depende de esos números).

Los videos nuevos no se clasifican por cuenta; el contenido educativo y el promocional comparten la misma carpeta. Para registros nuevos usar `account: "content"` sin alterar evidencia histórica.
