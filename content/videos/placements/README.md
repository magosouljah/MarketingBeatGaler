# placements — A-C1-H1

Video vertical 1080×1920, 23.40 s, 30 fps. Guion `A-C1-H1` de [`content/scripts/LOTE-01-27-GUIONES.md`](../../scripts/LOTE-01-27-GUIONES.md).
Un artista pide beats en una Story; el productor responde, filtra su Gallery por `rnb` + `dark`, arma un Quick Pack, copia el link y lo manda. El artista contesta «FIRE 🔥». Conversación ficticia e ilustrativa.

**Estado:** versión final entregada el 2026-11-25, pendiente de y de evaluación del propietario.

## Producir

```bash
bash content/videos/placements/tools/prepare.sh   # assets (necesita inputs/, ver inputs/README.md)
bash content/videos/placements/tools/render.sh    # out/placements-A-C1-H1.mp4 y copia con frames
```

## Estructura

| Archivo | Qué contiene |
| --- | --- |
| `project/js/timing.js` | Deriva todos los tiempos de `variant.js`. |
| `project/js/lib.js` | Curvas, `kf()`, `pulse()`, PRNG. |
| `project/js/type.js` | Tipografía cinética reutilizable (`KW`, `slam`). |
| `project/js/cursor.js` | Cursor-personaje de add-finder convertido en componente con guion de movimientos y clics. |
| `project/js/ig.js` | Chat (Story + DM) y escena 1. |
| `project/js/desk.js` | Finder → Gallery → tags → selección → Quick Pack → link (escenas 2 y 3). |
| `project/js/ig-close.js` | Escena 4: pegar link, enviar, respuesta. |
| `project/js/cta.js` | Cierre con el CTA. |
| `project/js/variant.js` | **Lo único que cambia entre variantes**: hook, tiempos, color, audio. Lo escribe `tools/sync.py`. |
| `tools/sync.py` | Recalcula `variant.js` para otro hook u otro beat (mide golpes y ajusta las acciones). |
| `tools/mix.py` | Mezcla: voz arriba, beat presente, sin ducking, efectos discretos. |
| `tools/make_sfx.py` | Sintetiza los whooshes. |

## Variantes

[`placements-h2`](../placements-h2/) y [`placements-h3`](../placements-h3/) son copias independientes de este proyecto: mismo cuerpo, otro hook, otra foto de Story, otro beat y otro color de fondo. Para una variante nueva: copiar la carpeta, poner los archivos en `inputs/`, escribir `variant.def.json` (tiempos del hook contra la alineación de palabras) y correr `python tools/sync.py`.
