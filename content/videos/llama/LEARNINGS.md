# llama — todo lo que aprendimos

Lo aprendido haciendo este video el 2026-11-12, escrito el 2026-11-16 a partir de la sesión completa y del código que quedó.

**Qué valor tiene cada cosa.** Nada de esto es una lección validada: el propietario no aprobó de forma explícita ninguna versión con el chico. Hay:

- **3 propuestas** en `learning/proposals/llama-*`, cada una nacida de un feedback textual. Marcadas con ⏳.
- **Observaciones del agente**, sin feedback detrás. Sirven de punto de partida, no de regla.
- Varias reglas que add-finder validó dos días después ya asomaban aquí; se señalan con su `id`.

Las reglas creativas son de la **cuenta 1**. Las secciones 3 a 6 son técnicas y sirven para cualquier cuenta.

---

## 1. Estructura y ritmo

1. **La plantilla del reel de fuego tiene tres partes y cada una se ancla a algo que se oye.** Preparación sobre los pulsos del buildup, la acción clave dentro del silencio, y un corte por golpe después del drop. Lo que hizo que encajara fue asignar cada gesto a un evento concreto del audio: la llama prende cuando la música se calla (4.46 s), rocía en el golpecito previo (4.85 s) y el cuadro llega a blanco en el drop (5.12 s).
2. ⏳ **Un inserto de acción real dura lo justo para leer sus acciones** (`live-insert-shortest-readable`). El chico duraba 3.6 s y el propietario pidió «que dure un poco menos… para que sea un poco más entretenido». Quedó en 2.3 s para tres acciones (frustrarse, sacar las cosas, prender y rociar). Es la misma idea que `no-static-screen-over-two-seconds`, que add-finder validó después: un solo plano de más de ~2 s pesa, aunque dentro haya movimiento.
3. **Para acortar una escena se quita una vuelta de música, no se acelera todo.** El buildup extendido eran tres repeticiones de 1.307 s; quitar una acortó al chico 1.3 s sin mover ningún otro corte ni tocar la parte de BeatGaler. La unidad de recorte es el bucle, no el segundo.
4. **Los golpes no están en una rejilla.** Entre golpe y golpe de esta pista hay de 0.617 a 0.693 s. Cada corte va en su golpe medido (`beat-sync-measured-hits`). Ver sección 5.
5. **En el escritorio el remate es el buscador.** Los archivos entran en ráfagas de 8 por pulso (de 40 a 104) y la cámara tiembla cada vez más, pero lo que cuenta el chiste es «0 resultados» en 1.85 s. Sin eso es solo desorden.
6. **Cada toma cambia una cosa distinta respecto a la anterior.** Las doce tomas alternan perspectiva (isométrico, lateral, suelo, de frente), forma (tarjeta, tiras, círculo, rombos, abanico) y dirección de movimiento, y la entrada rota entre zoom, barrido en cuatro direcciones y giro, de modo que dos seguidas nunca entran igual. Es lo que el propietario pidió como «ve cambiando los cuadros (ósea las perspectivas y formas de la foto)».
7. **Observación sin feedback: el cierre es corto.** «Create ur Galer» está 1.08 s en pantalla y la pose final, de frente, 0.45 s. En add-finder el problema fue el contrario (3.2 s, «largo»). El punto bueno está en medio y aquí no se probó.

## 2. Imagen y producto

8. **De una captura de 1600 px se aprovechan las imágenes, no el texto.** Las portadas (134 px) aguantan ampliarse a 360 px con Lanczos y máscara de enfoque. El texto de 8 px no: nombres, tags y BPM se volvieron a escribir con Inter. El logotipo sí salió de la captura: recorte de 290×82, ×5 bicúbico, desenfoque σ 2.5 y un umbral suave, que deja un borde limpio a cualquier tamaño.
9. **Esto no es «componentes reales».** Las tarjetas se reconstruyeron a ojo desde una captura: los tags van todos en gris y la barra del reproductor es una aproximación. `real-product-ui-components` (validada después) pide leer el componente y su paleta. Aquí pasó porque nadie comparó con la app.
10. ⏳ **Un cambio parcial deja intacto lo demás** (`partial-change-keeps-the-rest`). Ante «que algunos sean como una imagen y otros como la otra», el agente convirtió **todos** los archivos a `.flp` y `.als` y borró los `.mp3` y `.wav`. Respuesta: «no remplaces todos deja unos mp3 y wav». La variedad ya era un valor del video (`file-type-variety`, validada después con la misma idea).
11. **Logos de FL Studio y Ableton solo como iconos de archivo.** Aparecen en el escritorio y en ningún sitio de la parte de BeatGaler. Coincide con `daw-logos-only-as-files`.
12. **El icono que mandó el propietario pesa más que el dibujado.** Los iconos genéricos del agente (hoja blanca con etiqueta de color) se leen como «archivos»; los del propietario se leen como «mis proyectos». Por eso pidió el cambio aunque nada estaba mal.

## 3. El clip de IA

Detalle y prompt completo en [`shared/ai-video/README.md`](../../../shared/ai-video/README.md).

13. **Un solo clip continuo con las acciones en orden funcionó a la primera.** El prompt describía un plano de selfie vertical, un adulto ficticio con rasgos concretos, cada gesto en secuencia, y terminaba pidiendo que el fuego llenara el cuadro. Seedance 2.5 respetó el orden y los tiempos relativos.
14. **El sujeto salió en el 45 % superior del cuadro.** La mitad de abajo era escritorio negro. Hubo que recortar a 360×640 y ampliar 3×, y por eso el chico se ve más blando que el resto. Para la próxima: pedir que cara y manos llenen el cuadro, o generar a 720p.
15. **Remapear el tiempo con puntos clave.** Una tabla «segundo del video → segundo del clip» e interpolación lineal: frustración a 2.7×, sacar las cosas a 1.9×, y los puntos que importan (llama, rociado, fuego lleno) clavados en sus eventos de audio.
16. ⏳ **Acelerar metraje exige mezclar cuadros, y no se corta a mitad de un gesto** (`speed-ramp-needs-frame-blending`). La v2 tomaba el cuadro más cercano de un clip de 24 fps a 2× y tenía un corte con zoom en plena frustración; además el archivo iba a 16 Mbps. El propietario: «creo que está como trabado». La v3 promedia los cuadros fuente que cubre cada cuadro de salida, quita el corte y baja a 8 Mbps. **Se cambiaron las tres cosas a la vez**, así que no se sabe cuál era; después no volvió a mencionarlo.
17. **El fuego del clip no basta para clavar el blanco.** Encima va un fuego procedural que empieza 0.10 s después del rociado y garantiza cuadro blanco exactamente en el drop, venga como venga el clip.
18. **Con el clip bloqueado, entregar con un suplente.** El resultado de Higgsfield no se podía descargar desde el entorno del agente. En vez de esperar, se entregó el video completo con una silueta dibujada; el propietario aprobó todo lo demás («perfecto ahora solo agrega al chico») y adjuntó el clip él mismo. `guy.py` usa la silueta sola si falta `inputs/guy.mp4`. La silueta era fea y se dijo: sirve para juzgar el montaje, no para publicarse.

## 4. El fuego

19. **Receta.** Tres octavas de ruido repetible que suben a velocidades distintas; una máscara radial que crece desde la posición del encendedor; y una tabla de color negro → rojo → naranja → amarillo → blanco. Se calcula a 270×480 y se amplía ×4: el fuego es blando y no se nota.
20. **La salida es un agujero que se abre desde el centro.** La misma función sirve para tapar (crece) y para revelar (se quema hacia afuera). El primer intento se abría en 0.6 s con desaceleración y a los 5 frames ya no quedaba fuego; quedó en 0.75 s con aceleración suave.
21. **Tropiezo: costuras rectas en el fuego.** Envolver las coordenadas con módulo antes de interpolar crea una línea donde se salta de 255 a 0. Se arregla dejando que `cv2.remap` envuelva (`BORDER_WRAP`).
22. **El viñeteado sobre blanco puro se ve gris en las esquinas.** En el frame del drop se nota. No se corrigió.

## 5. Audio: extender una pista corta

23. **Medir en la grabación real.** Envolvente de volumen suavizada a 4 ms y su derivada: el pico marca el golpe. Tiempos medidos en `tools/prepare.py` y `common.py`. Es el mismo principio que [`shared/editing/find_hits.py`](../../../shared/editing/find_hits.py), que todavía no existía; para lo siguiente, usar esa herramienta.
24. **Un bucle tiene que medir un número entero de pulsos.** Buildup: 4 pulsos = 1.307 s. Drop: 7 golpes = 4.564 s. Se corta 6 ms antes del golpe y se funde 5 ms.
25. **El agente no puede oír.** Las uniones se comprobaron mirando tiempos, no escuchando, y el detector rápido que se usó para verificar el montaje dio ruido. El propietario no se quejó del audio, pero nadie lo confirmó.
26. **La pista es de un reel ajeno.** Sirve para montar; al publicar va el audio desde Instagram o un beat propio, y entonces hay que volver a medir.

## 6. Python + OpenCV: cuándo sí y cuándo no

Detalle en [`shared/rendering/README.md`](../../../shared/rendering/README.md).

`FASE-0.md` elige HyperFrames. Este video no lo usó y la razón es concreta: necesitaba **metraje real remapeado, fuego por píxel y decenas de planos 3D con textura**, y eso en numpy son pocas líneas. No es un sustituto: para interfaz real de la app, texto y CSS, HyperFrames es mejor (y add-finder lo demostró).

| | Python + OpenCV (este video) | HyperFrames (add-finder) |
| --- | --- | --- |
| Velocidad | 441 frames en 85 s (2 CPU, tres escenas en paralelo) | ~0.7 s por frame en 2 CPU |
| Fuerte en | Video dentro del video, efectos por píxel, perspectiva | Componentes reales, tipografía, CSS |
| Débil en | Maquetar texto e interfaz a mano | Metraje y efectos procedurales |

27. **Tiras de frames sueltos antes de renderizar.** Cada escena es `frame(t)` pura, y `python project/bg.py 9.3 9.9 10.6` escribe una tira con esos instantes en ~1.5 s. Casi todos los fallos (suelo roto, abanico descentrado, fuego demasiado rápido) se vieron ahí y no en un render.
28. **Un archivo por escena.** Las tres se renderizan en paralelo y se unen sin recodificar. Para los iconos (v4 y v5) solo se volvió a renderizar el escritorio: 85 frames de 441.
29. **Tiempos como constantes.** Quitar una vuelta de música fue cambiar una resta en `common.py`; todas las escenas se movieron solas.
30. **El grano cuesta megas.** Con grano σ 5 el archivo salía de 67 MB (crf 17) o 30 MB (crf 21). Con σ 3 y tope de 8 Mbps, 15.6 MB sin diferencia visible.
31. **Tropiezos de 3D.** Si el borde cercano de un plano inclinado cruza la cámara (profundidad ≥ distancia focal) sale basura: hay que alejar el plano o alargar la focal. Y el signo de la inclinación: el primer «suelo» salió como techo.
32. **Recortar un icono redondo.** Rellenar el fondo blanco por inundación se mete dentro de un icono con aro claro; para el de `.flp` hubo que usar una máscara circular. Para el de `.als` sí sirvió, quedándose con la mancha más grande para quitar el nombre de abajo.
33. **Falsa alarma.** Los tiempos de los paquetes de un MP4 con cuadros B no van en orden; comprobar saltos ahí no dice nada sobre si el video se traba.
34. **Código muerto.** Había una toma número 13 (anillo pasando de lado) que nunca se vio: un tope en el índice la saltaba. Se encontró al documentar y se quitó. Conviene contar las tomas que salen en el render contra las definidas.

## 7. Proceso con el propietario

- **Una sola pregunta antes de empezar**, la única que cambiaba el resultado y tocaba su cuenta: con qué pagar la generación. Respondió con un toque. Todo lo demás se decidió y se dijo en la entrega.
- **Seis entregas en 34 minutos.** Cada mensaje suyo fue de una línea y cada respuesta, un archivo. Funcionó porque re-renderizar una escena tarda segundos.
- **«Trabado» no decía dónde.** Sin contador de frames hubo que adivinar y arreglar tres cosas a la vez. Con `review-copy-frame-counter` habría señalado el frame.
- **Avisar lo que no se cumplió, aunque no pregunte:** que el chico era una silueta provisional, que el clip a 480p se vería más blando, que los iconos son marcas de terceros, que la música no es suya.
- **Decir cómo está hecho.** Preguntó «¿con código? ¿o lo renderiza higsfield?». Le importa saber qué parte es de quién.

## 8. Lo que este video no cumple

Se hizo antes de que existieran estas reglas del repo. No se corrigió nada: el video ya estaba entregado.

| Regla | Qué pasó aquí |
| --- | --- |
| Copia con contador de frames en cada entrega | Ninguna la llevó |
| Zonas seguras de Instagram | Compuesto a sangre. Medido después: el buscador y «0 resultados» quedan bajo la barra superior; la barra del reproductor se corta a los lados |
| Componentes reales de la app | Reconstruidos a ojo desde capturas; tags sin sus colores |
| HyperFrames como herramienta | Python + OpenCV (justificado en la sección 6) |
| Medir con `find_hits.py` | Medido con un script propio, mismo principio |
| Caso por cada entrega | Registrados cuatro días después, desde la sesión |
| Cuestionario 1-10 al cerrar | No se ha pedido: el video no está cerrado |
| CTA de la cuenta («Comment GALER…») | El cierre es la landing: «Create ur Galer» |
| Texto en pantalla | No tiene; la historia se entiende sin sonido solo hasta el fuego |

## 9. Errores del agente

| Error | Consecuencia | Qué hacer |
| --- | --- | --- |
| Leer «algunos… y otros» como «todos» | Una vuelta extra | Cambiar solo lo nombrado y conservar la variedad |
| Acelerar metraje tomando el cuadro más cercano | «Está como trabado» | Mezclar cuadros; sin cortes a mitad de gesto |
| Entregar a 16 Mbps | Archivo de 30 MB para un teléfono | Tope de 8 Mbps desde la primera entrega |
| Arreglar tres causas posibles a la vez | No se sabe cuál era | Si se puede, preguntar el segundo o mandar copia con frames |
| No pedir encuadre cerrado en el prompt | Clip recortado y ampliado 3× | Describir cuánto del cuadro ocupa el sujeto |
| Intentar dos generaciones a la vez | La segunda falló por límite | Una por vez |
| Envolver coordenadas con módulo en el ruido | Costuras en el fuego | `BORDER_WRAP` |
| Inclinar un plano hasta cruzar la cámara | Toma rota en dos intentos | Comprobar que el borde cercano queda delante |
| Dejar una toma definida que nunca se muestra | Código muerto | Contar tomas renderizadas |
| No componer para el teléfono | Texto del buscador tapado en Instagram | Guía de teléfono antes del render |

## 10. Abierto

- Feedback del propietario sobre la v5, y si el video se cierra. Entonces: cuestionario 1-10.
- Las 3 propuestas ⏳ necesitan un caso nuevo, con aprobación explícita, para promoverse.
- Saber qué causaba lo «trabado».
- Si se retoma: bajar el buscador a y ≥ 270, meter la barra del reproductor en x 80–1000, tags con sus colores reales, alargar el cierre y cambiar la música.
