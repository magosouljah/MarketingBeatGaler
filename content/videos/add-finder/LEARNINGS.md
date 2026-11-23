# add-finder — todo lo que aprendimos

Resumen legible de lo aprendido haciendo este anuncio (2026-11-13/14). La versión formal, con evidencia y prueba de aceptación por regla, vive en el Learning Engine:

- **22 lecciones validadas** en [`learning/lessons/account-1/`](../../../learning/lessons/account-1/): salieron de un fallo, se corrigieron y el propietario aprobó la versión que las cumplía (v5).
- **3 propuestas pendientes** en `learning/proposals/`: corregidas en la última entrega pero sin aprobación explícita todavía. Están marcadas abajo con ⏳.

Las reglas son de la **cuenta 1**. Lo técnico (secciones 5 a 8) sirve para cualquier cuenta.

---

## 1. Ritmo y estructura

1. **El video manda sobre la música** (`pacing-video-leads-music`). La v1 completa duraba 21.9 s porque cada escena esperaba un golpe del beat. Si la música obliga a esperar, se recorta o se desplaza la música. La final dura 11.9 s.
2. **Ningún encuadre quieto más de ~2 s** (`no-static-screen-over-two-seconds`). Mientras dura una escena la cámara sigue empujando y pasa algo nuevo cada medio segundo.
3. **Camino más corto al CTA** (`shortest-path-to-cta`). Encontrar el beat, Play, silencio, drop y zoom al disco eran el centro del guion original y se cortaron enteros: el producto ya se había entendido. El último gesto (clic en el tag) se usa como transición al cierre.
4. **Los golpes van sobre transientes medidos** (`beat-sync-measured-hits`). Nunca segundos redondos ni una rejilla BPM × compases: el kick real estaba 0.36 s antes de donde decía la cuenta teórica. Ver sección 6.
5. **Si la voz no cabe, se alarga la imagen** (`voice-phrase-spacing`). Pausa audible de 0.2 s o más entre las dos mitades de una frase. Se puede abrir el video sin música.

## 2. El cursor como personaje

6. **Está desde el primer segundo y busca** (`cursor-searches-from-start`): entra, recorre, visita archivos, y la fila bajo el dedo se tiñe de azul claro.
7. **Un clic es una decisión en cuatro tiempos** (`cursor-click-decision`): llegar, quedarse totalmente quieto al menos 0.2 s, encogerse a ~0.75× con sonido y aro, soltar.
8. **Cursor y scroll nunca a la vez** (`cursor-and-scroll-never-together`): juntos parece que la mano arrastra la página.
9. **Velocidad de mano real** (`cursor-natural-speed`): cada desplazamiento dura 0.3 s o más, con pausas; tres saltos en medio segundo se ven falsos.
10. ⏳ **En el plano final va centrado** (`cta-cursor-centered`): si tapa texto se mueve el texto, no el cursor.

## 3. Texto en pantalla

11. **Palabras, no frases** (`type-words-not-sentences`): sueltas, enormes (casi todo el ancho útil), una idea a la vez, detenidas lo justo para leerse.
12. **Sólidas** (`type-solid-not-transparent`): opacidad 100 %, un color pleno, sin iconos. El contraste se resuelve con halo o sombra.
13. **Nunca tapan ni imitan la interfaz** (`type-never-covers-or-fakes-ui`): sin fondo propio, sin franjas de fila ni selección azul. Las repeticiones van en bloques separados por aire, con el mismo margen izquierdo y el mismo ancho.
14. **Sincronía por alineación forzada** (`word-timing-forced-alignment`): la palabra llega como máximo 2 frames antes de oírse. Ver sección 6.

## 4. Imagen y producto

15. **Componentes reales de la app** (`real-product-ui-components`): la barra de tags se reconstruyó leyendo `TagNavigation.tsx` y `gallery.css`, con la paleta real. No se inventa un «parecido».
16. **Logos de terceros solo mientras es un archivo** (`daw-logos-only-as-files`): FL Studio y Ableton aparecen en la lista y en el vuelo; al caer en la Gallery, icono neutro.
17. **La carpeta se parece a la de un productor** (`file-type-variety`): `.wav`, `.mp3`, `.flp`, `.als` mezclados, con nombres como `beat_final_v3 (2).wav`.
18. **Mutación con reloj propio** (`cover-mutation-random-fast`): orden aleatorio, en ráfagas sobre el redoble; la portada crece desde un punto en ~0.2 s y los datos entran ~0.1 s después. Todo en 1.3 s.
19. **Dispersión de verdad** (`scatter-covers-only-varied-angles`): solo portadas, con ángulo, tamaño y giro distintos y sin simetría entre lados.
20. **Profundidad de campo** (`floating-depth-of-field`): foco en el protagonista; lo cercano grande y desenfocado, lo lejano pequeño y atenuado. Es lo que hace que lo flotante se vea caro.
21. **Motas, no líneas** (`speed-lines-read-as-rain`): los trazos blancos largos se leen como lluvia.
22. **Scroll con inercia** (`scroll-inertia-curve`): ataque rápido y cola exponencial, `(1 − e^(−5.2·u^1.25)) / (1 − e^(−5.2))`. Un ease in-out simétrico se siente como frenazo.
23. ⏳ **Componer para el teléfono real** (`instagram-safe-zones-measured`): Instagram recorta ~49 px por lado y tapa ~250 px arriba. La ventana se baja y se deja flotar con fondo alrededor; no se agranda su barra de título. Ver [`INSTAGRAM-SAFE-ZONES.md`](../../../shared/technical-qa/INSTAGRAM-SAFE-ZONES.md).
24. ⏳ **Planos 3D inclinados no se atraviesan** (`floating-covers-no-intersection`): la disposición final se resuelve antes de animar y la inclinación se limita a ~32°.

## 5. Proceso con el propietario

- **Preguntar todo antes de producir.** Cinco rondas de preguntas numeradas con respuesta recomendada cerraron el concepto antes de escribir una línea de código. Lo que parecía decidido en el documento original cambió bastante (ver [BRIEF.md](BRIEF.md)).
- **Pruebas cortas del momento más difícil primero.** Las cuatro primeras entregas fueron solo el tramo Finder → Gallery (7 a 10.7 s). Hasta que eso gustó no se hizo el anuncio completo.
- **Copia con contador de frames en cada entrega** (`review-copy-frame-counter`). Desde entonces el feedback llegó como «F124 a 141» en vez de «por el segundo 3». Si cambia el inicio del video, avisar que la numeración se recorrió.
- **«Ya te enseñé lo que me gusta y lo que no».** Con referencias y varias rondas, el propietario espera que el agente decida solo. Preguntar solo lo que cambia el resultado y proponer siempre una respuesta.
- **El propietario corta sin apego.** La idea más querida del concepto (Play en el drop) salió en un mensaje. No defender el guion: defender que se entienda.
- **Aprobación ≠ última entrega.** La aprobación explícita fue a la v5. Lo corregido después sigue como propuesta hasta que lo confirme.
- Notas del propietario para este proyecto: solo orgánico; «BeatGaler» se pronuncia «galer»; él hace la mezcla final; puede mandar más portadas si hacen falta.

## 6. Audio: cómo medir en vez de adivinar

**Golpes del beat.** [`shared/editing/find_hits.py`](../../../shared/editing/find_hits.py) separa kicks (< 150 Hz) y cajas (150–2500 Hz) y lista sus tiempos. Con `--offset` se obtienen ya en tiempo de video. El MP3 trae ~35 ms de relleno al inicio; por eso se mide el archivo real, no se calcula.

**Palabras de la voz.** [`shared/transcription/align_words.py`](../../../shared/transcription/align_words.py) hace alineación forzada contra el texto con pocketsphinx. Mirar la envolvente de volumen falla: en «beats» la explosión de la «b» y la «ts» final parecen dos palabras, y OF quedó 6 frames tarde y BEATS 9. Nombres propios se pasan con fonemas (`--say galer="G AA L ER"`).

**Encajar música y video.** Elegir qué kick debe caer en el momento clave y desplazar el inicio del archivo: aquí el kick de 5.346 s cae en el clic de 4.80 s, así que la música entra desde 0.546 s. Los cortes de música se hacen en compás o dentro de un silencio.

**Mezcla** (provisional, en `tools/render.sh`): voz mono centrada y subida, beat a 0.85 que baja a 0.50 bajo la última frase, clic 15 ms antes del frame para que se perciba a tiempo, `amix normalize=0` y limitador al final. `normalize=1` baja todo según el número de entradas.

## 7. HyperFrames: técnica y tropiezos

Detalle en [`shared/hyperframes/README.md`](../../../shared/hyperframes/README.md). Lo esencial:

- **Una función pura `frame(t)`**. Un solo tween de GSAP mueve `driver.t` y un setter llama a `frame(t)`, que calcula todos los estilos desde cero. Sin estado acumulado: cualquier frame se puede renderizar suelto y los tramos se pueden unir.
- **Tiempos como constantes con nombre** (`H0`, `H1`, `TF`, `TEND`…) arriba del script. Mover un golpe es cambiar un número.
- **Render por tramos**: ~0.7 s por frame en 2 CPU. `--start/--end`, unir con `-c copy`, audio aparte. Cambiar solo el audio no requiere volver a renderizar.
- **Lint antes de mirar capturas.** Una variable declarada dos veces dejó todos los frames en blanco sin error visible.
- **Nada más que `index.html` en la raíz del proyecto.** El lint lee cualquier `.html`; los respaldos van fuera.
- **`text-indent` se hereda** a los `inline-block` hijos y descoloca palabras repetidas: usar `margin-left` en el primer hijo.
- **Fuentes locales con `@font-face`**; el lint rechaza fuentes del sistema.
- **`preserve-3d` parte los planos que se cruzan**: por eso el resolvedor de la regla 24.
- **Dos temas con un archivo**: `theme.js` define `window.BG_THEME`; el CSS cuelga de `html[data-theme="light"]`.
- En entornos sin descarga de Chrome: `HYPERFRAMES_BROWSER_PATH=/usr/bin/google-chrome`.

## 8. Errores del agente (para no repetirlos)

| Error | Consecuencia | Qué hacer |
| --- | --- | --- |
| Colocar golpes por cálculo de BPM | La cuadrícula caía a mitad de un redoble | Medir transientes |
| Estimar palabras por volumen | Texto 6–9 frames fuera | Alineación forzada |
| Disfrazar el texto de interfaz para «integrarlo» | Tapaba el Finder y parecía parte de él | El texto va encima, sin fondo |
| Esperar al drop | Video lento, 21.9 s | El video manda |
| Inventar una barra de tags parecida | No era la del producto | Leer el componente real |
| Arreglar la isla dinámica agrandando la barra de la ventana | No resolvía el recorte lateral | Medir la captura real y bajar la ventana |
| Componer a sangre en 1080×1920 | Bordes cortados en el teléfono | Guía de teléfono antes del render |
| `grep -m1` con `pipefail` en un script | Fallo silencioso | `fc-match` directo; probar cada script |

## 9. Calificación del propietario (2026-11-15)

Cuestionario v2 sobre la final v2: **promedio 7.0** en 14 aspectos ([`scores/add-finder.json`](../../../learning/scorecard/scores/add-finder.json)).

| Nota | Aspectos |
| --- | --- |
| 9 | Fidelidad al producto |
| 8 | Formato en teléfono |
| 7 | Sincronía, Movimiento, Cámara y transiciones, Claridad visual, Acabado premium, Entendimiento, Control de calidad, Criterio propio, Ejecución global |
| 6 | Ritmo, Texto, Montaje de audio |
| — | Eficiencia (sin calificar) |

Qué hay detrás de los 6 (caso `add-finder-scorecard-v1`, tres propuestas nuevas):

- **Ritmo:** el cierre con el CTA es largo (F260–F357, 3.2 s).
- **Dispersión:** «están todas del mismo tamaño y no se sienten dinámicos».
- **Texto:** no convence ningún grupo de letras: «realmente siento que el texto se podría ver mejor». Mandará referencias.
- **Montaje de audio:** el 6 no es por la colocación del audio sino por «cómo queda con las letras al mismo tiempo». Texto y voz se diseñan juntos: para el siguiente video, enseñar 2 o 3 tratamientos de letras como clips cortos **con la voz sonando** y animar solo el elegido (caso `add-finder-scorecard-v1-followup`).

**Video cerrado:** «No hagas otra versión, es suficientemente buena». Estas correcciones se aplican al siguiente video, no a este.

## 10. Abierto

- El propietario cerró el video como «suficientemente buena» (2026-11-15). Falta que confirme si eso cuenta como aprobación para promover las 3 propuestas ⏳.
- Referencias de texto que enviará el propietario.
- Durante el medio segundo de dispersión las portadas aún pueden rozarse al pasar; en reposo no.
- Mezcla definitiva.
- `DIRECCION.md` sigue diciendo que la prioridad es la órbita; solo el propietario puede autorizar ese cambio.
