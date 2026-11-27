# Técnicas de animación — conocimiento activo

Salen de la producción de `old-beats` (C-C1-H1, 2026-11-26). Cada regla nombra el problema que resuelve. Son técnicas, no una estética obligatoria.

## 1. Nada se detiene a medio camino

El defecto que más se nota es un objeto que frena hasta cero y vuelve a arrancar. Casi siempre son dos curvas de easing pegadas: una que termina en reposo y otra que empieza desde reposo.

- **En un relevo se igualan posición y velocidad.** Cuando un objeto pasa de un movimiento a otro (un vuelo que termina en una rueda que gira, una cámara que llega a una escena que se mueve), el primero debe llegar con la velocidad y la dirección que tiene el segundo en ese instante.
- **La velocidad de un trayecto solo sube o solo baja.** Recorrer la ruta por longitud de arco con una velocidad que crece (por ejemplo de 0.35·v a v) evita paradas y retrocesos. Un easing in-out sobre la posición no lo garantiza.
- **Entrar de lado, no de frente.** Si el destino se mueve, la ruta llega tangente a ese movimiento: un arco cuyo punto de control está «detrás» del destino en su dirección de avance. Una ruta recta hacia un destino que luego sale en otra dirección se lee como pausa aunque la velocidad no sea cero.
- **Cuidado con las vueltas en U.** Una curva de Hermite con velocidad final impuesta puede pasarse y regresar si el origen está cerca del destino. Comprobar midiendo.
- **Medir px por frame.** Sacar la posición del objeto en cada frame del tramo dudoso y mirar la serie: si baja a 1–3 px y vuelve a subir, hay una parada aunque en el mosaico no se vea.

## 2. Quién pone en marcha a quién

- **El que llega inicia el movimiento.** Si una portada «arranca» un círculo, el círculo está quieto hasta que ella llega y empieza a girar con la velocidad que ella trae; después acelera. Si el círculo ya giraba, se lee como que la atrapa y se la lleva.
- **No esperar a que se junten todos.** El sistema arranca con el primero; los demás se enganchan sobre la marcha.
- **Empezar lento y acelerar.** Un arranque a velocidad plena se siente brusco; una rampa desde la velocidad de llegada se siente natural.

## 3. Líder y cola

- **El primero es el líder y los demás quedan detrás**, en el sentido del movimiento. En un anillo, «detrás» es el hueco que todavía no ha pasado por el punto de entrada.
- **Cada seguidor entra cuando su hueco pasa por donde entró el líder.** El momento de llegada de cada uno se calcula a partir del giro real (cuánto ha avanzado el ángulo), no con un escalonado fijo.
- **No cambiar la coreografía cuando solo falla el orden.** «Se ponen adelante en vez de atrás» fue un problema de capas y de orden de llegada; rehacer el vuelo como una fila sobre una vía fue peor que lo anterior.

## 4. Capas: quién se ve delante

- **Decidir el orden de profundidad a propósito**: el líder al frente, los que llegan después detrás, y los que ya llegaron por encima de los que aún vuelan.
- **Un `z-index` solo compite dentro de su contexto de apilamiento.** Hijos con `z-index` dentro de una capa sin contexto propio saltan por encima de capas hermanas (por ejemplo un canvas). Dar a la capa `z-index` o `isolation: isolate` y ordenar las capas hermanas explícitamente.
- **Comprobar las capas frame a frame en el punto donde se cruzan.** Un cambio de capas «hecho» que no se verificó ahí puede no haber tenido efecto.

## 5. Transformar, no sustituir

- **Las mismas imágenes pasan de una composición a la siguiente.** Si las portadas de la línea del tiempo forman el círculo, son esas portadas, no otras que aparecen mientras las primeras se desvanecen.
- **Relevo exacto entre 2D y 3D.** La imagen 2D se lleva a las cuatro esquinas proyectadas de su página 3D (homografía con `matrix3d`) y en ese frame la sustituye la página real.
- **Viajar rígido, deformar al final.** Interpolar esquina a esquina desde lejos cruza el cuadrilátero y la imagen revienta en una mancha enorme. El cuadrado viaja como cuerpo rígido (centro, tamaño, giro) y solo en el último tramo se deforma hasta las esquinas exactas.
- **Proteger las poses degeneradas.** Si la página destino está de canto, pegada a la lente o fuera de cuadro, apuntar a su pose de un instante después o no dibujar ese frame.
- **Reutilizar el código, no el video.** Un rig aprobado se copia y se parametriza (imágenes, momento en que nace cada pieza, velocidad inicial); no se pega su animación tal cual con otras imágenes.

## 6. Cámara

- **Ruta con velocidades, no con paradas.** Una spline de Hermite con la velocidad fijada en cada punto permite pasar despacio por donde hay algo que leer y rápido entre medias, sin detenerse nunca.
- **Lo que debe verse necesita unos 30 frames nítidos.** Con 15 no se aprecia. Frenar al acercarse, no parar.
- **Sincronizar el paso lento con la palabra.** Si la locución nombra algo, la cámara pasa por ahí en ese momento.
- **Un recorrido «largo» se construye con contenido y tiempo**, no solo con distancia: más elementos pasando, un principio que se vea como principio (tope, nada a la izquierda) y un final que apunte al futuro.
- **El objeto donde se detiene queda centrado** y ya con su aspecto definitivo; la siguiente escena se abre alrededor de él sin que cambie.
- **El desenfoque de movimiento solo en los tramos rápidos**; por debajo de cierta velocidad se quita para no ensuciar lo legible.

## 7. Nada encimado

- **Cada cosa reserva su caja antes de colocarse**: notas, flechas, años, texto y objetos. Lo que cae en una caja reservada no se coloca.
- **Carriles intercalados.** Con dos filas por lado, la exterior va desplazada medio paso para que su hilo pase entre los objetos de la interior.
- **Las notas manuscritas solo sirven si se leen**: grandes, en color que destaque, con flecha a lo que señalan y situadas donde la cámara va lenta. Las que pasan a toda velocidad son textura, no información.

## 8. Tiempo y sonido

- **Anclar a audio medido.** Palabras con `shared/transcription/align_words.py`, golpes con `shared/editing/find_hits.py`. Los cortes y entradas van a tiempos medidos, no estimados.
- **Sin huecos de silencio.** Si después del hook queda un tramo sin voz ni música, la siguiente frase entra pegada y la animación ocurre debajo.
- **La caída del beat sobre la palabra clave** (la batería entró en «fire») vale más que cualquier efecto.
- **Los beats suenan fuertes.** Bajo la voz ceden poco y con rampas lentas; sin bombeo.
- **Grabaciones reales a pantalla completa**, con subtítulos en bloques cortos sincronizados a la voz.
- **Si una grabación no alcanza**, repetir compases enteros en el audio y frenar el video cuando ya va saliendo de cuadro; avisar al propietario y pedir una grabación más larga para la versión final.
- **`alimiter` de ffmpeg sube el nivel solo** (`level` viene activado). Usar `level=0` y medir LUFS después.

## 9. Herramientas

- **Todo el cuadro es función pura del tiempo** (`renderT(t)`), filmado con Chrome/Playwright frame a frame. Las imágenes que cambian por frame se decodifican antes de capturar.
- **Tramo suelto con numeración global**: `render.py seg` + `drawtext` con `start_number` igual al frame inicial.
- **Mosaicos de frames consecutivos** (no uno de cada diez) para revisar relevos, capas y saltos.
- **Sonda numérica**: una página cargada en Playwright que devuelve posición por frame de un elemento.
