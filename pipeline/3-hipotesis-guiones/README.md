# 3. Hipótesis, selección y guiones

**Responsabilidad:** convertir un árbol en predicciones que se puedan comprobar, elegir cuáles se prueban y escribir sus guiones.

| | |
| --- | --- |
| Entra | Árboles del módulo 2 |
| Sale | `hipotesis.csv`, `guiones.csv` con sus archivos en `guiones/`, y `experimentos.csv` |

- **Hipótesis:** cita los nodos que pone a prueba, y trae `prediccion` y `refutacion` escritas antes de publicar. `estado`: `propuesta`, `reforzada`, `debilitada`. Ninguna se borra y ninguna pasa a «demostrada».
- **Selección:** la columna `seleccion` dice por qué se eligió esta y no otra. Generar muchas candidatas no obliga a producirlas.
- **Guion:** arranque, cuerpo que lo paga, cierre y lista de pendientes. `aprobado_por_propietario` empieza en `no`.
- **Experimento de contraste:** dos guiones que difieren en un solo elemento (`que_cambia`) y comparten el resto (`que_se_mantiene`). El contraste se produce con el mismo cuidado visual que la prueba.
