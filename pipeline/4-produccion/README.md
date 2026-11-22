# 4. Producción

**Responsabilidad:** convertir un guion aprobado en una pieza publicable. No decide qué decir.

| | |
| --- | --- |
| Entra | Guiones aprobados del módulo 3 |
| Sale | `piezas.csv`: una fila por pieza, con su guion, experimento, rol, cuerpo y estado |

Este módulo no duplica nada: usa lo que ya existe.

| Qué | Dónde |
| --- | --- |
| Cuerpos | [`account-1/videos/`](../../account-1/videos/) |
| Herramientas | [`shared/`](../../shared/) |
| Lecciones visuales y evaluación | [`learning/`](../../learning/) |
| Features que se pueden mostrar | [`research/product/FEATURES-V1-V2.md`](../../research/product/FEATURES-V1-V2.md) |

`estado`: `planificada`, `producida`, `aprobada`, `publicada`, `descartada`. `ejecucion` se llena solo si algo quedó mal hecho; si empieza por «mal», la pieza queda fuera de las comparaciones del módulo 6.

## Plantilla de arranques

[`arranque/`](arranque/) produce los primeros segundos de una pieza a partir de una orden en JSON, sin escribir código nuevo por pieza.

```bash
python pipeline/4-produccion/arranque/producir.py P-0001                                   # solo el arranque
python pipeline/4-produccion/arranque/producir.py P-0001 --cuerpo add-finder.mp4 --desde 4.8   # pieza completa
```

- `arranque/ordenes/<pieza>.json`: qué aparece y cuándo. Tres elementos disponibles: `texto`, `contador` y `campo`.
- `arranque/out/` (no se versiona): el arranque, la pieza completa si se pasó `--cuerpo`, y la copia con contador de frames.
- La plantilla rechaza cualquier elemento fuera de la zona útil (y de 120 a 1590) y ajusta el texto al ancho útil.
- Hoy solo hace arranques de texto sobre fondo negro, sin voz. Para otro tipo de arranque hay que añadir un elemento a `index.html`.
- Los cuerpos no están en el repositorio: el MP4 terminado lo aporta el propietario. `--desde` es el segundo donde aparece el producto.
