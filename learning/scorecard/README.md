# Cuestionario de calificación

Quince preguntas, del 1 al 10, que el **propietario** responde al cerrar cada video. Mide la ejecución del agente: en qué va bien, en qué falla y si mejora de un video al siguiente. Es el mismo cuestionario para todos los videos y ambas cuentas.

## Escala

| | |
| --- | --- |
| 10 | No cambiaría nada |
| 8 | Muy bien, detalles menores |
| 6 | Pasa, pero algo me molesta |
| 4 | Mal, hay que rehacerlo |
| 1 | No sirve |

Si un aspecto no aplica (por ejemplo, un video sin voz), se deja sin responder.

## Qué se califica

**Solo lo que el agente controla y puede mejorar.** Lo que aporta el propietario (idea, gancho, guion, CTA, voz, música, portadas) no se califica: una nota ahí no le dice al agente qué cambiar.

## Preguntas (versión 2)

**Ejecución del video**

1. **Ritmo** — ¿Ninguna parte se siente lenta ni atropellada?
2. **Sincronía** — ¿Imagen, música y voz caen juntas?
3. **Movimiento** — ¿Las animaciones se sienten naturales y con intención?
4. **Cámara y transiciones** — ¿Los cambios de escena fluyen, sin cortes raros?
5. **Texto** — ¿Las letras se leen bien y se ven bien?
6. **Claridad visual** — ¿Se entiende lo que pasa en pantalla a la primera?
7. **Acabado premium** — ¿Se ve caro y no de plantilla?
8. **Fidelidad al producto** — ¿Lo que sale se parece a BeatGaler de verdad?
9. **Formato en teléfono** — ¿Se ve bien en tu teléfono dentro de Instagram, sin cortes ni cosas tapadas?
10. **Montaje de audio** — ¿Efectos y entradas de voz y música están bien colocados? (no califica la voz ni el beat)

**Trabajar con el agente**

11. **Entendimiento** — ¿Capté lo que pedías sin que tuvieras que repetirlo?
12. **Eficiencia** — ¿Llegamos al resultado en pocas vueltas?
13. **Control de calidad** — ¿Te llegaron las versiones sin errores que yo debí ver antes?
14. **Criterio propio** — ¿Mis decisiones y propuestas sumaron, sin preguntar de más ni inventar de más?

**Global**

15. **Ejecución global** — Con lo que me diste (idea, guion, voz, música), ¿qué tan bien lo ejecuté?

Al final, un comentario libre opcional.

La versión 1 nunca se usó: incluía gancho, claridad del mensaje, CTA, audio y «¿lo publicarías?», que dependen de lo que entrega el propietario. Esos `id` quedan retirados.

## Reglas para el agente

- Se pide **una vez por video**, sobre la última versión entregada. No en cada iteración.
- Las calificaciones son solo del propietario. Se transcriben tal cual; nunca se rellenan, estiman ni redondean. Lo que no respondió queda vacío.
- Cualquier aspecto en **6 o menos**: preguntar qué falló y registrarlo como caso en `learning/cases/` con su explicación textual. El número solo no es evidencia suficiente para una regla.
- Una calificación alta **no** promueve propuestas: la promoción sigue necesitando aprobación explícita (ver [`../README.md`](../README.md)).
- Antes de empezar un video nuevo, ejecutar `show` y atacar primero los aspectos con peor nota.
- Toda pregunta nueva debe medir algo que el agente pueda cambiar.
- Las preguntas pueden cambiar con permiso del propietario: subir `version` en `questions.json` y **no reutilizar ni renombrar** los `id`, para que el historial siga siendo comparable.

## Comandos

```bash
python learning/scorecard/scorecard.py add <video> --account account-1 --version "final v2" \
    pacing=7 sync=9 motion=8 … --note "comentario" --evidence "sesión y fecha de la respuesta"
python learning/scorecard/scorecard.py show
```

Resultados en `scores/<video>.json`.
