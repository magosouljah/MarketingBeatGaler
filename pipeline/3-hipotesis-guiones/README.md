# 3. Hipótesis, selección y guiones — V1.2

**Responsabilidad:** explorar ideas genuinamente diferentes, explicar sus mecanismos, elegir tres y redactar borradores. **No** confundir aprobación creativa con validación de audiencia.

| | |
| --- | --- |
| Entra | Evidencia y preguntas del módulo 1; explicaciones causales del módulo 2; objetivo y cuenta |
| Sale | Lote exploratorio, tres finalistas, guiones no aprobados y, cuando proceda, hipótesis/experimentos trazables |

**Orden obligatorio:** [GENERAR-V12.md](GENERAR-V12.md) → comprobación mecánica → [revisión separada](../evaluacion/REVISAR-V12.md) → guiones. El generador **no lee** evaluaciones, guiones anteriores, preferencias archivadas ni `referencias-historicas.json` antes de guardar el lote inicial.

1. Explorar **15–20 situaciones**, no 15–20 frases del mismo problema. Diversificar por contexto, protagonista, deseo, consecuencia y forma narrativa; cubrir al menos cinco territorios del productor.
2. Antes de escribir hooks, formular en cada candidato: situación, deseo, estímulo perceptible, por qué podría captar atención, cómo se paga la promesa y grado de presencia comercial de BeatGaler (`ninguna/discreta/indirecta/directa`). `apoyo` distingue evidencia `EV-…` de `supuesto`.
3. Elegir tres finalistas de territorios distintos. Guardar un lote JSON y ejecutar `python pipeline/ideacion.py comprobar <lote.json>`. La comprobación **no certifica creatividad**.
4. En otro contexto, el revisor lee historial y ejecuta `python pipeline/ideacion.py revisar <lote.json>`; identifica repeticiones conceptuales, promesas infundadas y conexiones forzadas **sin dar al generador las frases históricas**.
5. Para las tres ideas que superen revisión, **crear o reutilizar mecanismos reales en el módulo 2** (cinco ramas obligatorias y nodos con evidencia o pregunta abierta); no asignar M-001 por conveniencia. Después registrar hipótesis `H-…` con nodos existentes, y redactar guiones distintos sin aprobación. El propietario decide cuáles aprobar para producción; cualquier efecto sobre la audiencia se descubre después de publicar.

**No imponer:** emoción intensa, contradicción, fórmula de hook, mención de BeatGaler o publicidad directa. Curiosidad, demostración, enseñanza, placer y otras rutas son válidas si se argumenta su efecto. Las técnicas populares de retención son posibilidades, no verdades empíricas.

## Contratos que permanecen

- **Hipótesis:** `hipotesis.csv` conserva `prediccion`, `refutacion`, `nodos` y `seleccion`; estados `propuesta`, `reforzada`, `debilitada`. Nunca «demostrada».
- **Guiones:** `guiones.csv` más archivo en `guiones/`; arranque, desarrollo que cumple la promesa, cierre y pendientes. `aprobado_por_propietario=no` hasta aprobación explícita.
- **Contraste:** `experimentos.csv` mantiene qué cambia y qué se mantiene si se quiere probar causalidad.
- Los históricos G-001/G-002 y X-001 permanecen **descartados**, no como inspiración ni como material para producir.
- Evidencia de rendimiento comparable > fundamentos investigados > gustos personales para **inferir eficacia**. La decisión estética del propietario sigue mandando en **qué se produce**. No generar un archivo exhaustivo de sus gustos.

**Límite:** no existe algoritmo que certifique que un guion es original o eficaz. `ideacion.py` solo detecta errores estructurales y algunas semejanzas literales; la revisión humana evalúa el significado.
