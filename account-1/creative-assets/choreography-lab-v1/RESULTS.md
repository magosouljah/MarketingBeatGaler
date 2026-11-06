# Choreography Lab V1 — resultados, diagnóstico y propuestas

**Nada de esto es aprobación creativa.** Son mediciones técnicas y una autoevaluación del agente; la decisión es del propietario. Casos del Learning Engine: `choreography-lab-v1-iter1`, `choreography-lab-v1-iter2`, `choreography-lab-v1-abc`, `apple-orbit-phase2-rerun-v1`.

## 1. Dos tipos de evidencia

- **Geometría exacta** (`evidence/geometry-metrics.json`): esquinas proyectadas, distancia a cámara y orientación de cada portada, leídas de la escena en cada uno de los 180 fotogramas. Verifica qué hace realmente cada variante.
- **Medición de imagen** (`evidence/motion-field-*.json`, `evidence/reference-intelligence/`, `evidence/reference-comparison.json`): el **mismo método** aplicado a la referencia de Apple Music y a nuestros MP4. Las fases se emparejan por función (entrada / órbita / clímax / final), no por reloj.

## 2. Diferencias técnicas entre A, B y C (geometría exacta)

Fases del laboratorio: entrada 0–1,4 s · órbita 1,4–3,3 s · peel/galería 3,3–4,9 s · aterrizaje 4,9–6 s.

| Métrica | A rígida | B independiente | C independiente + cámara |
| --- | ---: | ---: | ---: |
| Residuo rígido 3D (Kabsch, mediana, u/fotograma) | **0,000** | 0,034 | 0,034 |
| Recorrido de cámara (u) | 0 | 0 | **9,64** |
| Aceleración pico de cámara (u/fotograma²) | 0 | 0 | 0,022 (suave, C¹) |
| Portadas visibles en la órbita (mediana) | 22 | 19 | **13** |
| Contraste de escala cerca/lejos en la órbita (p90/p10) | 4,19 | **5,45** | 3,53 |
| Pares solapados en pantalla — órbita / clímax | 10 / 9 | 13 / **19,5** | 9 / 18 |
| CV de velocidad en pantalla — órbita | 0,32 | **0,65** | 0,60 |
| Coherencia de dirección — órbita (1 = todo igual) | 0,17 | 0,21 | **0,60** |
| Portadas de canto (\|facing\| < 0,25) — órbita | 0,15 | 0,14 | 0,13 |
| Distancia mínima portada–lente (u) | 6,61 | 5,14 | **4,07** |
| Aceleración máx. de centroide — clímax (px/fotograma²) | 4,3 | 25,2 | 19,1 |

Lectura:

- **A** es exactamente rígida (residuo 0) y uniforme (CV 0,32): se lee como carrusel. Cumple su papel de control y cae en el criterio de rechazo automático del handoff («carrusel uniforme»).
- **B** duplica la variación de velocidad (0,65) y obtiene el mayor contraste de escala (5,45) y el doble de solapamientos en el clímax: **el movimiento de objetos por sí solo ya crea profundidad y oclusión** sin mover la cámara.
- **C** añade 9,6 u de cámara sin tirones, pero con la cámara cerca **la estructura se fragmenta** (13 visibles, contraste 3,53) y la cámara impone un movimiento común (coherencia 0,60): el parallax de cámara se suma, pero tapa la lectura de la hélice. Aporta intimidad al inicio y a los héroes más cerca del lente (4,07 u).

## 3. Contra la referencia (misma medición de imagen)

| Fase | Métrica | Apple (ref.) | A | B | C |
| --- | --- | ---: | ---: | ---: | ---: |
| Arco de energía (relativo al pico) | entrada / órbita / clímax / final | 0,29 / 0,55 / **1,00** / 0,07 | 0,89 / 0,70 / 1,00 / 0,30 | **1,00** / 0,63 / 0,84 / 0,24 | **1,00** / 0,65 / 0,79 / 0,24 |
| Órbita | velocidad (alturas/s) | 0,62 | 0,26 | 0,23 | 0,31 |
| Órbita | cobertura de cuadro | 0,17 | 0,34 | 0,30 | 0,28 |
| Órbita | CV de velocidad | 0,41 | 0,37 | 0,67 | 0,58 |
| Clímax | velocidad (alturas/s) | 0,87* | 0,50 | 0,34 | 0,37 |
| Clímax | cobertura | 0,23 | 0,36 | 0,35 | 0,40 |
| Clímax | proxy de oclusión | **0,74** | 0,17 | 0,19 | 0,22 |
| Clímax | CV de velocidad | 0,69 | 0,36 | 0,68 | 0,66 |

\* subestimada: el barrido de la referencia supera la capacidad del flujo óptico.

## 4. Qué funciona, qué falla y por qué

**Funciona (técnico):**
1. Un solo `choreography.js` produce las tres variantes con `render --batch`; render determinista (A re-renderizado byte-idéntico); `lint`/`check` sin errores.
2. B y C sí tienen trayectorias independientes medibles y una variación de velocidad del orden de la referencia en el clímax (0,66–0,68 vs 0,69).
3. Las portadas héroe cruzan el primer plano y ocultan la galería en formación (pares solapados 18–19,5 en el clímax).
4. La cámara de C es continua (Hermite C¹) y aterriza exactamente en el plano maestro de B.

**Falla (medido):**
1. **Arco de energía invertido en B y C.** La entrada es la fase más enérgica (1,00) y el clímax queda en 0,79–0,84; la referencia sube hasta el clímax (0,29 → 1,00). Hipótesis: 24 portadas despegan del mazo en ~1 s con un ease que arranca a máxima velocidad (aceleración de centroide 152–220 px/fotograma²), y el clímax se apoya en aterrizajes que desaceleran.
2. **Demasiada ocupación de cuadro.** 0,28–0,40 vs 0,17–0,23: menos espacio negativo; riesgo de «collage» (ya rechazado antes).
3. **Clímax sin densidad de oclusión.** Proxy 0,17–0,22 vs 0,74: nuestras portadas se cruzan, pero no se apilan en capas grandes que se tapan entre sí.
4. **Órbita lenta.** 0,23–0,31 alturas/s vs 0,62.
5. **C pierde la estructura** durante la órbita (13 portadas visibles, coherencia 0,60).
6. **Hueco antes del clímax** (≈ 3,5–3,9 s): cuadro oscuro y disperso en B y C (visible en `contact-sheets/*climax*`).

**Corregido dentro del experimento (iteración 1 → 2):** el despegue hacia la galería usaba `easeOutQuint` desde la pose viva de órbita → tirón de velocidad de **72 px/fotograma²** (`evidence/iteration-1/geometry-metrics.json`). Se cambió a un ease con pendiente inicial cero (`easeSmoothOut`) → **25 px/fotograma²** en B y 19 en C. Es una corrección técnica verificada, **no** una regla creativa validada.

**Limitación de la herramienta descubierta:** el residuo afín 2D **no** separa una órbita rígida 3D de trayectorias independientes (A da 0,79). Para la referencia no hay geometría exacta: la prueba discriminante de la rigidez de la corona sigue abierta.

## 5. Propuestas para el siguiente experimento (no validadas)

Registradas como propuestas en `learning/proposals/choreography-lab-v1-abc--*.json`, cada una con su prueba de aceptación:

1. **energy-arc:** limitar la energía de entrada (despegue más corto y con arranque suave, mazo más pequeño) y hacer del clímax la fase más enérgica. Aceptación: diferencia media del clímax ≥ 1,3× la de la órbita y ≥ la de la entrada, más revisión del propietario.
2. **negative-space:** reducir escala o número visible durante la órbita hasta cobertura 0,15–0,25 manteniendo la galería final.
3. **climax-occlusion:** clímax con 3–5 portadas grandes en capas de profundidad cercanas que se tapan entre sí (no el riffle de Apple). Aceptación: proxy de oclusión ≥ 0,45 y pares solapados ≥ 20 con continuidad ≤ 30 px/fotograma².
4. **camera-legibility (C):** la cámara no debe bajar de ~16 portadas visibles en la órbita; mover la cámara más lejos o mover el objetivo, no acercarse.
5. **orbit-tempo:** subir la velocidad de órbita hacia 0,45–0,6 alturas/s y comprobar lectura en reproducción a 0,5×.

**Pregunta para el propietario:** ¿qué dirección merece la siguiente iteración — B (objetos, cámara fija) o C (objetos + cámara)? La métrica no decide gusto; ver `comparison-abc-side-by-side.mp4`.
