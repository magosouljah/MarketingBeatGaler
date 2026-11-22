# 1. Investigación

**Responsabilidad:** reunir lo que se sabe del productor y de la atención humana, diciendo siempre de dónde sale. No interpreta.

| | |
| --- | --- |
| Entra | Fuentes de [`research/`](../../research/), referencias de [`account-1/research/`](../../account-1/research/), testimonios del propietario, comentarios reales, resultados del módulo 5, preguntas del módulo 6 |
| Sale | `evidencia.csv` y `preguntas.csv` |

## `evidencia.csv`

`tipo`: `observacion` (algo visto y comprobable), `testimonio`, `fuente` (lo que afirma un texto), `resultado` (medido en una pieza nuestra).

`solidez` dice cuánto pesa: `propio_medido`, `observado`, `testimonio_unico`, `fuente_secundaria`, `documento_sin_fuentes`, `texto_historico`. Un texto histórico aporta un modelo, no una demostración.

Cada fila necesita `referencia` (ruta o enlace) y `contenido` en palabras propias. No se registra nada que no se haya leído o visto.

## `preguntas.csv`

La cola que mantiene viva la investigación. Toda hoja del árbol que termina en supuesto o en «no sabemos» apunta a una pregunta de aquí. `estado`: `abierta` o `respondida`; al responder se cita la evidencia nueva en `respuesta`.

## Investigación orientada a mecanismos (V1.1)

Investigar **sin escribir hooks ni decidir el guion**. Reunir observaciones que permitan al módulo 2 explicar una cadena causal: **persona → deseo/vulnerabilidad → situación → estímulo perceptible → posible reacción inmediata → atención sostenida → acción posterior**. No asumir que todos los productores comparten los mismos deseos o reaccionan igual.

### Preguntas guía (no formulario obligatorio)

Registrar solo lo que la fuente permita; la ausencia de métricas no bloquea ideas.

### Preguntas que debe alimentar la evidencia

1. **Deseo y contexto:** ¿qué intenta conseguir, evitar o proteger el productor? ¿En qué circunstancias aparece ese deseo? ¿Quiénes difieren?
2. **Situaciones y consecuencias:** ¿qué pérdidas, oportunidades, contradicciones, resultados o riesgos concretos describe o experimenta? ¿Cuál es su magnitud y frecuencia conocida?
3. **Estímulos observables:** ¿qué palabras, imágenes, hechos o demostraciones aparecen realmente en un video? Distinguir lo visto de la emoción que *suponemos* que causa.
4. **Atención y retención:** ¿hay métricas de primeros segundos, retención, reproducciones completas, envíos o visitas? Registrar denominadores, plataforma, periodo, fuente y comparabilidad cuando existan; no deducir causalidad de likes, vistas aisladas o comentarios.
5. **Conexión editorial:** ¿qué contenido valioso o capacidad de BeatGaler (V1/V2) se relaciona, directa o indirectamente? La investigación **no exige** que cada problema termine en una función ni que el video sea comercial.
6. **Alternativas y límites:** ¿qué otra explicación encaja, qué audiencia no reaccionaría y qué dato faltaría para distinguirlas?

### Disciplina de fuentes

- Mantener las categorías existentes de `evidencia.csv`: `tipo`, `solidez`, `origen`, `referencia`, `fecha` y `contenido`. **No cambiar esquema ni inventar filas.**
- Separar **lo dicho por un productor**, **lo observado en un video**, **lo afirmado por un autor** y **lo medido en publicaciones**. Una afirmación de Atkinson sobre atención, sugestión o deseo es una hipótesis histórica, no una prueba de que un hook funcione.
- Si el material ofrece solo una técnica de un creador («resultado primero», «no A ni B, sino C», «contradecir una creencia», «hay una forma mejor», «no funciona salvo que hagas X»), registrar que **el creador la propone**; no convertirla en eficacia demostrada sin datos.
- Documentar **ausencias de datos** en `preguntas.csv`. No rellenar lagunas con psicología genérica, intuiciones o estadísticas inventadas.
- Distinguir **respuesta emocional hipotética**, **retención real** y **visitas reales**. Son variables diferentes.
- Priorizar, para inferencias de rendimiento, resultados propios comparables y datos observables con contexto; usar investigación externa para generar hipótesis. Los gustos creativos del propietario ayudan a elegir qué producir, pero **no constituyen evidencia de audiencia** ni requieren un inventario exhaustivo.

### Entrega hacia el módulo 2

Para cada mecanismo investigado, entregar evidencia o preguntas abiertas sobre: **deseo específico, situación concreta, estímulo observable, reacción postulada, explicación alternativa, condiciones de fallo y resultados disponibles**. El módulo 2 interpreta estas piezas y pregunta «¿por qué?»; el módulo 1 no debe inventar el enlace causal.

**Entrega mínima:** una observación o fuente con referencia, una situación/estímulo concreto si consta, y las preguntas abiertas. La interpretación causal corresponde al módulo 2.

**Prioridades de investigación actuales:** fuentes modernas de atención y retención; observaciones reales de productores en situaciones concretas; resultados comparables de videos publicados; verificar las referencias aún no abiertas. No dar por respondidas Q-001–Q-007 ni revivir el hook rechazado «400 beats. Name ten.» por ser el único ejemplo histórico registrado.
