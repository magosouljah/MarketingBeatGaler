# Cuestionario de calificación

Quince preguntas, del 1 al 10, que el **propietario** responde al cerrar cada video. Sirve para ver en qué aspectos el agente va bien, en cuáles falla y si mejora de un video al siguiente. Es el mismo cuestionario para todos los videos y ambas cuentas.

## Escala

| | |
| --- | --- |
| 10 | No cambiaría nada |
| 8 | Muy bien, detalles menores |
| 6 | Pasa, pero algo me molesta |
| 4 | Mal, hay que rehacerlo |
| 1 | No sirve |

Si un aspecto no aplica (por ejemplo, un video sin voz), se deja sin responder.

## Preguntas (versión 1)

**El video**

1. **Gancho** — ¿Los primeros 2 segundos te hacen quedarte?
2. **Claridad** — ¿Se entiende qué es BeatGaler y qué hacer, incluso sin sonido?
3. **Ritmo** — ¿Ninguna parte se siente lenta ni atropellada?
4. **Sincronía** — ¿Imagen, música y voz caen juntas?
5. **Movimiento** — ¿Las animaciones se sienten naturales y con intención?
6. **Texto** — ¿Las letras se leen bien y se ven bien?
7. **Acabado premium** — ¿Se ve caro y no de plantilla?
8. **Fidelidad al producto** — ¿Lo que sale se parece a BeatGaler de verdad?
9. **Cierre y CTA** — ¿El final deja claro qué hacer y dan ganas de hacerlo?
10. **Audio** — ¿Voz, efectos y mezcla suenan bien?
11. **Formato en teléfono** — ¿Se ve bien en tu teléfono dentro de Instagram, sin cortes ni cosas tapadas?

**Trabajar con el agente**

12. **Entendimiento** — ¿Capté lo que pedías sin que tuvieras que repetirlo?
13. **Eficiencia** — ¿Llegamos al resultado en pocas vueltas?
14. **Criterio propio** — ¿Mis decisiones y propuestas sumaron, sin preguntar de más ni inventar de más?

**Global**

15. **Global** — ¿Lo publicarías tal cual?

Al final, un comentario libre opcional.

## Reglas para el agente

- Se pide **una vez por video**, sobre la última versión entregada. No en cada iteración.
- Las calificaciones son solo del propietario. Se transcriben tal cual; nunca se rellenan, estiman ni redondean. Lo que no respondió queda vacío.
- Cualquier aspecto en **6 o menos**: preguntar qué falló y registrarlo como caso en `learning/cases/` con su explicación textual. El número solo no es evidencia suficiente para una regla.
- Una calificación alta **no** promueve propuestas: la promoción sigue necesitando aprobación explícita (ver [`../README.md`](../README.md)).
- Antes de empezar un video nuevo, ejecutar `show` y atacar primero los aspectos con peor nota.
- Las preguntas pueden cambiar con permiso del propietario: subir `version` en `questions.json` y **no reutilizar ni renombrar** los `id`, para que el historial siga siendo comparable.

## Comandos

```bash
python learning/scorecard/scorecard.py add <video> --account account-1 --version "final v2" \
    hook=8 clarity=9 pacing=7 … --note "comentario" --evidence "sesión y fecha de la respuesta"
python learning/scorecard/scorecard.py show
```

Resultados en `scores/<video>.json`.
