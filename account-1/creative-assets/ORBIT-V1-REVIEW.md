# BeatGaler · Órbita 3D · Control de calidad (2026-11-04)

**Estado: primera prueba reproducible COMPLETADA; aprobación creativa PENDIENTE. No continuar con el anuncio completo todavía.**

## Repositorio y rama
- Marketing: `magosouljah/MarketingBeatGaler`, rama `marketing/first-video-3d-orbit-v1`.
- App/source artwork: `magosouljah/BeatGaler`, rama `design/beatgaler-design-system-lab-v1` (NO tocar producción).
- Código principal: [orbit-v1/index.html](orbit-v1/index.html); la documentación, QA y comando de render están en [orbit-v1/README.md](orbit-v1/README.md).
- Se copiaron y verificaron por SHA idéntico los 24 archivos reales `cover-01.jpg` a `cover-20.jpg` y `cover-21.avif` a `cover-24.avif`. Proceden de Design Lab: **no se han verificado licencias para uso publicitario**.

## Validación técnica realizada
- Motor original solicitado: **HeyGen HyperFrames**. Investigadas la documentación, skills, CLI y adaptador de Three.js. La escena usa un renderer WebGL2 propio con coordenadas 3D y sincronización `hf-seek`, no un reemplazo de HyperFrames.
- Acción: [GitHub Actions: render HyperFrames aprobado técnicamente](https://github.com/magosouljah/MarketingBeatGaler/actions/runs/41811962889).
- Validación oficial: **HyperFrames lint: 0 errores, 0 warnings**; `check --json` completado; `render --quality draft` completado en GitHub Actions: 140 fotogramas, ~5.8 s, 24 fps, 720x1280, MP4 H.264 compatible con iPhone, ~2.1 MB.
- Otro render Playwright/FFmpeg [41811453148](https://github.com/magosouljah/MarketingBeatGaler/actions/runs/41811453148) comprobó explícitamente **WebGL2 disponible** con SwiftShader; este era solo diagnóstico de respaldo.
- Workflow conservado en `.github/workflows/orbit-v1-preview.yml`. Publica artefacto descargable `beatgaler-orbit-v1-iphone-preview` de cada ejecución (caduca a los 14 días).
- La ruta de tiempo es absoluta (sin `requestAnimationFrame` ni `performance.now()`) y las 24 imágenes son precargadas antes de declarar readiness.
- La aplicación web de BeatGaler, su producción y el guion aprobado **no fueron modificados**.

## Revisión visual de fotogramas
- Se inspeccionaron imágenes extraídas de los MP4 en 0.2, 0.8, 1.7, 2.8, 4.2 y 5.6 s.
- **No aprobado como pieza premium**: muchas portadas aún compiten por protagonismo; algunos momentos parecen un collage 3D, no una órbita cinematográfica coreografiada. La profundidad existe técnicamente, pero el movimiento y la composición no alcanzan aún el cuidado visual solicitado.
- Dos prototipos previos fueron rechazados por el usuario; el presente resultado es una prueba de pipeline y base técnica, **no** una afirmación de paridad con Apple Music.
- El MP4 original de Apple Music (y otros clips descritos en [referencias](../design-references/FIRST-VIDEO-REFERENCES.md)) **no está incluido en los repositorios**. Los enlaces/descripciones no permiten observar con precisión aceleraciones, rotaciones o tiempos de la referencia.

## Decisiones y siguiente paso
1. Mantener la escena única y el guion aprobado; no construir el resto del anuncio.
2. Si se obtiene el MP4 Apple Music original, seleccionar seis cortes temporales y registrar camera moves, easing, profundidad, encuadres, velocidad/rotación.
3. Rediseñar composición en vez de simplemente aumentar cantidad o velocidad de portadas: 1–3 protagonistas por momento, rutas 3D realmente diferenciadas, jerarquía, encuadre/oclusiones intencionales, ritmo de cámara y distancias focales.
4. Contrastar primero fotogramas y luego el **video renderizado en HyperFrames**, no solo que el código pase.
5. Aprobar creativamente por separado. No publicar assets publicitarios sin autorización de uso.

**Enlaces de fuentes:** [HyperFrames](https://github.com/heygen-com/hyperframes) · [HyperFrames CLI skill](https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes-cli/SKILL.md) · [Referencia Apple original documentada](../design-references/FIRST-VIDEO-REFERENCES.md).
