# Revisión independiente V1.3 — rigor antes de novedad

Empieza **después** de guardar el lote. Leer `inputs/ideacion-01.json`, fuentes declaradas, `pipeline/evaluacion/referencias-historicas.json` y guiones anteriores **solo en este segundo contexto**. Ejecutar `python pipeline/ideacion.py revisar inputs/ideacion-01.json`. Cero coincidencias automáticas NO demuestra originalidad.

## Orden de descarte (sin puntajes inventados)

1. **Relevancia:** ¿por qué le importaría a un productor concreto? ¿Qué consecuencia sustancial aparece? Si el video se basa en una frivolidad sin valor suficiente, **rechazar**, aunque sea ingenioso.
2. **Causa de la atención:** ¿qué estímulo perceptible genera una reacción o curiosidad real? ¿Qué mecanismo conecta estímulo y deseo, con explicaciones alternativas? No aceptar etiquetas («sorpresa + curiosidad») como razonamiento.
3. **Desarrollo:** ¿el video satisface la tensión, demuestra algo útil o produce un resultado valioso? ¿El final justifica haber visto el inicio?
4. **Veracidad:** ¿hay afirmaciones o funciones no verificadas? La presencia de BeatGaler puede ser ninguna, discreta, indirecta o directa; no forzar una venta para cerrar el video.
5. **Novedad:** comparar acontecimientos centrales con el historial y entre candidatos, **sin convertir el pasado en plantillas**. La semejanza por sí sola no sustituye los filtros anteriores.
6. **Variedad:** es un beneficio opcional, **no un criterio de selección**. Aceptar tres del mismo territorio si todos son fuertes; aceptar uno o ninguno si no hay más.

**Resultado editorial:** aceptado, revisar o descartar para cada candidato desarrollado, con una explicación concreta (qué deseo, qué consecuencia, qué reacción, cuál es la objeción). Permitir que sobrevivan **cero a tres**; si cero, registrar por qué y regresar a investigación. No crear tres guiones débiles para completar una entrega. Separar los gustos del propietario, evidencia externa, métricas reales y calidad audiovisual.

**Aprendizaje:** las referencias históricas son diagnósticos puntuales, no votos de gusto ni evidencia de rendimiento. El criterio final de calidad creativa requiere evaluación humana; la calidad en audiencia requiere publicar y medir.

**Pruebas:** ejecutar unit tests del validador, realizar una ronda creativa real y comprobar manualmente que el revisor puede rechazar todas las ideas triviales. Un lote inventado no es una prueba de efectividad.
