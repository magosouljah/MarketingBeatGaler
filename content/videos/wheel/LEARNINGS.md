# wheel — todo lo que aprendimos

Este documento resume la línea completa: el laboratorio de la rueda (lab-v1 y lab-v2, que terminó en wheel-v7, aprobado) y la tanda de 8 videos con canciones (songs-v1). El detalle de la coreografía (geometría, mediciones contra Apple y parámetros del `RIG`) está en [lab-v2/LEARNINGS.md](lab-v2/LEARNINGS.md); aquí solo va el resumen.

**Qué tan firme es cada punto.** Ninguna regla de este archivo es todavía una lección validada del Learning Engine. Cada una lleva una de estas marcas:

- **[propietario]:** lo pidió o lo dijo él.
- **[medido]:** sale de una medición reproducible.
- **[hipótesis]:** sin validar.
- **[proceso]:** cómo se trabajó.
- **[pendiente]:** algo que falta hacer.

La aprobación del 2026-11-06 se refiere al video v7, no a cada regla por separado.

---

## 1. Coreografía de la rueda (resumen de lab-v2)

1. **[medido]** La referencia no es una órbita: es una **rueda de rolodex**. Son unas 28 páginas radiales con paso de pala; la aparición es escalonada (1 → 3 → 12 → 26 páginas entre 1,23 y 1,57 s) y la velocidad va rápido–lento–rápido.
2. **[propietario]** Las portadas nunca forman una cuadrícula, nunca se ven por detrás y no vuelven a entrar al cuadro una vez que salen. El círculo no se levanta entero: las páginas que salen se retiran.
3. **[medido]** La pila final queda nivelada y paralela con el paso de pala en π. Así el borde nivelado de cada página cae sobre el eje de la rueda: lo que hizo falta fue entender la geometría, no probar números.
4. **[medido]** Para evitar la portada deformada de gran angular, la lente se cierra (62° → 50°) mientras la rueda se aleja (*dolly zoom*).
5. **[propietario]** Ningún texto se queda quieto. Las palabras entran pequeñas, bajas y ladeadas, y siguen creciendo y subiendo hasta el corte.
6. **[medido]** Ninguna métrica basta sola. La IoU de silueta no ve la orientación, el ángulo del eje mayor se satura con portadas cortadas por el borde, y el rotacional del flujo óptico es el que mejor detecta tirones de giro.

## 2. Música sobre un video ya aprobado (songs-v1)

7. **[medido]** **Las canciones del propietario estaban hechas sobre el reloj de v7.** Las cuatro tienen el drop en 1,30 s, justo cuando la rueda pasa de 3 a 12 páginas. Por eso el fragmento correcto empieza en 0,000 s, sin desplazamiento. Antes de buscar «el tramo más fuerte», conviene comprobar si la música ya viene compuesta para el corte.
8. **[propietario]** **El video dura lo que la canción** («alargar todo el video hasta que finalice la canción»). No se corta la cola. El tiempo extra va al cierre, que mantiene las velocidades de v7 hasta el último fotograma para no quedarse quieto.
9. **[medido]** **Para mover cortes al golpe se busca el onset más fuerte alrededor del corte aprobado.** El puntaje es fuerza × e^−(Δ/0,1 s)², con una ventana de ±0,18 s, y el resultado se ajusta al fotograma. Con eso, 9 de 16 cortes cayeron en un golpe. En el corrido y el dembow algunas palabras se quedaron sin golpe cerca: **[hipótesis]** una rejilla de beats o una ventana de ±0,25 s cubriría casi todos (propuesta `phase2-songs-v1--beat-sync-coverage`).
10. **[medido]** **Instagram: −14 LUFS integrados y pico real ≤ −1 dBTP, medidos en el MP4 final** (`ffmpeg ebur128=peak=true`), no en el WAV. Si la ganancia empuja el pico, entra un limitador transparente (`alimiter` sobremuestreado ×4); hizo falta en 2 de 4 canciones. Fades de 0,03 s (anti clic) y 0,25 s.
11. **[propietario]** **Versión blanca:** pidió fondo claro y texto negro, con el tono a propuesta del agente. Se propuso `#F3F1EC` (blanco cálido de papel) con texto `#0C0C0C`, el negro de la otra versión, y respondió «va» al conjunto de la propuesta. No hay aprobación creativa del render. **[medido]** Con blanco puro, las portadas de fondo blanco perderían el borde. Gracias a las variables CSS (`--ground`, `--ink`), la pill y la letra pequeña se invierten solas.

## 3. Variantes únicas sin romper lo aprobado

12. **[propietario]** Cada pieza tiene que ser única para que Instagram no la marque como spam, con cambios ligeros: portadas, ángulo inicial, ritmo y posición dentro de ±5 % y entradas de palabras.
13. **[medido]** **Solo se varía lo que va antes de la pila** (t < 3,46 s): fase inicial, `omega` ×0,97–1,04, posición ±0,05, escala ±3 %, orden de portadas con semilla (sin repetir vecinas) y valores de entrada de las palabras. La pila y el cierre son intocables: su forma depende del retiro de páginas y se rompe con cualquier cambio. Resultado: los 8 se distinguen entre sí (diferencia media de 23–29 niveles de gris) y la pila queda llena en todos (`songs-v1/evidence/contact-sheets/stack-frames-107-131-all.png`).
14. **[medido]** **Toda tanda de variantes lleva una fila de control con los valores aprobados**, y se comprueba que reproduce el video aprobado antes de variar nada. Esa fila destapó un detalle heredado que nadie había visto: en v7, «Free*» y «Storage» comparten 1–2 fotogramas (propuesta `phase2-songs-v1--word-overlap`, pendiente de decisión del propietario).
15. **[medido]** **Las variantes se escriben en una tabla de parámetros (`variants.json`) y se construyen por plantilla.** No se editan proyectos a mano. La tabla del README sale de ese mismo archivo.

## 4. Técnica

16. **[medido]** **HyperFrames es determinista:** volver a renderizar v7 dio un MP4 idéntico bit a bit (PSNR ∞). Comparar contra el MP4 aprobado es una prueba válida de que nada cambió.
17. **[medido]** **1080×1920 desde una composición de 720×1280:** el cuadro de 720 va dentro de un `#frame` con `transform: scale(1.5)`, y three.js usa `setPixelRatio(1.5)`. El texto CSS sale nítido y las portadas tienen resolución real. `--resolution` de HyperFrames no sirve aquí porque solo acepta múltiplos enteros. Coste: unos 25–40 s por render en la nube.
18. **[medido]** **Render a secuencia PNG y una sola codificación con ffmpeg**, que mete video y audio a la vez (H.264 High CRF 17 + AAC 256 kbps, `+faststart`). Así se evita codificar dos veces.
19. **[medido]** La contact sheet útil para un video con música lleva tres cosas: fotogramas cada 0,25 s con su número, la forma de onda debajo y una línea por corte. Así el propietario ve a la vez la sincronía y la imagen.

## 5. Proceso y repositorio

20. **[propietario]** **Solo existe `main`** (2026-11-16: «debe quedar solo main»). Se trabaja directo en `main`, sin ramas ni PR apilados. Los PR #1–#4 se habían fusionado con squash y dejaban commits huérfanos. La unificación se hizo con merges sin squash (para las ramas ya integradas por squash, merge con estrategia `ours`), comprobando archivo por archivo que nada se perdiera antes de borrar las ramas.
21. **[proceso]** **Si el shell del equipo del propietario no arranca,** se trabaja en la nube: se copian solo los archivos necesarios, el repo se clona desde GitHub y los entregables se devuelven con `device_commit_files`. Hay que avisarle que la copia local no se tocó con git: para alinearla, tiene que hacer `git fetch` y cambiarse a `main`.
22. **[medido]** **El repositorio es público.** Los WAV, MP4 y la referencia de Apple viven en `work/` y `reference-runs/` (ignorados). Las contact sheets sí se versionan porque solo muestran portadas que ya están en el repo.
23. **[pendiente]** Las entregas de songs-v1 salieron sin la copia con contador de fotogramas que exige hoy la regla 11 de `AGENTS.md` (la regla es posterior a la entrega). Si se retoma esta línea, cada prueba tiene que llevarla.

## 6. Abierto

- Decisión del propietario sobre los 8 videos (aprobación creativa y tono blanco), sobre la superposición heredada de v7 y sobre la ventana de los cortes.
- Dar de alta **FREEGALER** en BeatGaler antes de publicar.
- Diferencias que quedaron contra Apple (giro en la aparición, posición de la pila): ver [lab-v2/LEARNINGS.md §6](lab-v2/LEARNINGS.md).
