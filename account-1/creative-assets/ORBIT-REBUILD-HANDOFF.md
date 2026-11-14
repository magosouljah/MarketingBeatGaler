# ORBIT — cierre de prototipos fallidos y handoff

Estado: **RECHAZADO VISUALMENTE**. No presentar las iteraciones V1/V2 como aprobadas ni reutilizar su coreografía como base. Se conserva el pipeline técnico HyperFrames, la escena web, la captura QA y las 24 portadas originales ya copiadas. No modificar producción ni guion.

## Qué se intentó
- Primera órbita: portadas dispersas, sensación de collage, cámara poco dirigida.
- Segunda órbita tras recibir el MP4 original de Apple Music: anillo simplificado, insuficiente fidelidad de movimiento y composición. El usuario confirmó que «nada que ver».
- El pipeline sí demostró que HyperFrames lint/check/render puede producir MP4 H.264 vertical y que WebGL2 funciona en GitHub Actions. Esto es **éxito técnico, fracaso creativo**.

## Referencia obligatoria
El usuario adjuntó en la conversación el video original de Apple Music: `-5258203640291409657(1).mp4`, ~6.03 s, 30 fps. **Este archivo NO está confirmado dentro de GitHub**: en la próxima sesión pedir acceso al adjunto o que se suba al repositorio antes de asegurar que puede analizarse. Nunca inferir trayectorias o cámara de descripciones, thumbnails o tres fotogramas.

## Nuevo proceso — no saltarse fases
1. Leer README.md, PLAN.md, FASE-0.md, shared/README.md, account-1/scripts/FIRST-VIDEO-V1.md, account-1/design-references/FIRST-VIDEO-REFERENCES.md y este handoff.
2. Abrir el MP4 original y examinarlo de principio a fin; extraer secuencia a 30 fps y seleccionar keyframes; estudiar cambios entre fotogramas (no solo imágenes fijas). Documentar timecodes y evidencia visible de posiciones, tamaño aparente, solapamiento, rotación, perspectiva, trayectorias, aceleraciones, centro vacío y movimientos de cámara. Distinguir observación de hipótesis; no afirmar reconstrucción 3D exacta de un video 2D.
3. Investigar skills relevantes: HyperFrames CLI/documentación y skills oficiales, Three.js, GSAP, camera rig/animación 3D, easing y motion design. Verificar licencias y compatibilidad. No asumir que una librería genera buena dirección automáticamente.
4. Antes de implementar, entregar un **desglose de dirección**: composición por tiempo, storyboard anotado, sistema de coordenadas y cámara, relaciones de profundidad, reglas de oclusión, movimientos individuales, velocidades/easing, criterios de similitud. Priorizar equivalencia del comportamiento de referencia, no copiar marca ni interfaz.
5. Construir **solo la órbita** en una escena web con portadas auténticas, render determinista en HyperFrames; no construir otras escenas ni cambiar el guion.
6. Renderizar MP4 iPhone, extraer frames correspondientes a los timecodes originales y preparar comparativa lado a lado. Revisar **el video en movimiento**, no solo lint. Corregir discrepancias y repetir. No declarar «premium» ni «parecido» sin evidencia visual.
7. Conservar código, documentación, resultados y decisiones en una rama de marketing. Pedir aprobación creativa explícita antes de avanzar.

## Criterios de rechazo automático
- Portadas girando como un círculo plano o un carrusel uniforme.
- Todas las portadas con una misma trayectoria o easing; movimientos arbitrarios sin correspondencia con la referencia.
- Cámara estática sin justificación visual, profundidad simulada solo mediante escalado, perspectiva u oclusiones incoherentes.
- Composición que parezca collage/PowerPoint, demasiados elementos compitiendo.
- No hay comparación temporal con el MP4 original.
- Afirmar aprobación por el mero hecho de que HyperFrames renderice.

## Restricciones
No tocar producción de `magosouljah/BeatGaler`. No cambiar guion aprobado. No producir anuncio completo. No borrar assets ni el pipeline útil. No fusionar la rama de prototipos fallidos a main como si fuera un diseño aprobado. Comprobar derechos de uso de portadas para publicidad antes de publicación.

## Rutas
- Código rechazado pero reproducible: `account-1/creative-assets/orbit-v1/`
- QA anterior: `account-1/creative-assets/ORBIT-V1-REVIEW.md`
- Workflow: `.github/workflows/orbit-v1-preview.yml`
- Rama: `marketing/first-video-3d-orbit-v1`
