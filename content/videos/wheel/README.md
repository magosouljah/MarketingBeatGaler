# wheel — rueda de portadas (rolodex) al estilo Apple Music

Video de 6 s de la cuenta 1: una rueda de portadas que aparece, gira y se apila como un rolodex. Cierra con la oferta «1 month of Unlimited Free* Storage» y el código FREEGALER. Es la línea de trabajo que empezó como [orbit](../orbit/), hoy archivado: aquellos prototipos nunca se aprobaron, mientras que esta reconstrucción sí.

| Carpeta | Qué es | Estado |
| --- | --- | --- |
| [lab-v1/](lab-v1/) | Laboratorio A/B/C: órbita rígida, trayectorias con profundidad y cámara 3D ([RESULTS](lab-v1/RESULTS.md)) | Sin aprobación; el propietario eligió la dirección de A (portadas ordenadas) |
| [lab-v2/](lab-v2/) | La rueda, de v2 a v7 ([RESULTS](lab-v2/RESULTS.md), [LEARNINGS](lab-v2/LEARNINGS.md)) | **wheel-v7 aprobado** por el propietario el 2026-11-06: «ok finalizamos me encanta» |
| [songs-v1/](songs-v1/) | 8 videos sobre v7: 4 canciones × fondo negro y blanco ([README](songs-v1/README.md)) | Entregados el 2026-11-07; no hay feedback registrado sobre sus 3 puntos abiertos |

Todo lo aprendido, de punta a punta: **[LEARNINGS.md](LEARNINGS.md)**.

- **Casos:** `learning/cases/choreography-lab-v1-*`, `choreography-lab-v2-wheel` … `choreography-lab-v7-wheel`, `apple-orbit-phase2-rerun-v1` y `phase2-songs-v1`.
- **Material local, no versionado:** referencia de Apple en `reference-runs/`; canciones en `work/songs/`; MP4 en `work/phase2-lab-v2-final/` y `work/phase2-songs/`.
- **Historia en Git:** la línea se hizo en las ramas `experiment/phase2-3d-choreography-lab-v1` (PR #5) y `experiment/phase2-songs-v1` (PR #6). El 2026-11-16 se unieron a `main` con merge, sin squash, así que los hashes que citan los casos (p. ej. `f004327` para v7) siguen existiendo. Las carpetas se movieron de `content/assets/choreography-lab-v1|v2` y `phase2-songs-v1` a esta.
