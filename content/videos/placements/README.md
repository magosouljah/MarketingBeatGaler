# placements — A-C1-H1

Video vertical 1080×1920, 21.16 s, 30 fps. Guion `A-C1-H1` de [`content/scripts/LOTE-01-27-GUIONES.md`](../../scripts/LOTE-01-27-GUIONES.md).
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
| `project/js/timing.js` | **Todos los tiempos**, anclados a 808/cajas medidos y a palabras alineadas. `HOOK` es el módulo intercambiable. |
| `project/js/lib.js` | Curvas, `kf()`, `pulse()`, PRNG. |
| `project/js/type.js` | Tipografía cinética reutilizable (`KW`, `slam`). |
| `project/js/cursor.js` | Cursor-personaje de add-finder convertido en componente con guion de movimientos y clics. |
| `project/js/ig.js` | Chat (Story + DM) y escena 1. |
| `project/js/desk.js` | Finder → Gallery → tags → selección → Quick Pack → link (escenas 2 y 3). |
| `project/js/ig-close.js` | Escena 4: pegar link, enviar, respuesta. |
| `tools/mix.sh` | Mezcla: voz arriba, beat presente, sin ducking. |

## Cambiar el hook sin tocar el cuerpo

El cuerpo usa tiempos relativos a `B = HOOK.DUR`. Para H2/H3: reemplazar el objeto `HOOK` (y la escena 1 en `ig.js` si cambia la imagen), la voz `hook.wav` y su `adelay` en `mix.sh`. Si `HOOK.DUR` cambia, los golpes del cuerpo dejan de caer sobre los mismos 808: mover el inicio de la música en `mix.sh` la misma diferencia (en múltiplos de 0.4 s) o volver a medir.
