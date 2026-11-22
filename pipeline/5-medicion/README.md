# 5. Medición

**Responsabilidad:** anotar lo que cada plataforma muestra de cada pieza, sin interpretarlo.

| | |
| --- | --- |
| Entra | Números que el propietario lee en Instagram y TikTok |
| Sale | `resultados.csv`: una fila por pieza, plataforma y lectura |

Reglas del registro manual:

- Una fila nueva por cada lectura; no se sobrescribe la anterior. Lecturas recomendadas: 48 horas y 7 días.
- `horas_desde_publicacion` y `fuente_dato` (por ejemplo «captura de Insights del propietario») son obligatorios.
- Lo que la plataforma no muestre se deja vacío. Nunca se estima.
- Instagram da `skip_rate_pct`; si no hay retención a 3 segundos, se anota solo ese.
- `origen` siempre es `real` en este archivo. Los datos inventados viven únicamente en [`../pruebas/circuito/`](../pruebas/circuito/).
