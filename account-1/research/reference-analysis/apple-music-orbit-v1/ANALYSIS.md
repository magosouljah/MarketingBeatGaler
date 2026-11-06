# Apple Music — primera referencia audiovisual real (V1)

**Actualización 2026-11-05:** reejecutado con Reference Intelligence V1 sobre una recodificación local medida contra este original → [PHASE2-RERUN.md](PHASE2-RERUN.md).

**Estado:** primer experimento de observación medido; **NO aprobado artísticamente**, no reconstruido, sin video nuevo renderizado. Cuenta: `account-1`.

## Procedencia y límites

El archivo `-5258203640291409657.mp4` fue recuperado de la **biblioteca de archivos que el usuario subió anteriormente**. Coincide visualmente con la referencia principal de [FIRST-VIDEO-REFERENCES.md](../../../design-references/FIRST-VIDEO-REFERENCES.md): [Apple Music](https://www.instagram.com/p/DcBoH7XgD1V/). Su SHA-256 es `74301c7f543eeb2695bdb496aca7e480150262e505ed5156184cceb4c5cdd2db`, tamaño 2.919.113 bytes. La copia no existe necesariamente en el checkout del IDE. **No subir el MP4 ni sus fotogramas derivados a GitHub:** el material original es una obra de un tercero; este commit almacena solamente datos derivados y observaciones.

Se ejecutaron **FFprobe y un análisis local independiente con OpenCV** sobre los bytes recuperados, no la CLI oficial de Reference Intelligence V1. No interpretar esto como prueba de que el pipeline V1 ya procesó este MP4. Próxima ejecución en el IDE: usar la CLI aprobada contra el archivo descargado en un directorio ignorado por Git.

## Datos medidos (no interpretación)

- Video vertical: **512 × 910**, **30 FPS**, **181 fotogramas**, duración del contenedor **6,033333 s**. PTS del primer fotograma **0 s** y del último **6 s**; intervalos de aproximadamente 33,333 ms.
- Pista de audio AAC detectada; inicio a **0 s** y duración indicada **5,926667 s**. No se examinó perceptualmente su sincronización.
- Diferencia media absoluta entre miniaturas grises consecutivas de 64×64: media del tramo **fotogramas 71–89 = 0,0579**; del tramo **110–129 = 0,1278**. El mayor valor observado está en **frame 122 (4,0667 s): 0,1720**. **No significa velocidad de cámara ni velocidad de las portadas.** También influye cuánto ocupan las portadas el encuadre.
- Datos reproducibles en [MEASUREMENTS.json](MEASUREMENTS.json), fuente identificada mediante su hash.

## Observaciones visuales por intervalos (aproximaciones, no cortes detectados)

| Tiempo aproximado | Observación |
| --- | --- |
| 0–1,2 s | Fondo blanco, logotipo de Apple Music; prácticamente no aparecen portadas |
| 1,3–1,6 s | Las portadas llegan en un grupo diagonal y empiezan a distribuirse |
| 1,6–3,0 s | Corona/arco de portadas alrededor de un espacio tipográfico central; variación de orientación, escala aparente, oclusiones y entrada/salida por bordes |
| 3,0–3,65 s | El anillo se abre/desplaza y el movimiento en pantalla aumenta; aparece texto de la oferta |
| 3,67–4,30 s | Pasos de portadas grandes por el primer plano, con fuerte perspectiva y oclusión; tramo de mayor diferencia de imagen medida |
| ~4,4–6,03 s | Despeje de las portadas y composición final fija con CTA |

Las portadas NO pueden describirse correctamente como un único círculo plano que rota rigidamente. Se aprecian transformaciones relativas y variaciones de escala/orientación. **No es posible recuperar una cámara 3D única del clip monocular sin otras restricciones.**

## Tres trayectorias 2D exploratorias

Se sembraron tres regiones **manualmente** en el fotograma 80 (2,667 s): portada de rosa púrpura, portada de cristal azul y portada fotográfica con figura. OpenCV KLT calculó la mediana de puntos característicos hasta el frame 90 o hasta perder puntos; detalle en [THREE_TRACKS.json](THREE_TRACKS.json).

- **Rosa púrpura:** centro estimado de `(0,7881; 0,5044)` en frame 80 a `(0,3400; 0,5386)` en frame 90.
- **Cristal azul:** de `(0,9258; 0,4709)` a `(0,4646; 0,5729)` en el mismo tramo.
- **Figura fotográfica:** de `(0,6680; 0,5593)` en frame 80 a `(0,3750; 0,5813)` en frame 86; a partir de ahí se interrumpe por pérdida de puntos fiables.

Coordenadas normalizadas: `x` crece hacia la derecha, `y` hacia abajo. Son **estimaciones de centros de features, no centros geométricos comprobados de las tarjetas**. Hay riesgo de drift por cruces, perspectiva y oclusión; no afirmar tracking semántico ni calcular 3D a partir de estas coordenadas.

## Tres hipótesis para la siguiente prueba original con HyperFrames

**Hipótesis A — Anillo rígido y cámara estática:** control negativo, útil para demostrar qué características de la referencia NO se explican con una órbita simple.

**Hipótesis B — Trayectorias individuales con varias capas de profundidad y cámara fija:** permite comprobar si el movimiento de objetos y las oclusiones reproducen la composición sin mover la cámara.

**Hipótesis C — Trayectorias individuales + cámara dolly/orbit original:** comprueba si el parallax y la dinámica mejoran con cámara móvil.

La comparación será en un **blocking corto con portadas originales de BeatGaler, no portadas de Apple Music**. Misma duración, tamaño y puntos temporales de revisión. Comparar trayectoria proyectada, relaciones de escala, continuidad de movimiento, cruces y lectura del texto, además del juicio artístico del propietario. Evitar escoger un candidato por métrica de pixels exclusivamente.

## Siguiente paso operacional

1. Copiar la copia del usuario a `reference-runs/apple-orbit/source.mp4` en su checkout del IDE (directorio ignorado por Git).
2. Ejecutar Reference Intelligence V1 contra esos bytes para crear manifiesto, PTS y evidencia local `validate`; verificar SHA-256 indicado.
3. Revisar las tres ROI/identidades y el tramo de primer plano en video continuo; corregir/split de tracks al perder identidad.
4. Generar y evaluar los tres blockings reproducibles, manteniendo todos los resultados fallidos y el feedback. **Sin aprobar ni promover ninguna regla artística automáticamente.**

### Aprendizaje pendiente

Todavía NO sabemos las trayectorias 3D reales ni la cámara. Aprendizaje inicial: el tramo 3,67–4,30 s requiere experimentar con grandes diferencias proyectadas, oclusiones y movimiento relativo; esta es una **hipótesis informada por la referencia**, no una regla validada.
