# Fase 0 — Especificación ejecutable del sistema de video

**Estado:** ✅ Gate de Fase 0 aprobado

Esta fase existe para cerrar los huecos reales del video de referencia antes de construir. Las decisiones de abajo separan explícitamente lo que viene del video, lo que fue verificado externamente y lo que queda para medirse durante la implementación.

---

## 1. Sistema web → video

### Hallazgo

La herramienta mencionada en la transcripción sí es **HyperFrames**, de HeyGen.

HyperFrames es un framework open source para crear video con **HTML, CSS y JavaScript** y renderizarlo a MP4. Está diseñado para trabajar con agentes de código y HeyGen documenta explícitamente compatibilidad con **Codex**, además de Claude Code, Cursor y otros agentes.

Requisitos documentados:

- Node.js 22+
- FFmpeg
- npm / npx
- un agente como Codex

Flujo documentado:

```text
brief / script / assets
↓
HTML + CSS + JS
↓
preview
↓
render
↓
MP4
```

HyperFrames ya tiene workflows especializados que encajan directamente con el sistema del video:

- `product-launch-video`
- `general-video`
- `motion-graphics`
- `talking-head-recut`
- `embedded-captions`
- `media-use` / transcription

Su documentación considera 30–90 s como un rango fuerte para varios de estos workflows y muestra ejemplos verticales 1080×1920, así que nuestros videos de 30–60 s / 9:16 entran directamente en el caso de uso.

### Decisión

**Usar HyperFrames como renderer inicial.**

No construir un renderer propio ni cambiar a Remotion solo para avanzar. Primero debemos demostrar que HyperFrames puede producir el estándar visual que buscamos.

Si falla el gate creativo posteriormente, entonces se reconsidera el renderer con evidencia.

### Fuente

- https://github.com/heygen-com/hyperframes
- https://help.heygen.com/en/articles/15001510-hyperframes-x-heygen
- https://github.com/heygen-com/hyperframes/blob/main/docs/prompting/overview.mdx

---

## 2. Corrección de la referencia `Prompt Motion`

La transcripción decía `promptmotion.com`, pero el sitio que coincide con la descripción del creador es:

**https://prompt-motion.com/**

Es una galería de motion graphics hechos con Claude que muestra los prompts / skills detrás de los ejemplos.

### Decisión

Usarlo como **fuente de referencias visuales y motion**, no como dependencia del pipeline.

Su función será ayudarnos a encontrar ejemplos que representen el estándar deseado y alimentar la etapa de Design del video.

---

## 3. Research de videos ganadores / outliers

El video no exige construir un scraper universal. La instrucción concreta es estudiar videos del nicho que hayan superado las views habituales de su propio canal y extraer sus **hooks y formatos**.

Por lo tanto, el sistema necesita datos confiables; no necesita fingir automatización cuando la plataforma no los ofrece de forma fiable.

### Contrato mínimo de una referencia

```text
platform
url
creator
video_views
creator_baseline_views   # cuando se pueda calcular de forma fiable
outlier_ratio            # cuando exista baseline
transcript
screenshots / frames relevantes
hook
format
account_target           # account-1 | account-2
```

### Regla de honestidad

Una referencia solo se marcará como **outlier** cuando tengamos suficientes datos para compararla con el rendimiento habitual del mismo creador.

Si solo sabemos que es un video bueno o popular, entra como **reference**, no como outlier.

### Cómo operacionalizar “usual views”

El video no define una fórmula matemática. Para convertir la idea en algo medible, en Fase 1 calcularemos un baseline robusto usando la mediana de videos recientes comparables del mismo creador y guardaremos:

```text
outlier_ratio = video_views / baseline_views
```

La cantidad exacta de videos usada para el baseline y cualquier threshold de “ganador” **no quedan congelados en Fase 0**. Se calibrarán en Fase 1 con datos reales para no inventar un número arbitrario.

### Fuentes confirmadas

#### YouTube / Shorts

YouTube Data API expone públicamente `viewCount`, fechas, duración y videos de un canal. Aquí sí podemos automatizar de forma limpia la comparación con el rendimiento normal del canal.

#### TikTok

TikTok Display API expone metadata y `view_count` para videos accesibles mediante sus permisos. Para tendencias generales, TikTok Creative Center permite descubrir contenido y hashtags que están funcionando.

El acceso amplio de investigación a datos de terceros mediante TikTok Research Tools requiere aprobación como investigador y no debe asumirse como parte de nuestro producto.

### Decisión

Fase 1 soportará primero:

```text
URLs / referencias verificadas
+
metadata pública o autorizada disponible
+
transcripción
+
frames
↓
Hook Library + Format Library
```

No bloquear el proyecto intentando construir primero un scraper universal de TikTok / Reels.

### Fuentes

- https://developers.google.com/youtube/data/reference/rest/v3/videos
- https://developers.tiktok.com/doc/display-api-overview/
- https://developers.tiktok.com/doc/tiktok-api-v2-video-object/
- https://ads.tiktok.com/creative/creativeCenter/trends
- https://developers.tiktok.com/doc/research-api-overview/

---

## 4. Implementación del enfoque de seis trabajos en Codex

El video dice que el salto de calidad ocurrió al dejar de pedir un video completo en one-shot y separar el trabajo en seis jobs:

1. scripting
2. editing
3. design
4. motion graphics
5. review
6. feedback

Conservamos exactamente esa separación conceptual.

OpenAI documenta Skills como carpetas con un `SKILL.md` más recursos/scripts opcionales, y Codex puede usar trabajo multiagente con contextos independientes.

### Arquitectura decidida

```text
orchestrator
│
├── scripting skill
├── editing skill
├── design skill
├── motion graphics
│   └── HyperFrames skills + builders/subagents
├── review skill
└── feedback skill
```

El **orchestrator** mantiene el orden. No se intenta hacer todo en un prompt.

### Research

Research alimenta la Skill de scripting con Hook Library + Format Library. No se convierte artificialmente en un séptimo job creativo, porque en el video aparece como preparación del scripting.

### Skills

Cada skill debe ser estrecha. No crear un `VIDEO_MASTER_SKILL.md` gigante.

Ejemplo conceptual:

```text
skills/
  scripting/
    SKILL.md
  editing/
    SKILL.md
  design/
    SKILL.md
  review/
    SKILL.md
  feedback/
    SKILL.md
```

Motion graphics usará primero las Skills oficiales de HyperFrames en lugar de duplicarlas localmente.

### Subagentes

La paralelización se introduce donde la usa explícitamente el creador: **después de que exista el beat map / storyboard**, dividiendo secciones independientes del video entre builders.

```text
approved storyboard
      ↓
section A → builder A
section B → builder B
section C → builder C
      ↓
assemble
```

Los pasos dependientes —script → beat map → design approval— siguen siendo secuenciales.

### Fuentes

- https://developers.openai.com/plugins/concepts/skills
- https://developers.openai.com/api/docs/guides/agents-api/multi-agent
- https://openai.com/codex/

---

## 5. Model routing

El creador usa modelos más fuertes / caros para pensar y tomar decisiones creativas, y modelos más rápidos / baratos para construir.

Conservamos **el principio**, pero no copiamos nombres de modelos ni fijamos routing todavía.

```text
creative direction / planning
        ↓
strong reasoning role

implementation / rendering work
        ↓
builder role
```

### Decisión

No es un blocker de arquitectura. La selección concreta de modelos se mide después de tener un primer caso reproducible, comparando calidad / coste / velocidad.

---

## 6. Transcripción, captions y sincronización

La transcripción del video describe Whisper con timestamps por palabra. HyperFrames ya tiene soporte documentado para transcripción local y word-level timings, incluyendo workflows que usan Whisper / WhisperX y normalizan los timestamps.

### Decisión

No crear desde cero un formato incompatible.

La capa Editing debe producir / convertir la transcripción al formato que HyperFrames pueda consumir para:

- captions palabra por palabra;
- overlays sincronizados;
- beat timing;
- QA posterior.

Fuente:

- https://github.com/heygen-com/hyperframes/blob/main/skills/embedded-captions/SKILL.md
- https://github.com/heygen-com/hyperframes/blob/main/docs/packages/cli.mdx

---

## 7. Separación de las dos cuentas

El motor técnico se comparte. El gusto y la memoria creativa no.

```text
shared/
  transcription
  editing mechanics
  ffmpeg
  hyperframes
  rendering
  technical QA
  product-source-assets/

account-1/
  research/
  hooks/
  formats/
  scripts/
  design-references/
  design-guidelines/
  feedback/
  creative-assets/

account-2/
  research/
  hooks/
  formats/
  scripts/
  design-references/
  design-guidelines/
  feedback/
  creative-assets/
```

### Cuenta 1 — BitGaler oficial

Objetivo:

- vender;
- posicionar BitGaler.

Sensación:

- premium;
- limpia;
- minimalista;
- moderna;
- intencional;
- cara / profesional.

### Cuenta 2 — productor / contenido

Objetivo:

- atraer productores dando valor;
- convertir una parte de esa audiencia hacia BitGaler / Telegram.

Sensación:

- rápida;
- útil;
- humana;
- nativa de TikTok / Reels;
- primero contenido que vale la pena seguir, después integración natural de BitGaler.

### Regla común

**Nada de comedia absurda.**

El feedback creativo de una cuenta no modifica automáticamente las reglas de la otra.

---

## 8. Feedback = archivos versionados, no “memoria mágica”

El video dice que después de cada ronda Claude identifica qué instrucción habría prevenido el error y reescribe esa instrucción.

Nuestra implementación debe hacer lo mismo de forma auditable.

```text
human note
↓
classify mistake
↓
identify instruction that should have prevented it
↓
patch account-specific rule / skill
↓
fix current video
↓
commit change
```

Así podemos saber **qué aprendió el sistema, cuándo y por qué**.

No se confiará en una conversación larga como única memoria del editor.

---

## 9. Lo que todavía NO decidimos

Estas cosas no bloquean el inicio de Fase 1 y sería prematuro congelarlas ahora:

- threshold exacto para declarar un video “outlier”;
- cantidad exacta de videos para calcular baseline;
- modelo concreto para creative direction vs builders;
- número óptimo de builders concurrentes para nuestra máquina;
- reglas creativas finales de cada cuenta;
- catálogo final de assets reutilizables.

El video da `4` renders simultáneos como la solución del creador después de saturar su máquina con `9`. Conservaremos **4 como límite inicial de seguridad cuando lleguemos al render paralelo**, pero lo mediremos en nuestro entorno antes de tratarlo como óptimo.

---

# Gate de Fase 0

## 0.1 Renderer / web → video

✅ **RESUELTO** — HyperFrames.

## 0.2 Fuente de referencias / outliers

✅ **RESUELTO A NIVEL DE ARQUITECTURA** — references verificadas + metadata fiable; automatización por plataforma donde exista fuente limpia; no scraper universal como prerequisite.

## 0.3 Skills y subagentes en Codex

✅ **RESUELTO** — seis jobs separados; Skills estrechas; orchestrator secuencial; builders paralelos en motion después del storyboard.

## 0.4 Separación de cuentas

✅ **RESUELTO** — engine compartido; research, scripting, design, feedback y creative assets separados.

## Resultado

**FASE 0 = PASS**

Podemos entrar a Fase 1 sin elegir herramientas por inercia ni construir piezas que ya resuelve el stack seleccionado.

---

# Siguiente fase

## Fase 1 — Research System

Primer objetivo práctico:

1. crear el esquema real de `account-1` y `account-2`;
2. definir el formato de una referencia;
3. conseguir un primer conjunto pequeño de referencias por cuenta;
4. extraer hooks + formatos;
5. construir las primeras Hook / Format Libraries;
6. probar si el análisis distingue realmente un patrón útil de una descripción superficial.

No avanzar a generación masiva de scripts hasta pasar ese gate.