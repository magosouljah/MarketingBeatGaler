# Regla — cumplimiento real de cada variable

## Paso 0 — Lectura obligatoria ANTES de generar

**Leer íntegramente este archivo y las bibliotecas de `formula-hooks/` antes de seleccionar ninguna variable o escribir un hook.** Respetar el proceso y sus dependencias. No inventar variables ni empezar usando instrucciones parciales recordadas.

## Fórmula y orden obligatorio

`M → (V + E) → (C + X) → Hook`

1. **M — Emoción.** Elegir primero una de las 10 emociones/estados permitidos. Puede escogerse aleatoriamente, dejando constancia de la elección.
2. **V + E — Valoración y espectador.** Elegir una dimensión/grupo de Scherer y un rasgo específico del Mapa V3 —experiencia, creencia, deseo, miedo, identidad o valor— **a partir de la emoción ya seleccionada**. Razonar por qué la interpretación del rasgo podría activar esa emoción. No sortear E y V independientemente si eso hace que la conexión resulte arbitraria.
3. **C + X — Concepto y expresión.** Construir un concepto que materialice esa reacción; **dentro de esta misma etapa**, seleccionar sucesivamente intención, estructura, recurso retórico y tono, buscando la forma de comunicar el concepto que más intensifique la emoción y la expectativa. Cada elección respeta las anteriores. No exigir combinaciones lingüísticas arbitrarias que hagan artificial el resultado.

**Expectativa = razonamiento, no variable adicional.** Tras conectar M, V y E, definir qué acontecimiento, explicación, revelación o resultado importante podría esperar el espectador **después** de oír el hook. Utilizar esa expectativa para crear C + X sin revelarla por completo.

**Objetivo prioritario:** provocar **la mayor intensidad posible de la emoción seleccionada** y **la expectativa más fuerte posible** de lo que sigue en el video. Se permite exagerar, dramatizar y provocar, siempre que la promesa pueda satisfacerse y no se presenten como hechos falsedades, cifras inventadas ni capacidades inexistentes.

**Formato:** solo la apertura verbal de aproximadamente **3 segundos**, no un párrafo, explicación ni guion completo.

## Contrato obligatorio para nuevas pruebas

1. **Expectativa antes del texto:** después de elegir M y conectar V + E, y **antes de redactar C + X**, formular internamente qué espera descubrir o ver el espectador **después** de los tres segundos y qué contenido del futuro video podría cumplirlo. No es parte de la fórmula. Si no hay continuación posible y significativa, volver a razonar V + E o descartar el candidato. No explicar ni resolver la expectativa dentro del hook.
2. **Duración pronunciada:** escribir solo la frase de apertura, no un párrafo. Objetivo aproximado: **3 segundos de voz**. Estimar el tiempo en español contando las palabras y suponiendo inicialmente ~180 palabras/minuto (unas 3 palabras/segundo), ajustando si hay pausas, puntuación o palabras difíciles. Si se puede, verificar con una lectura o voz real; de otro modo marcar la cifra como **estimación**, no como medición exacta. Las 6–10 palabras son una orientación, no una cuota. Si las variables exigen una frase larga y no admiten una versión natural de ~3 s, descartar y registrar el motivo, no recortar hasta perder el sentido.
3. **Selección ordenada, no sorteo independiente:** permitir decisiones inusuales cuando tengan una razón psicológica o expresiva. Tras seleccionar M, escoger V + E por su capacidad de suscitarla; construir C y seleccionar sucesivamente I, S, R y T para maximizar emoción y expectativa. Si una elección resulta imposible, artificial o demasiado larga, reconsiderar esa elección o descartar el candidato y registrar la causa. No crear listas negras por un solo fracaso.
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

## Evaluación final: solo dos criterios

**No prohibir combinaciones por adelantado porque parezcan raras.** Completar primero la fórmula **en orden**, eligiendo cada componente en función de los anteriores y sin forzarlos; después evaluar el hook mediante **solo dos criterios**:

1. **Impacto:** ¿el hook tiene potencial de despertar **la emoción elegida con la mayor intensidad posible** y abrir **una expectativa muy fuerte** de lo siguiente? Se evalúa el efecto hipotético, no se afirma rendimiento real.
2. **Naturalidad:** ¿suena como algo que una persona diría, tiene sentido en el contexto y cumple **semánticamente** todas las variables seleccionadas sin muletillas ni artificios? La coherencia está incluida aquí; no crear un tercer criterio llamado «coherencia».

**Ambos deben aprobar.** Si falla cualquiera, revisar las decisiones previas o descartar el hook e indicar por qué. No rescatar un candidato fallido solo porque sea gracioso, extraño o formalmente cumpla la lista; tampoco forzar una combinación imposible. Registrar intentos, decisiones descartadas y causas para detectar patrones. Un fallo aislado **no** convierte esa elección en prohibida.

Ejemplo de fallo: **ira + académico + sarcasmo** puede producir una frase divertida, pero si no suscita ira ni interesa al espectador, **falla Impacto** aunque satisfaga el estilo. Las palabras «perdón» o «lo siento» sin una disculpa verdadera **fallan Naturalidad/cumplimiento semántico**.
