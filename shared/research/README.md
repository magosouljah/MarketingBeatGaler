# Research — contrato compartido

`reference.schema.json` define cómo documentar **una referencia ya investigada**. Un enlace recibido sin análisis se registra primero en el `INBOX.md` de su cuenta.

Campos esenciales: plataforma, URL, creador, visualizaciones, baseline habitual del creador (si verificable), ratio de outlier (si existe baseline), transcripción, frames, hook, formato, cuenta destino y fundamento de la clasificación.

El ratio solo se calcula cuando ambos datos existen: `video_views / creator_baseline_views`. Si no hay suficientes datos, dejar baseline/ratio como `null`, y `classification: "reference"`.

Tomar el baseline de la **mediana de videos comparables recientes**, documentando tamaño de muestra, método, fecha y fuente. El número de muestras y el umbral de outlier **no** están fijados aún: se calibrarán con investigación real en Fase 1.

Preferir datos públicos/autorizados y enlaces verificados. No inventar métricas ni automatizar scraping universal para poder avanzar.

