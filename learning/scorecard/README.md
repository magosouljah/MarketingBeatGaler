# Evaluación de videos

Sistema para evaluar la **calidad técnica y artística del trabajo de la IA** en cada video. Lo responde el **propietario**. Es el mismo para todos los videos y ambas cuentas.

No evalúa la estrategia de marketing, el guion, el gancho ni las ideas del creador: solo la ejecución.

## Criterios (versión 3)

| Criterio | `id` | Peso | Qué mira |
| --- | --- | ---: | --- |
| Animación | `animation` | 20% | Fluidez, movimientos y transiciones |
| Estética | `aesthetics` | 20% | Estilo visual, colores y composición |
| Originalidad visual | `originality` | 15% | Creatividad y personalidad |
| Consistencia | `consistency` | 15% | Coherencia visual entre escenas |
| B-roll | `broll` | 10% | Calidad de las tomas de apoyo |
| Realismo | `realism` | 10% | Naturalidad y ausencia de errores visuales |
| Acabado profesional | `finish` | 10% | Nitidez, iluminación y detalles |

Los criterios, sus pesos y la escala viven en [`criteria.json`](criteria.json): para cambiarlos se edita ese archivo, no el código.

## Cómo se puntúa

- Cada criterio recibe de **0 a 5**, con decimales (`4.5`).
- Resultado final ponderado sobre **100**: `suma(peso × nota) ÷ suma(pesos que aplican) ÷ 5 × 100`.
- Si un criterio **no aplica** (por ejemplo, un video sin tomas de apoyo) se marca `na`: queda fuera y su peso se reparte en proporción entre los demás. Con B-roll fuera, Animación pasa de 20% a 22.2%.
- Cada criterio admite un comentario breve con el defecto y la mejora necesaria, más una nota general.
- Hay que dar los siete criterios, cada uno con número o `na`; no se asume nada.

| Nota | Significa |
| ---: | --- |
| 5 | No cambiaría nada |
| 4 | Muy bien, detalles menores |
| 3 | Pasa, pero algo molesta |
| 2 | Mal, hay que rehacerlo |
| 0 | No sirve |

## Comandos

```bash
python learning/scorecard/scorecard.py add <video> --account account-1 --version "final" \
    animation=4.5 aesthetics=4 originality=3.5 consistency=4 broll=na realism=4 finish=4.5 \
    --comment aesthetics="el bote dibujado se veía infantil" --comment finish="nube pixelada al inflarse" \
    --note "comentario general" --evidence "sesión y fecha de la respuesta"

python learning/scorecard/scorecard.py show            # última versión de cada video, lado a lado
python learning/scorecard/scorecard.py show <video>    # detalle: notas, pesos efectivos, comentarios y total
python learning/scorecard/scorecard.py compare <video> # todas las versiones de un video y cuánto cambió cada criterio
```

Cada video guarda todas sus versiones evaluadas en `evaluations/<video>.json`. Volver a registrar la misma `--version` la reemplaza; una versión nueva se añade.

## Reglas para el agente

- Las calificaciones son solo del propietario. Se transcriben tal cual; nunca se rellenan, estiman ni redondean.
- Se pide al cerrar el video, sobre la última versión entregada. Si el propietario quiere evaluar versiones intermedias, se registran con su `--version` para poder compararlas.
- Cualquier criterio en **3 o menos**: preguntar qué falló y registrarlo como caso en `learning/cases/` con su explicación textual. El número solo no es evidencia suficiente para una regla.
- Una calificación alta **no** promueve propuestas: la promoción sigue necesitando aprobación explícita (ver [`../README.md`](../README.md)).
- Antes de empezar un video nuevo, ejecutar `show` y atacar primero los criterios con peor nota.
- Los criterios pueden cambiar con permiso del propietario: subir `version` en `criteria.json` y **no reutilizar ni renombrar** los `id`, para que el historial siga siendo comparable.

## Historial del sistema

- **Versión 3 (2026-11-16, vigente):** siete criterios ponderados de 0 a 5 y total sobre 100, definidos por el propietario.
- **Versión 2 (retirada):** cuestionario de quince preguntas del 1 al 10. Solo se usó con add-finder (promedio 7.0); su registro sigue en [`scores/add-finder.json`](scores/add-finder.json) y sus preguntas en [`questions.json`](questions.json). No es comparable con la versión 3 y no se convierte.
- **Versión 1:** nunca se usó.
