# Learning Engine — BeatGaler Marketing

Control del sistema: [DIRECCION.md](../DIRECCION.md). Estado: **motor inicial operativo**, NO editor ni evaluador visual autónomo. Compatible con Python 3.10+ sin dependencias.

## Comandos (desde la raíz del repositorio)

```bash
python learning/engine.py audit
python learning/engine.py status
python learning/engine.py review orbit-initial-rejection
python -m unittest discover -s learning/tests -v
```

`review` crea un informe reproducible en `learning/reviews/` y propuestas en `learning/proposals/`. Las propuestas **no son conocimientos probados**. Se pueden editar las skills y probar otras versiones libremente, pero solo se asciende una propuesta a `learning/lessons/account-N/` cuando existe **otra** prueba con el mismo check en `pass`, `validates_proposal` y `human_approved: true` con `approval_evidence` del propietario:

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

## Protección y límites

- `DIRECCION.md` es el **único archivo con permiso especial**. Solo el propietario puede autorizar explícitamente editarlo. `.github/direccion.sha256` permite detectar modificaciones accidentales; `.github/CODEOWNERS` solicita revisión del propietario. Para forzar la aprobación en GitHub también debe habilitarse protección de rama / CODEOWNERS en Settings.
- Todas las demás instrucciones, código, casos, reviews y skills pueden evolucionar normalmente, con commits y pruebas. No se inventan métricas ni aprobaciones.
- `audit` comprueba formato, trazabilidad y la integridad del archivo rector; **no** verifica automáticamente la calidad artística del MP4.
- Próximo trabajo real: crear preview editable de órbita 3D de portadas, evaluar con frames y video, corregir y validar con el propietario. HyperFrames es la elección inicial según `FASE-0.md`; herramientas 3D complementarias requieren justificación, no sustitución silenciosa.
