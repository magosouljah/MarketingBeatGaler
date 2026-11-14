# Referencia Apple Music — Análisis temporal de portadas 3D

**Estado:** evidencia recuperada, dirección documentada, reconstrucción **NO aprobada creativamente**. Este documento corresponde solo al movimiento de las portadas, no al anuncio completo.

## Fuente y alcance

- Referencia original proporcionada por el usuario: `-5258203640291409657(1).mp4`, 181 fotogramas H.264 a **30 fps**, **512×910**, duración **6.033 s**.
- Fuente pública indicada: https://www.instagram.com/p/DcBoH7XgD1V/
- Se inspeccionó la secuencia completa; se hizo una exploración temporal en saltos de 0.20–0.25 s, ampliaciones de 0.10–0.20 s en cambios rápidos y análisis numérico fotograma por fotograma de la ocupación cromática.
- La fuente tiene fondo prácticamente uniforme **RGB (244,244,244)**. **No** incluir la marca Apple, locución, texto promocional o CTA de la referencia en nuestro resultado.
- Ventana útil de portadas ~**1.20–4.55 s**; el resto (0–1.2 / 4.55–6.03 s) corresponde a marca y CTA, fuera de alcance. La salida aislada debe empezar en la entrada de las portadas.
- No guardar el MP4 original ni sus capturas en el repositorio público por derechos de terceros. Guardar el análisis, URLs, código y datos derivados; comparativas locales de QA se entregan en la conversación.

## Observaciones directas — lo que **sí** muestran los píxeles

| Tiempo del original | Movimiento observado |
|---|---|
| 1.20–1.34 | Primera aparición compacta de un pequeño abanico de superficies cuadradas inclinadas. Aún **no** existe un anillo estable. |
| 1.35–1.62 | Expansión rápida en forma de abanico/guirnalda; llegan múltiples portadas con diferentes orientaciones y solapamientos. Centro abierto. |
| 1.65–2.20 | Arcos superior/inferior visibles alrededor del área central; **gran desigualdad** de tamaño aparente y giro: algunas portadas se ven como líneas finas, otras muestran toda la cara. El lado derecho concentra portadas grandes. |
| 2.20–2.95 | Giro continuo y cambio de cuáles portadas ocupan cada posición. El grupo aumenta ligeramente su presencia en el encuadre, sin una cadencia idéntica de tamaño/rotación para todos los elementos. |
| 3.00–3.45 | Expansión/aproximación pronunciada: muchas portadas salen parcialmente por los límites; la composición deja de poder leerse como una figura completa. |
| 3.48–3.80 | Ruptura del arco, barrido de elementos en primer plano; se produce un notable cambio de escala y oclusión. |
| 3.80–4.30 | Un paquete de superficies grandes, superpuestas y con escorzo fuerte, barre la parte derecha del plano; aparecen otras muy cerca de cámara en partes del encuadre. |
| 4.30–4.55 | Las últimas portadas salen del plano; el original revela contenido tipográfico que **no** forma parte de este encargo. |

### Medición no semántica sobre los 181 fotogramas

Se detectaron píxeles de saturación alta (HSV: S>70, V>45). Es un **proxy de ocupación visual**, no un detector de tarjetas ni una medición del movimiento de cámara. Píxeles en portadas grises o negras no entran en la cuenta. Ejemplos:

| t fuente | píxeles cromáticos | caja de percentiles 1–99%, X/Y |
|---|---:|---|
| 1.30 | 28,363 | X 123–467; Y 273–453 |
| 1.50 | 41,691 | X 59–453; Y 226–526 |
| 2.00 | 54,855 | X 29–508; Y 170–565 |
| 2.60 | 53,013 | X 8–510; Y 163–559 |
| 3.00 | 61,784 | X 6–509; Y 156–578 |
| 3.40 | 65,431 | X 5–507; Y 26–600 |
| 3.80 | 120,151 | X 49–502; Y 145–686 |
| 4.20 | 128,290 | X 97–501; Y 144–733 |
| 4.60 | 10 | La mayoría ha salido |

La comparación debe priorizar la **evolución** de la forma, el volumen de primer plano, la orientación y los tiempos; no igualar colores o arte original.

## Hipótesis de reconstrucción — no observables directamente

A partir de un video plano no se puede determinar de manera única la distancia focal, el camino de cámara, la coordenada Z de una cubierta ni el software original. Tampoco hay evidencia suficiente para afirmar que sea un toro geométrico perfecto o que cada portada siga una circunferencia.

### Propuesta de puesta en escena, ajustable tras comparativa

- Sistema derecho X, arriba Y, hacia cámara Z. 24 *image planes* con cara frontal auténtica, grosor fino y z-buffer.
- Formar primero un **abanico asimétrico**, después una cinta de portadas que recorre un campo ovalado y finalmente un **barrido de primer plano**. No un círculo cerrado en todo momento.
- Malla individual: `position(x,y,z)`, `rotation(x,y,z)`, escala y opacidad derivadas exclusivamente de t. Las diferencias de orientación y profundidad producen arcos de tarjetas casi de perfil y un lado de tarjetas frontales grandes.
- Cámara de perspectiva (hipótesis inicial: FOV vertical **48°**) con objetivo por encima del centro del formato, dolly suave y aceleración en el tramo de primer plano. El FOV exacto no se puede recuperar del original.
- Cada portada recibe desfasajes de entrada, fase y rotación pequeños y **deterministas**; el barrido final utiliza destinos y velocidades por elemento, **no** una rotación global reciclada.
- Timing local (t local = t fuente − 1.20):
  - **0.00–0.55:** salida desde abanico y despliegue con ease-out.
  - **0.55–2.25:** arco deformado, giro moderado y acercamiento progresivo.
  - **2.25–2.65:** aceleración hacia la transición y entrada de cubiertas de primer plano.
  - **2.65–3.30:** composición de paquetes solapados y salida de campo.
- Preservar **fondo blanco roto**, textura de portadas sin iluminación exagerada, sin brillos falsos ni sombras dramáticas. La fuente es editorial/limpia, no una escena espacial oscura.
- Toda variable debe poder evaluarse en tiempo arbitrario (HyperFrames `hf-seek`), sin depender de wall-clock, timers o frames anteriores.

## Evaluación de herramientas

- **HyperFrames**: motor inicial/garantía de render determinista, 30 fps, MP4 H.264 vertical; contrato `hf-seek`. https://github.com/heygen-com/hyperframes ; https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes-animation/adapters/three.md
- **WebGL2 propio (ya validado)**: reutilizar solo shaders, geometría de planos, carga de 24 texturas, z-buffer, soporte `hf-seek`, no su coreografía anterior. Evita nuevas dependencias en esta iteración. Three.js sería valioso con mallas complejas/quaternions/curvas, pero no hace la dirección automáticamente. https://threejs.org/docs/pages/Quaternion.html
- **GSAP**: útil para construir un timeline editable con easings controlados y `seek()`. Para esta escena trigonométrica por card, la evaluación directa por t es más fácil de comprobar y reproducir; no introducir GSAP solo para adorno. https://gsap.com/docs/v3/GSAP/Timeline/seek%28%29/
- **Blender tracking**: buena alternativa para *reprojection* si se etiquetan manualmente portadas, pero un solve de cámara tradicional es ambiguo cuando los objetos se mueven independientemente y no hay suficientes marcadores rígidos. https://docs.blender.org/manual/en/latest/movie_clip/tracking/
- **Referencias/skills HyperFrames**: `hyperframes-core`, `hyperframes-animation`, `hyperframes-keyframes`, `hyperframes-cli`; sin prometer que la skill automatiza gusto visual.

## Gate visual / aceptación

Comparar **al menos 0.15 / 0.40 / 0.70 / 1.05 / 1.40 / 1.80 / 2.10 / 2.40 / 2.70 / 2.95 / 3.20 s** de la animación con los tiempos de fuente equivalentes +1.20 s, mismo ratio 9:16 y misma altura. Revisar además en reproducción continua y a 0.5×:

1. Apertura en abanico (NO anillo instantáneo).
2. Izquierda casi de perfil / derecha con superficies amplias, sin repeticiones equidistantes.
3. Profundidad/oclusiones creíbles; ningún salto de tarjeta al entrar en el barrido.
4. Expansión, velocidad y timing relativo creíbles.
5. Barrido final diagonal con capas, sin quedar elementos aislados estáticos.
6. Calidad H.264 y ausencia de parpadeos de texturas.

**La primera comparación geométrica local todavía evidenció una forma demasiado ovalada y un barrido final demasiado regular. No se declara conformidad visual.** Las versiones anteriores siguen rechazadas.

## Restricciones

Únicamente `account-1/creative-assets/` del repositorio de marketing. Las 24 imágenes auténticas ya disponibles en la rama experimental se mantienen sin edición. El vídeo comparativo del material Apple no se sube al GitHub público. No producción, no aplicación, no guion, no otras escenas. Verificar derechos publicitarios de las portadas antes de publicación.