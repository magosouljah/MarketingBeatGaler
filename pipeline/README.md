# Pipeline V1.3 — seis módulos

Convierte lo que sabemos del productor musical en videos, mide qué pasa y devuelve lo aprendido. Todo son archivos de texto y CSV unidos por identificadores; no hay base de datos ni servicios.

```
1 Investigación → 2 Razonamiento → 3 Hipótesis, selección y guiones → 4 Producción → 5 Medición → 6 Aprendizaje
        ↑______________________________ preguntas nuevas ______________________________________|
```

| Módulo | Carpeta | Entra | Sale | Identificador |
| --- | --- | --- | --- | --- |
| 1. Investigación | [`1-investigacion/`](1-investigacion/) | Fuentes, testimonios, referencias, resultados propios | Evidencia etiquetada y cola de preguntas abiertas | `EV-0001`, `Q-001` |
| 2. Razonamiento | [`2-razonamiento/`](2-razonamiento/) | Evidencia y preguntas | Un árbol de porqués por mecanismo | `M-001`, `N-001-01` |
| 3. Hipótesis, selección y guiones | [`3-hipotesis-guiones/`](3-hipotesis-guiones/) | Árboles | Predicciones comprobables, guiones y experimentos de contraste | `H-001`, `G-001`, `X-001` |
| 4. Producción | [`4-produccion/`](4-produccion/) | Guiones aprobados | Piezas listas para publicar | `P-0001` |
| 5. Medición | [`5-medicion/`](5-medicion/) | Números leídos a mano de cada plataforma | Una fila por pieza, plataforma y lectura | usa `P-…` |
| 6. Aprendizaje | [`6-aprendizaje/`](6-aprendizaje/) | Predicción y resultados | Informe de ocho preguntas; preguntas nuevas para el módulo 1 | `A-001` |

La cadena completa de una pieza: `P → G → H → N → M → EV`. Con eso cualquier número se puede seguir hasta la evidencia que motivó el video.

## Órdenes

```bash
python pipeline/pipeline.py comprobar        # todos los identificadores enlazan
python pipeline/pipeline.py estado           # qué hay en cada módulo
python pipeline/pipeline.py arbol M-001      # árbol de un mecanismo y cuántas hojas están ancladas
python pipeline/pipeline.py aprender <X-activo>   # genera borrador solo de experimento no descartado
python -m unittest discover -s pipeline/pruebas -v
# Ideación V1.3: primero explorar y profundizar SIN historial; revisión en OTRO contexto
python pipeline/ideacion.py comprobar inputs/ideacion-01.json
python pipeline/ideacion.py revisar inputs/ideacion-01.json
```

## Hooks — sistema de aprendizaje creativo (2026-11-23)

Para ideas y frases iniciales de videos usar [`hooks/SKILL.md`](hooks/SKILL.md), con Mapa de Deseos, principios, técnicas y criterio. La vieja [`formula-hooks/`](formula-hooks/README.md) es ahora una **biblioteca/experimento histórico opcional**: no obliga a elegir emoción ni seguir `M → V + E → C + X`. La crítica del propietario actualiza la **forma activa de generar**, no solo un archivo de ejemplos. Ver [aprendizaje de hooks](hooks/APRENDIZAJE.md).

Esto no sustituye los seis módulos de investigación a publicación ni convierte un juicio creativo en medición de audiencia.

## Guiones — biblioteca creativa experimental (V0)

Para desarrollar guiones con ideas y enseñanzas del propietario, consultar [`scripts/SKILL.md`](scripts/SKILL.md), sus principios, técnicas y criterio. El [aprendizaje de guiones](scripts/APRENDIZAJE.md) modifica el conocimiento activo tras feedback humano. Complementa el módulo 3 y no reemplaza sus registros, aprobaciones ni medición. Las variantes de una misma idea son una posibilidad de exploración, no una cuota ni calendario aprobados.

## Guion gráfico — tercer sistema creativo (V0)

Después de hooks y scripts, usar [`storyboard/SKILL.md`](storyboard/SKILL.md) para decidir estructura audiovisual, acción en pantalla, locución, montaje, sonido y transiciones. Su conocimiento activo evoluciona con feedback mediante [`storyboard/APRENDIZAJE.md`](storyboard/APRENDIZAJE.md), sin fórmula obligatoria. El guion gráfico se entrega antes de producción; el Learning Engine sigue validando ejecución. El [lote 01 de 27 guiones](../content/scripts/LOTE-01-27-GUIONES.md) tiene nueve cuerpos invariables, tres aperturas por cuerpo. Diferenciar el efecto del texto del hook del tratamiento audiovisual completo.

## Generación creativa V1.3

El generador lee [EXPLORACION-V13](1-investigacion/EXPLORACION-V13.md), razona con el [módulo 2](2-razonamiento/README.md) y usa [GENERAR-V13](3-hipotesis-guiones/GENERAR-V13.md). Explora sin cuotas de cantidad o territorio y profundiza **solo** ideas con una consecuencia importante y una explicación de por qué el estímulo puede captar atención. Puede seleccionar **cero, uno, dos o tres** finalistas, incluso de un mismo territorio. Si ninguno merece desarrollarse, lo justifica y no escribe guiones.

Guardar un lote JSON en `inputs/`. `python pipeline/ideacion.py comprobar` valida estructura, evidencia y causalidad **declarada**, no calidad. Un revisor en otro contexto usa [REVISAR-V13](evaluacion/REVISAR-V13.md) y el historial reservado. Rechaza trivialidad o explicaciones superficiales antes de revisar diversidad. Solo las ideas sobrevivientes pasan a guiones sin aprobar.

`ideacion.py` **no genera ideas ni asegura originalidad o rendimiento**: esas tareas requieren un agente y revisión humana. Las pruebas sintéticas comprueban el contrato técnico; falta validación creativa con productores y datos de publicación.

## Dos aprendizajes que no se mezclan

- **Audiencia:** vive aquí, en `6-aprendizaje/`. Solo los datos de publicación cambian el estado de una hipótesis.
- **Producción:** sigue en [`learning/`](../learning/) (casos, lecciones, evaluación de 7 criterios). Depende de la aprobación visual del propietario.

Una pieza marcada como mal ejecutada en `4-produccion/piezas.csv` no cuenta ni a favor ni en contra de su hipótesis.

## Estado de cada módulo (2026-11-21)

| Módulo | Qué funciona | Qué falta |
| --- | --- | --- |
| 1 | 17 evidencias documentadas con su solidez; 7 preguntas abiertas | Fuentes modernas de atención y validación de las ramas conceptuales del Mapa |
| 2 | Un árbol real (Autoexamen) con sus cinco ramas; 3 de 11 hojas ancladas | Regla de cuándo un árbol está listo para producir; más mecanismos |
| 3 | Una hipótesis y dos guiones históricos descartados | Primer lote V1.3 con selección fundada y revisión independiente |
| 4 | Registro de piezas y plantilla de arranques: los dos arranques del experimento X-001 ya se renderizan | Unirlos al cuerpo (falta el MP4 de add-finder y el segundo de corte); voz; más tipos de arranque |
| 5 | Formato de registro manual y validación | Ninguna lectura real; integraciones |
| 6 | Borrador numérico del informe, con avisos de comparaciones dudosas | Ningún informe real; la interpretación siempre se escribe a mano |

El circuito completo está comprobado solo con los datos inventados de [`pruebas/circuito/`](pruebas/circuito/), marcados como `PRUEBA` en cada identificador y aislados de los datos reales.

**Integración V1.3 (2026-11-22):** módulos 1–3 simplificados; G-001/G-002, X-001 y P-0001/P-0002 descartados, preservados como historial. El flujo requiere relevancia y consecuencia concreta antes del guion, sin automatizar su calidad. La medición incorpora `visitas_web` opcional y el aprendizaje separa guion, ejecución y distribución. Faltan pruebas ejecutadas y datos reales de audiencia.

`DIRECCION.md` no se ha modificado y sigue describiendo la dirección anterior.
