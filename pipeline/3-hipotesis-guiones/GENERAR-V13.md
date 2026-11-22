# Generador V1.3 — primero relevancia, después creatividad

**Objetivo:** descubrir propuestas que puedan importarle al productor y captar atención por una razón concreta. Ser diferente no basta; tampoco basta decir «miedo», «curiosidad» o «valor». El código verifica estructura, **no calidad psicológica**.

## Fuentes del generador (sin contaminación)

Leer `DIRECCION.md` (solo lectura), `AGENTS.md`, `PLAN.md`, `FASE-0.md`, `pipeline/1-investigacion/EXPLORACION-V13.md`, Mapa V3, evidencia relevante y `pipeline/2-razonamiento/README.md` (protocolo causal). **No leer** `pipeline/evaluacion/`, `pipeline/3-hipotesis-guiones/guiones/`, `guiones.csv` ni videos/guiones favoritos antes de cerrar el lote.

## Paso 1: exploración libre

Explorar tantas situaciones como aporten perspectivas reales; **sin mínimo/máximo ni cuota de territorios**. Investigar rutas diferentes cuando ayude, pero no inventar conflictos para cumplir una cifra. Cada idea inicial requiere solo:
- `id` (`I-01`...), `nucleo` (conflicto sin hook), `situacion` (quién, momento, hecho), `deseo` y `apoyo` (`EV-0000` o `supuesto`).
- `territorio` es opcional y nunca se usa como criterio de aprobación.
- Evitar empezar por una función de BeatGaler y fabricar un problema que la justifique.

## Paso 2: profundizar **solo las candidatas que lo merezcan**

Antes de seleccionar, contestar en un objeto de `profundizaciones`:
- `relevancia`: por qué este público concreto se identifica, desea o necesita algo.
- `consecuencia`: qué puede ganar, perder, decidir o comprender; por qué es importante **en su vida musical**.
- `estimulo`: qué vería u oiría que activa esa tensión/curiosidad/utilidad en el momento, no qué emoción se le pide recordar.
- `por_que`: **razonamiento causal**, no una etiqueta («miedo + urgencia» no explica nada); preguntar por qué en varias direcciones, explorar una explicación rival.
- `pago`: qué aporta el resto del video para cumplir la promesa y mantener el interés.
- `objecion`: por qué puede ser trivial, poco creíble, engañosa, no tener efecto o no poder demostrarse.
- `presencia`: `ninguna`, `discreta`, `indirecta` o `directa`. BeatGaler puede no aparecer; evitar conexiones forzadas, no atribuir capacidades no verificadas.

**Filtro editorial:** si no se puede explicar de forma específica por qué la consecuencia importa y por qué el estímulo puede captar atención, descartar la idea aunque sea distinta. No tratar toda emoción como objetivo obligatorio: también son válidos utilidad, curiosidad genuina, experiencia estética o juego si la respuesta tiene peso para la audiencia.

Seleccionar **de cero a tres finalistas** por fortaleza del razonamiento, sin exigir territorios diferentes. Si ninguno alcanza el estándar, usar `finalistas: []` y explicar en `sin_finalistas_por_que`; **no escribir guiones por obligación**.

## Paso 3: guardar, verificar, revisar, escribir

Guardar un JSON local en `inputs/ideacion-01.json`. Ejecutar `python pipeline/ideacion.py comprobar inputs/ideacion-01.json`. Esta verificación solo encuentra datos incompletos, referencias inexistentes y duplicados exactos.

**Detenerse** y enviar el lote a un revisor independiente (nuevo contexto) que lea `pipeline/evaluacion/REVISAR-V13.md` y compare historial. El generador no debe leer esa revisión mientras crea el primer lote.

Tras la revisión, **solo si sobreviven finalistas**, formalizar nuevos mecanismos y nodos (cinco ramas), registrar hipótesis/guiones sin aprobar, y ejecutar `python pipeline/pipeline.py comprobar`. Si no sobrevive ninguno, investigar o iterar: no producir un video mediocre.

### Contrato JSON (ejemplo parcial, no un lote aprobado)

```json
{
  "version": "1.3",
  "cuenta": "1",
  "candidatos": [
    {"id": "I-01", "nucleo": "descripción sin hook",
     "situacion": "protagonista, hecho y momento",
     "deseo": "qué quiere o protege", "apoyo": "supuesto"}
  ],
  "profundizaciones": [
    {"id": "I-01", "relevancia": "a quién le importa y por qué",
     "consecuencia": "qué está en juego", "estimulo": "hecho visible o audible",
     "por_que": "cómo podría captar atención y por qué",
     "pago": "qué entrega el desarrollo", "objecion": "motivo plausible de fallo",
     "presencia": "indirecta"}
  ],
  "finalistas": ["I-01"],
  "sin_finalistas_por_que": ""
}
```

Para descartar **todos**, `profundizaciones` puede ser `[]`, `finalistas` debe ser `[]` y `sin_finalistas_por_que` debe explicar la decisión.

### Prompt del generador

> CONTINUAR · MEDIA · MarketingBeatGaler · GENERADOR V1.3. Sigue GENERAR-V13.md. Investiga qué tiene consecuencias importantes para productores concretos, explora sin cuotas y profundiza solo ideas relevantes. Justifica causalmente la atención, considera objeciones y permite cero finalistas. Guarda lote JSON en inputs/, ejecuta ideacion.py comprobar y DETENTE. No leas historial, preferencias ni el material del revisor.
