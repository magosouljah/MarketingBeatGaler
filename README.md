# MarketingBeatGaler

Sistema de research y producción de videos verticales para **BeatGaler**. Documentos de autoridad: [PLAN.md](PLAN.md) y [FASE-0.md](FASE-0.md). **Fase 0: aprobada. Fase 1: Research System, en preparación.**

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

Esta estructura es un punto de partida documental: **todavía no implementa scraping, transcripción, generación de scripts, edición o render**. Esos sistemas se construirán en sus fases correspondientes. No iniciar producción masiva hasta pasar el gate de Research de [PLAN.md](PLAN.md).

