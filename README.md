# MarketingBeatGaler

Sistema de research y producción de videos verticales para **BeatGaler**. Documentos de autoridad: [PLAN.md](PLAN.md) y [FASE-0.md](FASE-0.md). **Fase 0: aprobada. Fase 1: Research System, en preparación.**

## Videos

| Video | Cuenta | Estado |
| --- | --- | --- |
| [add-finder](account-1/videos/add-finder/) | 1 | Entregado 2026-11-14 (11.9 s, negro y blanco). v5 aprobada; última entrega pendiente de confirmar. **[Todo lo aprendido](account-1/videos/add-finder/LEARNINGS.md)** |
| [orbit](account-1/videos/orbit/) | 1 | Archivado, nunca aprobado |

## Mapa del repositorio

```
DIRECCION.md  PLAN.md  FASE-0.md  AGENTS.md     dirección (protegida), plan y reglas para agentes
account-1/                                      cuenta oficial de BeatGaler
  videos/<video>/                               un video por carpeta: BRIEF, LEARNINGS, HISTORY, project/, tools/
  creative-assets/covers/                       60 portadas (cover-002 … cover-061)
  creative-assets/audio/voice-samples/          pruebas de voz
  research/  hooks/  formats/  scripts/         referencias, hooks, formatos y briefs antiguos
account-2/                                      cuenta de contenido para productores
learning/                                       Learning Engine: cases/ → proposals/ → lessons/
shared/                                         utilidades técnicas comunes (HyperFrames, FFmpeg, audio, QA)
skillpack/  skills/                             skills externas fijadas y skill de análisis de referencias
```

## Dirección y aprendizaje

- **[DIRECCION.md](DIRECCION.md)** — archivo rector **protegido**: solo se modifica con autorización explícita del propietario.
- [learning/README.md](learning/README.md) — comandos y ciclo reproducible de evaluación → propuesta → nueva prueba → regla validada.
- [AGENTS.md](AGENTS.md) — instrucciones obligatorias para agentes de programación.
- [learning/cases/](learning/cases/) — evidencia de pruebas; [learning/proposals/](learning/proposals/) — ideas todavía no validadas; [learning/lessons/](learning/lessons/) — aprendizajes comprobados.

Inicio rápido: `python learning/engine.py status`. El motor registra y valida mejoras con pruebas; **no crea ni evalúa MP4 automáticamente**. Hoy: 22 lecciones validadas en la cuenta 1, todas de add-finder.

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

Ya existe un flujo de producción probado de punta a punta con un video: HyperFrames para la imagen, FFmpeg para el audio, medición de golpes y de palabras, copia de revisión con contador y guía de zonas seguras (ver [shared/](shared/README.md) y [add-finder](account-1/videos/add-finder/)). Siguen sin implementarse el scraping, la generación de scripts y cualquier evaluación automática de calidad. El **Learning Engine V1** dispone de CLI y pruebas locales. No iniciar producción masiva hasta pasar los gates de [PLAN.md](PLAN.md).

## Reference Analysis V1

Executable full-frame source preparation, technical reports, optional annotated 2D kinematics and Learning Engine integration: [execution guide](shared/reference_analysis/README.md), [skill](skills/reference-analysis/SKILL.md), [research](shared/reference_analysis/RESEARCH.md). The original Apple Music MP4 is still unavailable in this checkout; the committed demonstration is synthetic. New tests: `python -m unittest discover -s shared/reference_analysis/tests -v`. A [pre-existing protected hash mismatch](shared/reference_analysis/AUDIT-BLOCKER.md) was repaired with explicit owner authorization, preserving direction text and the integrity check.

### First real reference intake

The original 6.033s Apple Music cover-orbit video was recovered from the user's previous ChatGPT Library upload and independently measured (FFprobe and short seed-based OpenCV tracks). It is **not** stored in GitHub or this checkout. [Derived source analysis, data, limitations and next comparison](account-1/research/reference-analysis/apple-music-orbit-v1/ANALYSIS.md). This is unapproved research, not a reconstructed or validated cinematic result.

## Skills de motion graphics para Fase 2

[Motion Skills Library](skillpack/README.md): **57 skills catalogadas y fijadas por SHA** desde 7 repositorios de GitHub; **19 prioritarias para la primera prueba de motion design**. Instalador reproducible para Codex y Claude Code: `python skillpack/manager.py install --profile phase2 --agent both` desde el IDE local. Las fuentes externas se descargan en cada equipo y no están incluidas físicamente en el repositorio; `DIRECCION.md` continúa protegido.
