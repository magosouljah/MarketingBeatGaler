# Regla — cumplimiento real de cada variable

## Lectura obligatoria ANTES de generar

**Antes de seleccionar variables o escribir el primer hook, el agente debe leer íntegramente este archivo (`REGLA.md`) y las bibliotecas de espectador, emoción, valoración y expresión verbal de `formula-hooks/`.** No iniciar generación con reglas recordadas de conversaciones o fragmentos.

**El objetivo es un hook verbal para los primeros ~3 segundos de un video, no un párrafo, explicación o mini-guion.** La duración se verifica según cómo se pronuncia: usar aproximadamente 6–10 palabras en español como orientación, no como límite ciego. Evitar introducciones, justificaciones y respuestas anticipadas.

**Antes de redactar cada candidato, definir qué expectativa concreta se va a abrir en ese espectador y qué información, resultado o explicación quedará pendiente para el video.** La expectativa debe importar al espectador y ser posible de satisfacer en el desarrollo; no crear una pregunta vacía ni inventar una promesa imposible. La definición es planificación interna del candidato, **no una frase que se agrega al hook**.

Solo entonces combinar las variables seleccionadas y redactar el hook. La evaluación posterior mediante Impacto y Naturalidad sigue vigente, pero **no sustituye la lectura y el diseño previo**.

## Contrato obligatorio para nuevas pruebas

1. **Expectativa antes del texto:** para cada intento, formular internamente qué espera descubrir o ver el espectador **después** de los tres segundos y qué contenido del futuro video podría cumplirlo. Si no hay una respuesta o continuación posible y significativa, descartar la combinación. No convertir la expectativa en explicación dentro del hook.
2. **Duración pronunciada:** escribir solo la frase de apertura, no un párrafo. Objetivo aproximado: **3 segundos de voz**. Estimar el tiempo en español contando las palabras y suponiendo inicialmente ~180 palabras/minuto (unas 3 palabras/segundo), ajustando si hay pausas, puntuación o palabras difíciles. Si se puede, verificar con una lectura o voz real; de otro modo marcar la cifra como **estimación**, no como medición exacta. Las 6–10 palabras son una orientación, no una cuota. Si las variables exigen una frase larga y no admiten una versión natural de ~3 s, descartar y registrar el motivo, no recortar hasta perder el sentido.
3. **Combinaciones aleatorias sin lista negra previa:** permitir combinaciones inusuales; probar si pueden cumplir naturalmente la intención, estructura, recurso, tono, emoción y expectativa. Si resultan semánticamente imposibles, forzadas o demasiado largas, descartarlas, conservar variables e indicar causa. No prohibir una combinación por un solo fallo.
4. **Registro:** cada hook aceptado debe conservar las siete variables (incluida la dimensión de valoración), sus categorías y origen, texto del hook, **`expectativa`** concreta y **`duracion_estimada_segundos`** numérica. Mantener vacías las columnas de calificación humana. Registrar los intentos rechazados por separado con variables y causa. No atribuir a las estimaciones ni al juicio de la IA resultados de audiencia.

La pregunta «¿qué espera descubrir?» guía la **generación previa**, no es un tercer criterio de evaluación. Los **únicos criterios finales** siguen siendo Impacto y Naturalidad.

**Cada variable elegida para un hook debe cumplirse de verdad en el contenido, no solo mencionarse o imitarse superficialmente.**

En particular, la **intención comunicativa debe ejecutarse como una acción con significado**, no como una palabra o un estilo de redacción.

- Si la intención es **disculparse**, el hablante debe reconocer un error, daño o responsabilidad propios y expresar una disculpa auténtica. Decir «perdón» o «discúlpame» antes de una afirmación no basta.
- Si la intención es **advertir**, debe comunicar un riesgo o consecuencia relevante.
- Si la estructura es **comparación**, deben aparecer elementos realmente comparables.
- Si el recurso es **isocolon**, debe haber miembros de estructura gramatical y longitud semejantes.
- Si el tono es **intrigante**, la formulación debe producir una incertidumbre significativa, no limitarse a usar una palabra misteriosa.

**Comprobación antes de aceptar el hook:** identificar en las palabras concretas dónde se realiza cada variable seleccionada. Si alguna no se cumple, reescribir o rechazar el candidato; no afirmar que cumplió la fórmula.

**Ejemplo fallido (intención: disculparse):** «Perdón, pero ¿por qué no vendes beats?». Aquí «perdón» funciona como muletilla.

**Ejemplo válido (intención: disculparse):** «Te dije que publicar más beats te conseguiría más clientes. Me equivoqué. Perdón por darte ese consejo sin entender a qué artistas estabas llegando».

Esta regla se aplica a todas las variables de `formula-hooks/` y no implica que la combinación elegida sea necesariamente buena para captar atención.

## Selección aleatoria y evaluación: solo dos criterios

**No prohibir combinaciones por adelantado porque parezcan raras.** Primero seleccionar y producir un candidato sin forzar ni simular las variables. Evaluar el resultado mediante **solo dos criterios**:

1. **Impacto:** ¿el hook tiene potencial de captar la atención del espectador y suscitar la emoción elegida? Se evalúa el efecto hipotético, no se afirma rendimiento real.
2. **Naturalidad:** ¿suena como algo que una persona diría, tiene sentido en el contexto y cumple **semánticamente** todas las variables seleccionadas sin muletillas ni artificios? La coherencia está incluida aquí; no crear un tercer criterio llamado «coherencia».

**Ambos deben aprobar.** Si falla cualquiera, descartar el hook e indicar por qué. No rescatar un candidato fallido solo porque sea gracioso, extraño o formalmente cumpla la lista; tampoco forzar una combinación imposible. Registrar intentos, combinaciones descartadas y causas para detectar patrones. Un fallo aislado **no** convierte esa combinación en prohibida; solo considerar restricciones tras observar fallos repetidos con evidencia suficiente.

Ejemplo de fallo: **ira + académico + sarcasmo** puede producir una frase divertida, pero si no suscita ira ni interesa al espectador, **falla Impacto** aunque satisfaga el estilo. Las palabras «perdón» o «lo siento» sin una disculpa verdadera **fallan Naturalidad/cumplimiento semántico**.
