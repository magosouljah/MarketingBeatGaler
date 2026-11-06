# Lo que aprendimos: reconstrucción de la órbita de Apple Music (laboratorio V2)

**Estado:** el propietario aprobó `wheel-v7.mp4` como versión final del laboratorio en el chat, el 2026-11-06 a las 14:37 (hora de Ciudad de México): «ok finalizamos me encanta». Es el commit `f004327` de `experiment/phase2-3d-choreography-lab-v1` (PR #5). La aprobación se refiere al **video** v7. Las reglas de este documento salen del trabajo que llevó a ese video. Solo pasan a ser lecciones validadas del Learning Engine (`learning/lessons/account-1/`) si el propietario aprueba cada regla por separado. Hasta entonces, cada punto indica si es dirección del propietario, una medición o una hipótesis.

Detalle por iteración: [RESULTS.md](RESULTS.md). Casos: `learning/cases/choreography-lab-v2-wheel` … `choreography-lab-v7-wheel`.

---

## 1. Dirección del propietario (lo que pidió, en sus palabras o casi)

- **Acercarse lo más posible a Apple.** Las portadas nunca forman una cuadrícula. Entre A/B/C, la variante A fue la más cercana porque las portadas van ordenadas, no al azar.
- **Fondo `#0C0C0C`** y texto blanco.
- **Comparar fotograma a fotograma contra Apple.** El propietario da números de fotograma aproximados (±2): hay que revisar la vecindad, no solo ese fotograma.
- **Aparición escalonada:** las portadas van saliendo, no todas de golpe. La parte superior del arte apunta al centro del círculo (arte girado 180°).
- **Nunca se ve una portada «por detrás».**
- **Al salir, el círculo no se levanta entero:** las portadas que salen del cuadro desaparecen y no vuelven a entrar por abajo.
- **Ritmo:** rápido al salir, más lento hacia el fotograma ~50, otra vez rápido hacia el ~93.
- **El cambio de ángulo del círculo (≈ fotogramas 94–102) tiene que ser suave.**
- **Pila final (fotogramas ~116–127):** el ángulo de las portadas tiene que coincidir con Apple. Lo pidió varias veces y fue lo último que se resolvió. Las portadas van un poco más cerca, como en v6.
- **Ningún texto se queda quieto.**
- **Copy:** «Unlimited» / «Free*» / «Storage»; cierre «BeatGaler / 1 month of / Unlimited Free* Storage / for your beats / and projects», pill «CODE: …» y letra pequeña con la oferta.
- **Cierre con criterio propio:** «BeatGaler» grande, «1 month of» sin negritas y más chico, buenos espacios. No tiene que copiar a Apple.
- **Oferta:** 1 mes gratis con código de descuento, luego $11/mes en USD, con renovación automática. El código lo inventa el agente (FREEGALER); **hay que darlo de alta en BeatGaler antes de publicar.**

## 2. Lo que medimos en la referencia (Apple Music, encode de Instagram)

Se midió en `reference-runs/apple-music-ig/` (local, no versionado). El fotograma N del archivo es el fotograma N del original, a 30 fps.

- **Estructura:** no es una órbita, es una **rueda de rolodex**. Son ~28 páginas radiales, cada una girada sobre su línea radial (paso de pala). El «riffle» es el paso del borde de la rueda junto a la cámara.
- **Aparición:** páginas visibles por tiempo: 1,233 s → 1; 1,267 → 3; 1,300 → 12; 1,333 → 16; 1,400 → 20; 1,500 → 26; 1,567 s → todas. Primer fotograma con páginas: 1,20–1,23 s.
- **Velocidad** (mediana de píxeles en movimiento, px/fotograma a 360 px de alto): pico de 0,87 en el fotograma 48, mínimo de 0,54–0,55 en 72–75 y otra vez 0,9–1,1 en 90–99. El rotacional de pantalla alcanza 10,5 en el 48, baja a 5,1 en el 75 y vuelve a 6,8 en el 90.
- **Giro del círculo:** el eje mayor de la silueta va de +16° (fotograma 88) a −54° (99) y se queda en ≈ −57° hasta el 106. Es un giro limpio que se detiene; después la pantalla casi no rota (rotacional ≈ 0).
- **Pila final:** todas las portadas niveladas (bordes cercano y lejano horizontales), paralelas entre sí y apiladas una sobre otra, con los lados inclinados (el arriba corrido a la derecha). Son capas de tamaño casi igual: **efecto teleobjetivo**.
- **Palabras del centro:** cortes en los fotogramas 46, 66 y 91. Cada palabra entra al ~85 % de tamaño, más abajo y ladeada (unos −3,5°), llega al ~95 % en ~5 fotogramas y **nunca se detiene**. Sigue creciendo ~5 % y subiendo ~25 px, cada vez más despacio («1 mes»: de 212 a 223 px de ancho y 23 px hacia arriba en los fotogramas 71–87).
- **Cierre de Apple:** marca 0,158 del alto; titular 0,27–0,40; línea inferior 0,51–0,54; botón 0,59; letra pequeña 0,64. El titular entra a 4,37 s y hace zoom en su lugar (del 93 % al 100 % de su ancho final); la línea inferior y el botón suben 10–12 px; el logo es lo único que se queda quieto. Las últimas portadas salen hacia 4,47 s.

## 3. Qué funcionó (cómo está hecho v7; parámetros en `hyperframes/src/wheel.js`, objeto `RIG`)

- **Rueda + paso de pala** (`pitch`) para el anillo. Con 2,59 rad, los planos de página coinciden con Apple en la rueda y el acercamiento.
- **Velocidad angular trazada sobre el flujo de Apple** (`omega`): casi quieta hasta 1,4 s, pico a 1,6 s, mínimo a 2,45 s, otra vez rápida entre 2,8 y 3,15 s. Al final acelera para que las últimas portadas salgan a ~4,45 s.
- **Giro de pantalla sin pausas** (`tip`): una pausa a mitad del giro hace que la rotación propia de la rueda reaparezca y se perciba como un tirón.
- **Pila como rolodex (lo que resolvió el fotograma ~121):** el paso de pala va a π, así que el borde «nivelado» de cada página queda sobre el eje de la rueda y no cambia de dirección cuando la rueda gira. El giro de pantalla deja el eje horizontal (−1,57 rad) y una guiñada leve (`rotation[1]` = 0,2) da la inclinación de los lados. Con eso, todas las portadas quedan paralelas y niveladas, como en Apple. Medido: rotacional del riffle 0,04 (Apple 0,14; antes 0,98).
- **Lente que se cierra durante el acercamiento** (`fovTrack`, 62° → 50°) mientras la rueda se queda más atrás (*dolly zoom*): el tamaño en pantalla se mantiene y la perspectiva se aplana. Así desaparece la portada gigante deformada de gran angular.
- **Retiro de páginas** (`retireFrom`): una página que sale del cuadro después de 3,55 s no vuelve a entrar. Ojo: si se cambian el giro o la posición de la pila, páginas que salían un instante quedan retiradas y la pila se vacía antes de tiempo (ver §5).
- **Las dos caras de cada página imprimen la misma portada** con el mismo brillo, así que ninguna se lee como vista por detrás.
- **Texto siempre en movimiento:** entrada `power3.out` de 0,16 s (85 % → 95 %, de 26 px abajo y −3,5° a su lugar). Después, un `sine.out` más largo que la palabra (crece +5 %, sube ~26 px) que sigue en curso cuando entra la siguiente palabra. En el cierre: zoom lento del titular, deriva hacia arriba de la parte inferior y la marca también se mueve un poco.
- **Cierre en columna propia:** marca de 48 px, «1 month of» en Archivo regular de 26 px pegado al titular, titular de 76 px, línea inferior de 32 px, pill y letra pequeña repartida en líneas parejas (`text-wrap: balance`). Las fuentes son OFL y están dentro del proyecto, de modo que el render no depende de las fuentes del sistema.

## 4. Método de trabajo que sirvió

- **Comparar en el mismo reloj:** video lado a lado Apple | nuevo | anterior con número de fotograma, más una versión a 1/4 de velocidad. Es lo que más ayuda al propietario y al agente. **Solo local:** contiene píxeles de Apple y nunca se versiona.
- **Las métricas se complementan; ninguna basta sola:**
  - El **IoU de silueta** dice dónde hay portadas, pero no ve su orientación ni si se ve el frente o el reverso. Por eso se agregó el histograma de orientación de bordes, la medida de área trasera visible y el ángulo del eje mayor (`tools/fit_pose.py`).
  - El **ángulo del eje mayor se satura** cuando las portadas grandes quedan cortadas por el borde del cuadro: ahí dejó de responder a los cambios de giro. En esos tramos no hay que fiarse de él.
  - El **rotacional del flujo óptico** es el mejor indicador de cuánto se ve rotar la escena. Con él se detectó el tirón del giro (v6) y se confirmó la pila nivelada (v7).
  - La **velocidad mediana por fotograma** sirvió para reproducir el ritmo rápido–lento–rápido.
- **Explorar con cuadrículas de candidatos en el fotograma exacto** que señala el propietario, en grande, antes de renderizar el video completo. Cambiar un parámetro de la pila obliga a revisar toda la secuencia (por ejemplo 100–131), porque mueve el flujo y el retiro de páginas.
- **Entender la geometría antes de ajustar números:** lo que resolvió el fotograma ~121 no fue probar ángulos al azar. Fue notar que las portadas de Apple son paralelas, lo que exige que su borde nivelado esté sobre el eje de la rueda.

## 5. Errores que no hay que repetir

- **Levantar el círculo entero** para sacarlo del cuadro: el propietario lo rechazó. Hay que retirar las páginas que salen.
- **Mostrar el reverso de las portadas** o invertir la inclinación de los planos (v4/v5).
- **Portadas «en diamante»** en la pila: cada una giraba distinto porque el borde nivelado no estaba sobre el eje. Tampoco funcionó girar cada página en su plano (`twist`, sin usar en v7): nivela una portada y las vecinas siguen girando.
- **Lente gran angular con la pila muy cerca:** los bordes se abren a 30° y 80° en lugar de los ~55° de Apple.
- **Pausar el giro de pantalla a la mitad** (v6, 3,4–3,5 s).
- **Suponer la causa sin medirla:** el giro durante la aparición no venía de la rueda. Con la rueda quieta, el rotacional siguió en 4,0. Esa hipótesis quedó descartada.
- **Cambiar el nombre de archivos de evidencia que cita un caso:** rompe la trazabilidad.

## 6. Abierto (hipótesis sin validar; propuestas en `learning/proposals/choreography-lab-v7-wheel--*`)

- **Aparición:** se ve un giro (rotacional 4,0 contra 0,56 de Apple). La sospecha es el crecimiento de cada página al aparecer (`popIn`) sobre un anillo inclinado.
- **Después del giro del círculo** (fotogramas 99–108) queda rotación (3,4–4,5 contra ≈ 0 de Apple).
- **Posición de la pila:** es más angosta y está más a la derecha que la de Apple (IoU del riffle 0,32). Idea: desplazar la imagen con un *lens shift* (`camera.setViewOffset`), que mueve la pila sin cambiar su ángulo.
- **Acercamiento:** las portadas se tapan menos entre sí (0,45 contra 0,58).

## 7. Operación

- Render: `cd hyperframes && npx --yes hyperframes@0.9.17 render --quality draft -o ../evidence/renders/wheel-v7.mp4`. Variables necesarias en Linux: `HYPERFRAMES_BROWSER_PATH=/usr/bin/google-chrome`, `HYPERFRAMES_SKIP_SKILLS=1`, `DO_NOT_TRACK=1`. Para revisar: `npx --yes hyperframes@0.9.17 check` y `lint`.
- Mediciones: `python -m shared.motion_metrics.motion_field VIDEO OUT.json`, `tools/frame_iou.py`, `tools/fit_pose.py` y `tools/compare_same_clock.py` (detalles en [README.md](README.md)).
- `DIRECCION.md` no se tocó en ningún momento. La app de BeatGaler tampoco: solo se leyeron sus portadas.
