# Diagnóstico final — Paso 3 de 3: experimento A/B/C

> **TEMPORAL:** resultado del tercer y último paso del diagnóstico de Formula Hooks. Conservar hasta que el propietario autorice eliminar esta carpeta. **Este informe no cambia la fórmula ni las reglas.**

## Datos y método

- Fuente original: [03-HOOKS-CIEGOS.csv](03-HOOKS-CIEGOS.csv) (sin calificaciones), [03-CLAVE.csv](03-CLAVE.csv) (clave revelada solo después de recibir las puntuaciones) y [03-CONTROL-EXPERIMENTO.md](03-CONTROL-EXPERIMENTO.md).
- [03-RESULTADOS-CRUZADOS.csv](03-RESULTADOS-CRUZADOS.csv): **30 puntuaciones originales proporcionadas por el propietario**, asociadas a situación, emoción y método, sin cambio del texto de los hooks.
- **A:** fórmula completa M → (V + E) → (C + X [intención, estructura, recurso, tono]).
- **B:** psicología (emoción + valoración + espectador + concepto), redacción sin técnicas retóricas obligatorias.
- **C:** situación y emoción objetivo, sin uso consciente de la fórmula.
- Las diez situaciones y emociones son idénticas entre A, B y C dentro del paso 3. Se utilizaron tres agentes separados con el mismo **modelo declarado** `claude-fable-5-2` y configuración por defecto sin valores numéricos expuestos.
- Los criterios humanos son **Impacto** y **Naturalidad**, ambos en escala ordinal 0–3. **Total /6** = suma descriptiva con igual peso, *no* métrica de eficacia real.

## Paso 3 — Resultado por método

| Método | N | Suma Impacto | Suma Naturalidad | Impacto medio /3 | Naturalidad media /3 | Total medio /6 | Ambos ≥2 | Ambos 3 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **A** | 10 | 18 | 12 | 1.80 | 1.20 | 3.00 | 5 | 1 |
| **B** | 10 | 18 | 17 | 1.80 | 1.70 | 3.50 | 5 | 3 |
| **C** | 10 | 14 | 8 | 1.40 | 0.80 | 2.20 | 2 | 1 |

**B obtuvo mayor suma media (3.50/6)**, empató con A en Impacto (1.80) y tuvo más Naturalidad (1.70 frente a 1.20). C tuvo 2.20/6, la menor media.

**Calificados 3/3:** H009 (A); H013, H015, H022 (B); H012 (C). No equivalen a retención ni a conversiones reales.

## Paso 3 — Parejas por situación

Cada celda: **ID · Impacto/Naturalidad**. La «victoria» por situación compara únicamente el total /6 y conserva empates.

| Situación | Emoción | A | B | C | Mayor total |
|---|---|---|---|---|---|
| S01 — Un artista acepta el precio de un beat y, justo antes de pagar, ofrece una fracción de lo acordado. | Ira | H025 · 3/1 | H003 · 2/2 | H021 · 1/0 | A=B |
| S02 — Herramientas de IA generan beats completos en segundos y el productor teme volverse reemplazable. | Miedo | H027 · 1/0 | H015 · 3/3 | H012 · 3/3 | B=C |
| S03 — Lleva semanas sin abrir el DAW y siente que se está quedando atrás mientras otros siguen publicando. | Ansiedad | H002 · 0/0 | H001 · 1/2 | H026 · 1/1 | B |
| S04 — Un beat que hizo en veinte minutos gusta más que otro en el que trabajó semanas. | Sorpresa | H019 · 2/2 | H029 · 2/2 | H028 · 2/0 | A=B |
| S05 — La mezcla que anoche sonaba perfecta suena mal a la mañana siguiente, sin haber cambiado nada. | Confusión | H016 · 2/2 | H020 · 1/1 | H014 · 2/0 | A |
| S06 — Recordar las madrugadas haciendo beats con amigos por pura diversión, antes de pensar en vender. | Nostalgia | H005 · 2/0 | H007 · 1/1 | H008 · 2/0 | A=B=C |
| S07 — Soñar con dejar el empleo y vivir únicamente de producir música. | Anhelo intenso | H030 · 3/2 | H018 · 1/0 | H004 · 1/2 | A |
| S08 — Un artista publica una canción hecha sobre su beat y el productor la escucha por primera vez. | Entusiasmo | H010 · 0/0 | H011 · 1/0 | H017 · 0/0 | B |
| S09 — Otro productor con menos experiencia consigue placements y él no entiende qué hace distinto. | Interés | H009 · 3/3 | H013 · 3/3 | H024 · 2/2 | A=B |
| S10 — Sigue retocando un beat sin saber si ya está terminado o si lo está empeorando. | Curiosidad | H006 · 2/2 | H022 · 3/3 | H023 · 0/0 | B |

**Ganadores por situación:** A=2, B=3, C=0, empates=5.

**Comparación directa de totales:** B contra A: B gana 4, A gana 2, empates 4. A contra C: A gana 6, C gana 2, empates 2. B contra C: B gana 6, C gana 1, empates 3.

## Comparación con el paso 2

| Método | Paso 2 Impacto | Paso 2 Naturalidad | Paso 2 total /6 | Paso 3 Impacto | Paso 3 Naturalidad | Paso 3 total /6 |
|---|---:|---:|---:|---:|---:|---:|
| A | 1.90 | 0.90 | 2.80 | 1.80 | 1.20 | 3.00 |
| B | 2.10 | 1.20 | 3.30 | 1.80 | 1.70 | 3.50 |
| C | 1.60 | 1.20 | 2.80 | 1.40 | 0.80 | 2.20 |

**Ambas rondas, 20 hooks por método (descriptivo; situaciones y condiciones difieren):**

| Método | Impacto medio /3 | Naturalidad media /3 | Total medio /6 | Ambos ≥2 | Ambos 3 |
|---|---:|---:|---:|---:|---:|
| A | 1.85 | 1.05 | 2.90 | 7/20 | 1/20 |
| B | 1.95 | 1.45 | 3.40 | 8/20 | 4/20 |
| C | 1.50 | 1.00 | 2.50 | 6/20 | 2/20 |

- **B supera a A por exactamente 0.50 puntos /6 de media en las dos rondas**; esto es consistente descriptivamente, pero **no demuestra** que la fórmula B sea causalmente mejor.
- En paso 2, B superó a A en 7/10 situaciones por total; en paso 3, B superó a A en 4, perdió 2 y empataron 4.
- La naturalidad de A aumenta de 0.90 a 1.20, pero B también aumenta de 1.20 a 1.70; no se puede atribuir al modelo, ya que cambiaron otras condiciones.
- En paso 3 C queda por detrás de A y B; en el paso 2 estuvo empatado con A en total medio. **No sostener que C siempre pierde.**

## Interpretación y límites

**Hallazgo principal:** la psicología sin retórica obligatoria (**B**) es el candidato de trabajo mejor respaldado **por estas dos evaluaciones subjetivas**, no una fórmula científicamente ganadora. Incluir la retórica obligatoria en A **no mostró una ventaja consistente** sobre B. La retórica puede ser útil opcionalmente; esta prueba no separa cuál subcomponente de X ayuda o estorba.

**A conserva posibilidades:** obtuvo un 3/3 y triunfos en situaciones concretas, como el deseo de vivir de la música y la mezcla que cambia de percepción. No concluir que toda retórica es perjudicial.

**Situaciones importan:** el escenario de la canción publicada (S08) resultó débil para los tres, mientras S09 (placements) elevó puntuaciones de A y B. Esto limita la atribución del resultado a una sola variable.

**Limitaciones:**
1. La evaluación viene de **una persona**; no hubo espectadores reales, tasas de retención, clics ni visitas a BeatGaler.
2. Hay **10 situaciones por ronda y método**, puntuaciones discretas ordinales y posible variabilidad del gusto; las medias son resúmenes, no pruebas estadísticas.
3. El **paso 2** generó A/B/C dentro de una misma sesión, sin independencia estricta. En el **paso 3** hubo agentes separados, pero el mismo modelo y estilo base.
4. En el paso 3, **B vio automáticamente AGENTS.md**, que menciona la estructura retórica de la fórmula; no abrió las bibliotecas expresivas, pero sí hubo una contaminación parcial de las instrucciones.
5. Las instrucciones de lectura se comprobaron mediante informes de los agentes, **no aislamiento técnico**. C sabía la situación y emoción objetivo, y por tanto no es creatividad libre absoluta.
6. **No se puede medir la aportación aislada de la valoración V**, ni de cada intención, estructura, recurso o tono: cambiaron grupos enteros de instrucciones.
7. No hay medición de duración con locución real, y algunas aperturas parecen exceder tres segundos; las duraciones de la clave son **estimaciones**.
8. Aunque los métodos usaron el mismo modelo dentro del paso 3, **no se controlaron todas las diferencias entre pasos 2 y 3** (situaciones, forma de generación, independencia). No atribuir cambios a mayor inteligencia del modelo.

## Decisión técnica recomendada (pendiente de aprobación)

- **No declarar la fórmula completa validada ni cambiar las reglas automáticamente.**
- Considerar **B como configuración experimental preferente para la siguiente prueba**: emoción → valoración + espectador → concepto → expresión libre, usando retórica cuando agregue valor, sin obligarla.
- Antes de consolidar una fórmula definitiva, probar hooks de B/A en videos reales y comparar retención inicial y continuidad del visionado; la evidencia actual solo mide el juicio del propietario.
- **Los tres pasos de diagnóstico están terminados.** La carpeta seguirá siendo temporal y solo se borrará con autorización del propietario.

## Referencias internas

- [Diagnóstico paso 1](01-DIAGNOSTICO-V3.md)
- [Resultados paso 2](02-RESULTADOS-Y-DIAGNOSTICO.md)
- [Control paso 3](03-CONTROL-EXPERIMENTO.md)
- [Clave paso 3](03-CLAVE.csv)
- [Hooks ciegos paso 3](03-HOOKS-CIEGOS.csv)
- [Puntuaciones cruzadas paso 3](03-RESULTADOS-CRUZADOS.csv)
