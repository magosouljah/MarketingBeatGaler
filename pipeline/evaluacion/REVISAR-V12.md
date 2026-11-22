# Revisión creativa V1.2 — contexto separado

Este papel **empieza únicamente después** de guardar el lote exploratorio. No entregar al generador las referencias que siguen ni reescribir su lote antes de evaluar la independencia del intento.

**Entradas del revisor:** lote JSON ya cerrado, `pipeline/evaluacion/referencias-historicas.json` (casos conocidos para detectar repetición; no evidencia de éxito), investigación y mecanismo causal citados, capacidades de producto verificables cuando se afirme algo.

**Comprobación:** `python pipeline/ideacion.py revisar inputs/ideacion-01.json`. El comando detecta ciertas coincidencias de palabras; NO identifica todas las repeticiones semánticas. No interpretar «0 avisos» como originalidad demostrada.

### Decisión editorial sin puntuación falsa

1. **Novedad conceptual:** comparar el *acontecimiento central*, no las palabras. Si cambia el hook, pero se repite el mismo problema, marcar duplicado. También comparar similitudes dentro del lote.
2. **Razonamiento:** ¿qué se desea y por qué importaría ese estímulo? ¿La reacción está supuesta o respaldada? ¿Hay una explicación rival y una razón de fallo?
3. **Valor narrativo:** ¿el desarrollo cumple la promesa, sostiene interés o entrega algo útil? No es obligatorio causar una emoción intensa.
4. **Diversidad:** los finalistas presentan situaciones y caminos de atención distintos, no solo tres nombres de mecanismos.
5. **Producto:** puede no aparecer, aparecer discretamente o dominar. No afirmar capacidades V2 como lanzadas si no se ha comprobado. Eludir conexiones forzadas, no exigir que BeatGaler resuelva cada conflicto.
6. **Aprendizaje:** separar gusto del propietario (decide producción), métricas reales de audiencia (informan rendimiento) y calidad de ejecución audiovisual (otra causa).

**Salida:** aceptado / revisar / descartar por candidato, una razón concreta y reemplazos conceptuales solo si faltan ideas suficientes. El autor de los guiones redacta después de esta revisión, **sin usar los ejemplos históricos como estilos que copiar**. No guardar opiniones aisladas como si fueran resultados medidos.

### Prueba de aceptación

Realizar tres rondas con contextos de generación separados y sin historial visible; el revisor busca duplicaciones **antes** de escribir guiones. Registrar cuántas situaciones realmente diferentes sobrevivieron y qué razones de rechazo hubo; no inventar métricas de audiencia. Los tres recorridos sintéticos del test automatizado solo comprueban el programa, no sustituyen tres pruebas creativas con modelo.
