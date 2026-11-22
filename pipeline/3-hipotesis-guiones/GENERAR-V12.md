# Generador V1.2 — solo contexto nuevo

**Objetivo:** crear situaciones nuevas antes de escribir hooks. Es una instrucción para un agente de IA, no un generador autónomo basado en plantillas.

## Fuentes permitidas para esta fase

Leer `AGENTS.md`, `DIRECCION.md` (solo lectura), `PLAN.md`, `FASE-0.md`, `pipeline/1-investigacion/EXPLORACION-V12.md`, el Mapa V3, del módulo 1 **priorizar los nuevos EV-0012–EV-0017** y sus fuentes; del módulo 2 leer **el protocolo causal, no los árboles históricos**. La evidencia histórica anterior puede contener slogans previos: no usarla como fuente creativa. **No leer** `pipeline/evaluacion/`, `pipeline/3-hipotesis-guiones/guiones/`, `guiones.csv`, los ejemplos históricos, rechazos o guiones anteriores. Los ejemplos reservados solo los usa un **revisor en otro contexto**, tras guardar el lote.

## Generación: orden obligatorio

1. Fijar cuenta (1 publicidad premium o 2 contenido de valor), objetivo (alcance, interés, visitas web) y amplitud comercial (desde ninguna hasta anuncio). No construir todavía escenas ni mencionar por defecto funciones del producto.
2. Explorar por cuenta propia **15–20 situaciones distintas** extraídas de varios territorios del productor (mínimo cinco). Mezclar actores, contextos, tensiones, resultados, maneras de captar interés y consecuencias. Un cambio de emoción o de redacción **no** convierte el mismo incidente en otra situación.
3. Para cada situación, preguntar «¿por qué?» en múltiples direcciones: deseo, vulnerabilidad, contexto, efecto posible del estímulo, objeciones y alternativas. Distinguir evidencia verificable de supuestos. Una idea puede interesar por utilidad, humor, demostración, expectativa o emoción: ninguna ruta es obligatoria.
4. Escribir **solo el lote de situaciones**, todavía sin hooks redactados. Elegir tres finalistas de **territorios diferentes**, explicando por qué y cuál es la mayor incertidumbre.
5. Guardar JSON local (por ejemplo `inputs/ideacion-01.json`) con el contrato siguiente y ejecutar `python pipeline/ideacion.py comprobar inputs/ideacion-01.json`. Corregir los problemas estructurales antes de continuar.
6. **DETENERSE** y entregar el lote al revisor independiente. No abrir ni invocar `revisar` en este mismo contexto. Solo después de esa revisión, redactar tres guiones y marcar su estado **sin aprobación**. Ningún guion va a producción sin el dueño.

## Contrato de un lote (JSON)

```json
{
  "version": "1.2",
  "cuenta": "1",
  "candidatos": [
    {
      "id": "I-01",
      "territorio": "contexto amplio",
      "nucleo": "descripción corta del conflicto, sin hook",
      "situacion": "hecho específico, protagonista y momento",
      "deseo": "qué está en juego",
      "estimulo": "qué se vería u oiría, sin eslogan",
      "por_que": "hipótesis causal y su límite",
      "pago": "qué entrega realmente el desarrollo",
      "apoyo": "supuesto",
      "presencia": "discreta"
    }
  ],
  "finalistas": ["I-01", "I-02", "I-03"]
}
```

El ejemplo describe el **esquema**, no un lote válido: son obligatorios 15–20 candidatos, cinco territorios y tres finalistas distintos. `apoyo` admite `supuesto` o identificadores `EV-0001` separados por espacios. `presencia`: `ninguna`, `discreta`, `indirecta`, `directa`.

**Nunca usar la validación automática para afirmar que las ideas son buenas, psicológicamente probadas o distintas en significado**: solo detecta problemas mecánicos.

## Prompt mínimo para el agente generador

> CONTINUAR · MEDIA · MarketingBeatGaler · rol GENERADOR V1.2. Lee únicamente las fuentes permitidas de `GENERAR-V12.md`. Investiga varias ramas del Mapa V3; produce 15–20 situaciones realmente diferentes, sin redactar hooks ni leer históricos. Razonar en varias direcciones cada porqué. Selecciona tres finalistas de territorios diferentes. Guarda el lote JSON en `inputs/`, ejecuta `pipeline/ideacion.py comprobar`, entrega los IDs y detente antes de revisión histórica.
