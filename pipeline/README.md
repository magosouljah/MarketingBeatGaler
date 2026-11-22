# Pipeline V1.2 — seis módulos

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
python pipeline/pipeline.py aprender X-001   # parte numérica del informe; añade --escribir para guardar el borrador
python -m unittest discover -s pipeline/pruebas -v
# Ideación V1.2: primero generar lote sin historial, después revisar en OTRO contexto
python pipeline/ideacion.py comprobar inputs/ideacion-01.json
python pipeline/ideacion.py revisar inputs/ideacion-01.json
```

## Generación creativa V1.2

El generador comienza en [EXPLORACION-V12](1-investigacion/EXPLORACION-V12.md), razona con [módulo 2](2-razonamiento/README.md) y sigue [GENERAR-V12](3-hipotesis-guiones/GENERAR-V12.md). Explora **15–20 situaciones antes de redactar hooks**, escoge tres de territorios diferentes y guarda un JSON local en `inputs/`. El validador solo comprueba formato/diversidad declarada. Un revisor **en otro contexto** consulta [REVISAR-V12](evaluacion/REVISAR-V12.md) y el historial reservado para detectar repeticiones conceptuales. Las tres ideas seleccionadas pasan entonces a guiones sin aprobación para producir. El historial y los gustos no se exponen durante la generación.

**No es un generador autónomo por código:** el trabajo creativo lo hace un agente de IA siguiendo la guía; `ideacion.py` no escribe guiones, no mide originalidad semántica y no garantiza retención. Tres pruebas sintéticas automatizadas comprueban el contrato; faltan tres corridas creativas realmente ciegas con revisión humana.

## Dos aprendizajes que no se mezclan

- **Audiencia:** vive aquí, en `6-aprendizaje/`. Solo los datos de publicación cambian el estado de una hipótesis.
- **Producción:** sigue en [`learning/`](../learning/) (casos, lecciones, evaluación de 7 criterios). Depende de la aprobación visual del propietario.

Una pieza marcada como mal ejecutada en `4-produccion/piezas.csv` no cuenta ni a favor ni en contra de su hipótesis.

## Estado de cada módulo (2026-11-21)

| Módulo | Qué funciona | Qué falta |
| --- | --- | --- |
| 1 | 17 evidencias documentadas con su solidez; 7 preguntas abiertas | Fuentes modernas de atención y validación de las ramas conceptuales del Mapa |
| 2 | Un árbol real (Autoexamen) con sus cinco ramas; 3 de 11 hojas ancladas | Regla de cuándo un árbol está listo para producir; más mecanismos |
| 3 | Una hipótesis y dos guiones históricos descartados | Primer lote de situaciones V1.2 y guiones nuevos |
| 4 | Registro de piezas y plantilla de arranques: los dos arranques del experimento X-001 ya se renderizan | Unirlos al cuerpo (falta el MP4 de add-finder y el segundo de corte); voz; más tipos de arranque |
| 5 | Formato de registro manual y validación | Ninguna lectura real; integraciones |
| 6 | Borrador numérico del informe, con avisos de comparaciones dudosas | Ningún informe real; la interpretación siempre se escribe a mano |

El circuito completo está comprobado solo con los datos inventados de [`pruebas/circuito/`](pruebas/circuito/), marcados como `PRUEBA` en cada identificador y aislados de los datos reales.

**Integración 2026-11-22:** módulos 1–3 simplificados; G-001/G-002, X-001 y P-0001/P-0002 descartados, preservados como historial. El flujo requiere ficha causal breve antes del guion, sin automatizar su calidad. La medición incorpora `visitas_web` opcional y el aprendizaje separa guion, ejecución y distribución. Faltan pruebas ejecutadas y datos reales de audiencia.

`DIRECCION.md` no se ha modificado y sigue describiendo la dirección anterior.
