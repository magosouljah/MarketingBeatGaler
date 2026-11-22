# 6. Aprendizaje (audiencia)

**Responsabilidad:** contrastar lo que se predijo con lo que pasó y decir qué cambia en nuestra comprensión del productor. El aprendizaje de producción vive en [`learning/`](../../learning/).

| | |
| --- | --- |
| Entra | Hipótesis y experimentos del módulo 3, piezas del 4, lecturas del 5 |
| Sale | Un informe por experimento en `informes/`, registrado en `informes.csv`; cambios de estado en `hipotesis.csv`; preguntas nuevas en el módulo 1 |

`python pipeline/pipeline.py aprender X-001 --escribir` deja un borrador con la predicción, las tablas y los avisos. Las respuestas 4 a 8 las escribe quien analiza.

Las ocho preguntas: qué predijimos, qué ocurrió, qué explicación propusimos, qué evidencia la respalda, qué otras explicaciones siguen siendo posibles, qué aprendimos realmente, qué preguntas nuevas aparecieron y qué deberíamos probar después.

Tres niveles que no se confunden:

1. **Resultado observado:** la pieza tuvo más retención.
2. **Interpretación:** posiblemente el arranque contribuyó.
3. **Explicación causal:** el mecanismo produjo la diferencia.

Un buen resultado no convierte una hipótesis en regla, y pocas vistas no descartan un mecanismo. «Todavía no sabemos» es una respuesta válida.
