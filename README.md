# MarketingBeatGaler

Sistema de research y producción de videos verticales para **BeatGaler**. Documentos de autoridad: [PLAN.md](PLAN.md) y [FASE-0.md](FASE-0.md). **Fase 0: aprobada. Fase 1: Research System, en preparación.**

## Dirección y aprendizaje

- **[DIRECCION.md](DIRECCION.md)** — archivo rector **protegido**: solo se modifica con autorización explícita del propietario.
- [learning/README.md](learning/README.md) — comandos y ciclo reproducible de evaluación → propuesta → nueva prueba → regla validada.
- [AGENTS.md](AGENTS.md) — instrucciones obligatorias para agentes de programación.
- [learning/cases/](learning/cases/) — evidencia de pruebas; [learning/proposals/](learning/proposals/) — ideas todavía no validadas; [learning/lessons/](learning/lessons/) — aprendizajes comprobados.

Inicio rápido: `python learning/engine.py status`. El motor inicial registra y valida mejoras con pruebas; **todavía no crea ni evalúa MP4 automáticamente**.

## Estructura

- [shared/](shared/) — infraestructura técnica y contrato de referencias reutilizables, sin mezclar el gusto de las cuentas.
- [account-1/](account-1/) — cuenta oficial de BeatGaler: anuncios, producto, UI y posicionamiento premium.
- [account-2/](account-2/) — cuenta de contenido para productores: consejos, recursos y contenido nativo útil.

## Cómo añadir videos de referencia

1. Enviar los enlaces en el chat, indicando si corresponden a la cuenta 1 o 2 (si no se sabe, clasificar después).
2. Registrar el enlace original sin inventar métricas en [account-1/research/INBOX.md](account-1/research/INBOX.md) o [account-2/research/INBOX.md](account-2/research/INBOX.md).
3. Investigar transcripción, escenas, hook, formato, creador y métricas verificables. Mover el análisis estructurado a `REFERENCES.json` usando [shared/research/reference.schema.json](shared/research/reference.schema.json).
4. Actualizar la Hook Library y Format Library de **esa cuenta** solo con patrones sustentados en referencias reales.

Un video interesante **no** es necesariamente un outlier. Solo clasificarlo como outlier cuando exista una comparación razonable con el rendimiento habitual del mismo creador.

## Estado

La infraestructura audiovisual de scraping, transcripción, generación de scripts, edición y render aún no está implementada; las carpetas reservadas no significan funcionalidad terminada. El **Learning Engine V1** sí dispone de una CLI y pruebas locales. No iniciar producción masiva hasta pasar los gates de [PLAN.md](PLAN.md).

## Reference Analysis V1

Executable full-frame source preparation, technical reports, optional annotated 2D kinematics and Learning Engine integration: [execution guide](shared/reference_analysis/README.md), [skill](skills/reference-analysis/SKILL.md), [research](shared/reference_analysis/RESEARCH.md). The original Apple Music MP4 is still unavailable in this checkout; the committed demonstration is synthetic. New tests: `python -m unittest discover -s shared/reference_analysis/tests -v`. A [pre-existing protected hash mismatch](shared/reference_analysis/AUDIT-BLOCKER.md) blocks the existing audit; it is not bypassed.
