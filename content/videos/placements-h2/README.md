# placements — A-C1-H2

Variante de [`placements`](../placements/) (A-C1-H1 aprobado). 24.51 s, 1080×1920, 30 fps. Proyecto independiente: se puede renderizar sin la carpeta original.

**Hook:** «Imagine missing your first major placement because you couldn't find the right beat in time.»

| Qué cambia | Valor |
| --- | --- |
| Tipografía del hook | PLACEMENT bajo el mensaje; RIGHT / BEAT / IN TIME |
| Foto de la Story | `inputs/story.jpg` (aportada por el propietario) |
| Beat | grabación de las 6:58 p.m., ~122 BPM. Duraba 19.3 s: se repiten dos compases (5.94–13.81 s) para cubrir el video |
| Color de fondo | rojo oscuro |
| Sincronía | `python tools/sync.py` eligió el punto de entrada del beat y movió cada acción libre al golpe o a la corchea más cercana; las palabras de la voz no se movieron |

**No cambia:** voz del cuerpo, conversación, Finder, cursor, iconos, transformación, Gallery, pack, link, FIRE, CTA.

```bash
bash tools/prepare.sh && bash tools/render.sh
```

Estado: entregada el 2026-11-25, sin feedback ni evaluación todavía.
