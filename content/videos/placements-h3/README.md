# placements — A-C1-H3

Variante de [`placements`](../placements/) (A-C1-H1 aprobado). 23.85 s, 1080×1920, 30 fps. Proyecto independiente: se puede renderizar sin la carpeta original.

**Hook:** «Imagine an artist asking you for beats and having nothing ready to send.»

| Qué cambia | Valor |
| --- | --- |
| Tipografía del hook | NOTHING / READY / TO SEND (sin palabra bajo el mensaje: no hay tiempo antes de «nothing») |
| Foto de la Story | `inputs/story.jpg` (aportada por el propietario) |
| Beat | grabación de las 7:20 p.m., ~144 BPM, alargada del mismo modo para poder elegir el punto de entrada |
| Color de fondo | azul |
| Sincronía | `python tools/sync.py` eligió el punto de entrada del beat y movió cada acción libre al golpe o a la corchea más cercana; las palabras de la voz no se movieron |

**No cambia:** voz del cuerpo, conversación, Finder, cursor, iconos, transformación, Gallery, pack, link, FIRE, CTA.

```bash
bash tools/prepare.sh && bash tools/render.sh
```

Estado: entregada el 2026-11-25, sin feedback ni evaluación todavía.
