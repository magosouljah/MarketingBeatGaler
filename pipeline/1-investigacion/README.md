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
