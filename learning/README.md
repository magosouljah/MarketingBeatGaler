# Learning Engine — BeatGaler Marketing

Control del sistema: [DIRECCION.md](../DIRECCION.md). Estado: **motor inicial operativo**, NO editor ni evaluador visual autónomo. Compatible con Python 3.10+ sin dependencias.

## Comandos (desde la raíz del repositorio)

```bash
python learning/engine.py audit
python learning/engine.py status
python learning/engine.py review orbit-initial-rejection
python -m unittest discover -s learning/tests -v
```

`review` crea un informe reproducible en `learning/reviews/` y propuestas en `learning/proposals/`. Las propuestas **no son conocimientos probados**. Se pueden editar las skills y probar otras versiones libremente, pero solo se asciende una propuesta a `learning/lessons/account-N/` cuando existe **otra** prueba con el mismo check en `pass`, que cite la propuesta en `validates_proposal` (una) o `validates_proposals` (lista, cuando una misma prueba aprobada verifica varias) y tenga `human_approved: true` con `approval_evidence` del propietario:

```bash
python learning/engine.py promote orbit-initial-rejection--orbit-depth nombre-de-la-nueva-prueba
```

## Para cada nueva iteración

1. El agente lee `DIRECCION.md`, `PLAN.md`, `FASE-0.md`, el brief, las referencias originales y las lecciones de la cuenta correspondiente.
2. Produce **una prueba pequeña** y conserva MP4, proyecto editable, logs y frames (o links verificables). Nunca afirmar que un video fue analizado si no existe el archivo.
3. Crea `learning/cases/<id>.json`, con checks `pass`/`fail`, evidencia específica y, para fallos, hipótesis, regla candidata y prueba de aceptación.
4. Ejecuta `review <id>` para generar una propuesta por fallo, implementa la corrección en una skill/código, y crea una **prueba nueva**, no modifica retroactivamente el caso rechazado.
5. Obtiene aprobación humana antes de afirmar calidad creativa profesional; entonces `promote` incorpora la nueva regla validada. Todo se versiona con Git.
6. En los próximos trabajos, el agente debe leer las reglas en `learning/lessons/<cuenta>/`. Las reglas de la cuenta 1 NO contaminan la cuenta 2.

## Cuestionario por video

Al cerrar cada video el propietario califica del 1 al 10 quince aspectos de la ejecución del agente (solo lo que el agente controla): [scorecard/README.md](scorecard/README.md). Sirve para comparar videos entre sí; no sustituye a los casos ni a la aprobación explícita.

## Protección y límites

- `DIRECCION.md` es el **único archivo con permiso especial**. Solo el propietario puede autorizar explícitamente editarlo. `.github/direccion.sha256` permite detectar modificaciones accidentales; `.github/CODEOWNERS` solicita revisión del propietario. Para forzar la aprobación en GitHub también debe habilitarse protección de rama / CODEOWNERS en Settings.
- Todas las demás instrucciones, código, casos, reviews y skills pueden evolucionar normalmente, con commits y pruebas. No se inventan métricas ni aprobaciones.
- `audit` comprueba formato, trazabilidad y la integridad del archivo rector; **no** verifica automáticamente la calidad artística del MP4.
- Primer ciclo completo: [add-finder](../account-1/videos/add-finder/) (2026-11-14). 11 casos, 22 lecciones validadas por la aprobación de la v5 y 3 propuestas a la espera de que el propietario confirme la última entrega (`cta-cursor-centered`, `instagram-safe-zones-measured`, `floating-covers-no-intersection`). Para promoverlas: crear un caso nuevo con esa confirmación como `approval_evidence` y ejecutar `promote`.
- [llama](../account-1/videos/llama/) (2026-11-12, registrado el 2026-11-16): video hecho fuera del repositorio y antes de add-finder. 5 casos, 3 propuestas sin aprobar (`live-insert-shortest-readable`, `speed-ramp-needs-frame-blending`, `partial-change-keeps-the-rest`) y ninguna lección: el propietario no aprobó de forma explícita ninguna versión final.
- La órbita 3D de portadas quedó archivada sin aprobar; sus dos propuestas siguen abiertas. `DIRECCION.md` aún la nombra como prioridad: cambiarlo requiere autorización explícita del propietario.
- HyperFrames es la elección según `FASE-0.md`; herramientas 3D complementarias requieren justificación, no sustitución silenciosa.

## Reference Analysis integration

The [Reference Analysis CLI](../shared/reference_analysis/README.md) validates full-frame evidence before `register`, then reuses this engine for cases/reviews. `failure` records diagnostics and generates existing-format proposals with use/avoid conditions. No parallel promotion mechanism or automatic owner approval. The [baseline audit incident](../shared/reference_analysis/AUDIT-BLOCKER.md) records its explicitly authorized repair and retains the initial failing evidence.
