# Pendientes: lecturas priorizadas, vacíos y preguntas abiertas

**Estado al 2026-11-24.** Esta biblioteca tiene el mapa de las ocho áreas y 21 fichas. Es una primera ronda: hay más localizado que leído.

## 0. Balance honesto de esta ronda

| | Cantidad | Nota |
| --- | --- | --- |
| Fuentes localizadas en mapas | ~230 | Calidad desigual; muchas marcadas `[MEMORIA]` |
| Fichas con **lectura directa** del texto original | 13 | Todas parciales (capítulos concretos), y todas de dominio público |
| Fichas por **extracción** de texto completo | 6 | Artículos y documentos abiertos; pueden faltar matices y cifras de figuras |
| Ficha mixta | 1 | Loewenstein 1994 (solo abstract) leído a través de una revisión de 2019 (extracción) |
| Ficha solo por **resumen** | 1 | Rubin (índice y una reseña, vistos por un agente) |
| Libros de pago leídos | 0 | Ninguno |
| Principios sintetizados | 17 | 9 de comunicación, 1 puente, 7 de sabiduría y oficio |

**Sesgo de esta ronda:** se leyó lo que era legal y accesible, es decir, clásicos en dominio público y artículos abiertos. Eso dejó muy bien cubierta la raíz histórica y filosófica, razonablemente la psicología de la curiosidad y la persuasión (vía agentes), y **mal cubiertos el conocimiento musical técnico y el profesional actual**, que son justo las áreas donde el propietario pidió no fiarse solo de libros.

---

## 1. Lo que solo puede resolver el propietario

1. **Libros que tengas.** Si tienes *The Creative Act* o algún texto del Cuarto Camino (*Fragmentos de una enseñanza desconocida*, *Psicología de la posible evolución del hombre*, Nicoll), pásalos como hiciste con Atkinson, o indica capítulos. No hay edición legal gratuita de ninguno.
2. **Jurisdicción.** ¿Para qué países quieres el conocimiento de regalías y contratos? Hoy solo hay EE. UU. Sin esto no se puede priorizar México, España o el resto.
3. **Tu propio oficio como fuente.** Varias ideas tuyas registradas en `pipeline/hooks/EVIDENCIA.md` coinciden con fuentes de la biblioteca sin que las conocieras. Tu experiencia produciendo y vendiendo beats es una fuente `OFICIO` de primera mano que no está escrita en ningún sitio del repo más allá de la historia de origen. Una sesión de preguntas sobre lo que sabes de producción, de trato con artistas y de qué beats te piden rendiría más que muchos libros.
4. **Métricas de retención.** Varios principios (K-02, K-03, K-08) solo pueden comprobarse con curvas de retención por segundo de tus videos. Ningún estudio revisado por pares cubre video corto para este público: los agentes buscaron y no encontraron.
5. **Acceso institucional.** Varias fuentes clave son de pago (Loewenstein 1994 legible, Friestad & Wright 1994, Huron). Si tienes acceso por alguna biblioteca, desbloquea las tres más importantes del proyecto.
6. **Decisión de integración.** ¿Quieres que las fuentes leídas se registren también como filas `EV-…` en `pipeline/1-investigacion/evidencia.csv`? No lo hice porque el esquema de `solidez` no tiene categoría para estudios académicos primarios y AGENTS.md prohíbe cambiar el esquema sin más. Opciones: usar `texto_historico` y `fuente_secundaria` tal cual, o autorizar una categoría nueva.

---

## 2. Lecturas priorizadas

Criterio de orden: cuánto cambia lo que hacemos × si es accesible legalmente ya.

### Prioridad 1 — accesibles ahora, alto impacto

| # | Fuente | Por qué | Acceso | Alimenta |
| --- | --- | --- | --- | --- |
| 1 | **Bjork & Bjork (2011)**, «Making things hard on yourself, but in a good way» | Decide la tensión fluidez/aprendizaje, la más importante para un canal que enseña | PDF abierto (laboratorio de los autores) | K-06 |
| 2 | **Aristóteles, *Retórica*, libro II, caps. 2–11** | Cada emoción: en qué estado se siente, hacia quién y por qué. Es la lectura que más puede afinar el Mapa de Deseos | Ya descargada | K-01, Mapa |
| 3 | **Kidd & Hayden (2015)**, «The Psychology and Neuroscience of Curiosity» | La mejor revisión única de curiosidad, según el agente A1 | Abierta; el acceso automático falló por captcha — probar otra ruta | K-03, K-10 |
| 4 | **DeSantis, *Making Music***: los 21 capítulos gratuitos restantes | Material directo para productores, con problema y porqué | Web oficial | K-08, K-13, K-14 |
| 5 | **McEnerney, «The Craft of Writing Effectively»** (charla, U. de Chicago) | El valor está en el problema del lector, no en lo que sabe el autor | Vídeo público; transcripción de terceros localizada | K-01, K-06 |
| 6 | **Golman & Loewenstein (2016)** | Versión actual y legible de la teoría de la brecha | PDF abierto (CMU) | K-03 |
| 7 | **Bordwell, blog**: sobre el tráiler y sobre «la bomba bajo la mesa» | Vocabulario de quién sabe qué y cuándo | Abierto | K-04 |
| 8 | **Münsterberg, cap. VI y X**; **James, *Principles*, cap. XI** | Completar dos fuentes ya abiertas | Ya descargadas | K-02, K-07 |
| 9 | **Toussaint (2005)**, ritmos euclidianos | Estructura matemática de tresillo, clave y dembow; candidato fuerte para público latino | PDF del autor (localizado, sin abrir) | nuevo principio de ritmo |
| 10 | **Sedikides et al. (2022)**, nostalgia y música; **Jakubowski et al. (2017)**, melodías pegadizas | Lo más musical del área de memoria y emoción | PDF abiertos | nuevo principio |
| 11 | **Hume, «Of the Standard of Taste»** | Cómo se forma el criterio: el hueco de K-11 | Edición legal en Liberty Fund (ojo: el volumen de Gutenberg no lo incluye) | K-11 |
| 12 | **Wallas, *The Art of Thought*** y **Sio & Ormerod (2009)** | Incubación con estructura y con datos | Dominio público / por localizar | K-11 |
| 13 | **William Archer, *Play-Making: A Manual of Craftsmanship*** (1912) | Manual de oficio dramático poco citado. Índice verificado en el texto: IX «"Curiosity" and "Interest"», X «Foreshadowing, Not Forestalling», XI «Tension and Its Suspension», XIII «The Obligatory Scene», XIV «The Peripety», XVII «Keeping a Secret». Hallazgo propio; contenido sin leer | Ya descargado (dominio público) | K-03, K-04, K-05 |

### Prioridad 2 — accesibles, impacto medio o más especulativo

- **Tolstói**, caps. X–XII (los métodos del arte falsificado) y XVI.
- **Longino, *De lo sublime*** (descargado): las cinco fuentes de lo sublime; las imágenes.
- **Hopkins, *Scientific Advertising*** (1923, dominio público): conseguir edición completa. Caps. sobre ofrecer servicio y ser específico.
- **Berger & Milkman (2012)**, qué se comparte; **Guo, Kim & Rubin (2014)**, engagement en video educativo; **Reber, Schwarz & Winkielman (2004)**, fluidez. Los tres con PDF abierto.
- **Lehne & Koelsch (2015)**: tensión y suspense, puente música–narrativa.
- **McGraw & Warren (2010)**: humor como violación benigna.
- **Kappes & Oettingen (2011)** y **Lutz et al. (2008)**: los dos paralelos empíricos de la tradición contemplativa, uno en contra y otro a favor.
- **Schopenhauer** sobre la música (descargado), **Nietzsche**, *El nacimiento de la tragedia* §1–5 (descargado), **Busoni**, *Esbozo de una nueva estética de la música* (descargado).
- **Zhuangzi**: las otras parábolas de artesanos. **Bhagavad Gita**: la acción sin apego al fruto (descargado).
- ***Corpus Hermeticum*** en traducción de dominio público, para separar lo antiguo de lo añadido por el Kybalion.

### Prioridad 3 — de pago o sin acceso: fichar por resumen o esperar

| Fuente | Por qué importa | Qué hacer |
| --- | --- | --- |
| Rubin, *The Creative Act* | Libro ancla | Ejemplar del propietario; mientras, entrevistas largas |
| Huron, *Sweet Anticipation* | Marco teórico de K-10 | Capítulo 1 si hay acceso; reseñas académicas |
| Loewenstein (1994) | Fundador de K-03 | Texto legible por biblioteca |
| Friestad & Wright (1994) | Fundador de K-09 | Ídem |
| Schloss, *Making Beats* | Etnografía académica de beatmakers: ética del sampling y del oficio | Reseñas y capítulos de muestra |
| Charnas, *Dilla Time* | Microtiming explicado con rigor | Entrevistas del autor |
| Margulis, *On Repeat* | La repetición, el agujero de K-10 | Artículos abiertos de la autora |
| Ouspensky, Gurdjieff, Nicoll | Cuarto Camino | Ejemplares del propietario |
| Inayat Khan; Godwin | Sonido y mística con rigor histórico | Verificar derechos y ediciones |
| Passman; Herstand | Referencias del negocio (ediciones de 2023 verificadas por agente) | Reseñas; mejor fuentes primarias actuales |
| Senior, Katz, Izhaki | Mezcla y mastering | Artículos abiertos de *Sound On Sound* |

---

## 3. Inventario de lo que todavía nos falta

### 3.1 Áreas pedidas y casi sin cubrir

| Área pedida | Estado | Lo que falta |
| --- | --- | --- |
| **Producción musical moderna, mezcla, mastering, diseño sonoro** | **Crítico.** El agente no pudo abrir páginas; su mapa es casi todo memoria | Rehacer el mapa B3. Fuentes abiertas probables: *Sound On Sound* (serie de síntesis y entrevistas de mezcla), documentación oficial de sonoridad de las plataformas, archivo de conferencias de Red Bull Music Academy (sin confirmar que siga en línea) |
| **Psicoacústica** | Solo localizada | Enmascaramiento, bandas críticas, fundamental ausente, precedencia: buscar un texto abierto fiable |
| **Armonía, melodía, composición** | Solo localizada | *Music Theory Online* (revista abierta) sobre loops y armonía en pop y trap |
| **Sampling** (técnica, ética y derecho) | Solo localizada | Casos legales posteriores a 2016; Schloss; licencias de servicios de samples |
| **Técnicas de productores reconocidos** | **Sin ninguna fuente primaria verificada.** El agente no dio ni una URL de entrevista | Buscar entrevistas con enlace y fecha, productor por productor, incluida la escena latina |
| **Venta y licenciamiento de beats** | Datos de mercado vía agente; contratos sin leer | Términos oficiales de las plataformas; conflictos de identificación de contenido |
| **Placements; cómo eligen beats artistas y A&R** | Casi nada: un testimonio | Es lo más cercano a lo que BeatGaler resuelve. Búsqueda dedicada de testimonios primarios |
| **Regalías fuera de EE. UU.** | Nada | SACM, SGAE, AIE y equivalentes |
| **Negociación** | Solo mapa | El efecto de la primera oferta es robusto; el del precio señuelo está disputado (verificado por agente). Leer a Fisher & Ury por resumen y a Blair Enns |
| **Marketing para productores** | Solo mapa | Sivers (abierto en su web); «mil fans verdaderos» |
| **Emociones y memoria** | Mapa bueno (A3), cero fichas | Pico-final, emoción y consolidación, nostalgia |
| **Comunicación verbal: voz, prosodia, ritmo oral** | Débil incluso en el mapa | No hay metaanálisis de pausas; un estudio de 2025 sobre velocidad de habla. Relevante porque la locución se genera con IA |
| **Imaginación** | Solo Coleridge (dos párrafos) | Simulación mental, lenguaje concreto, afantasía; y la tradición de la imaginación creadora (Corbin, Jung, Neville) como enseñanza |
| **Bloqueo creativo** | K-11 y K-13 lo tocan | Rose, Boice, Pressfield (resumen); el origen real de la anécdota de la clase de cerámica (según un agente no era cerámica sino fotografía, y no es un estudio) |
| **Desarrollo del criterio** | Hueco reconocido en K-11 | Hume, Bourdieu, «Active Listening» de DeSantis |
| **Tradición hispana** | Nada leído | Lorca (duende), Paz, Ortega (con derechos vigentes en España), Gracián (texto legal localizado), Jodorowsky |
| **Cuarto Camino** | Nada leído | Ver sección 1 |

### 3.2 Afirmaciones populares que **no** debemos usar (verificado por agentes)

- «La atención humana dura 8 segundos»: procede de un informe comercial de 2015; no hay ciencia detrás.
- «El video ideal dura 6 minutos»: el estudio original es de cursos en línea de ciencia, correlacional, y no mide aprendizaje.
- El efecto Zeigarnik como justificación de finales abiertos: un metaanálisis de 2025 no halla ventaja de memoria.
- «Cada video da un chute de dopamina»: el error de predicción de recompensa es sólido en animales; la extrapolación no.
- La oxitocina como química del storytelling: muestras pequeñas de un solo laboratorio; no replica bien.
- El efecto Kuleshov como hecho establecido: réplicas débiles.
- Estilos de aprendizaje visual/auditivo/kinestésico: sin apoyo.
- «Eres libre de…» y otras frases mágicas de persuasión: el efecto casi desaparece en los estudios de calidad.
- El precio señuelo: disputado; hay un intento de réplica fallido y una respuesta de los autores originales.
- «−14 LUFS» como regla de calidad: es una referencia de normalización, y las cifras hay que confirmarlas en la documentación oficial vigente.
- 432 Hz: el agente no lo investigó; no usar hasta hacerlo.
- La historia de la clase de cerámica de *Art & Fear* como «estudio».

Todas están desarrolladas en la sección 5 de cada mapa. Si alguna se quiere usar en un video como «mito», hay que abrir antes la fuente: el agente principal no las verificó una por una.

### 3.3 Limitaciones del método que conviene arreglar

- **PubMed Central y varios portales bloquean el acceso automático.** Muchos estudios abiertos quedaron sin leer por eso.
- **La herramienta de lectura web devuelve respuestas, no el texto.** Sirve para datos concretos; para matices y tablas hay que conseguir el texto crudo. Las fichas `EXTRACCION` deberían releerse cuando sea posible.
- **Los textos de dominio público sí se leyeron en crudo** (desde un espejo de Project Gutenberg y Perseus). Es el método más fiable y conviene explotarlo: hay una decena de textos descargados y sin leer o leídos a medias.
- **Un agente por área fue poco para música.** La próxima ronda de B3 debería dividirse en cuatro: ciencia de la música, composición, mezcla y sonido, productores.

---

## 4. Preguntas abiertas de fondo

1. **¿Fluidez o esfuerzo?** ¿Queremos que el productor sienta que aprendió o que al día siguiente pueda hacerlo? (K-06)
2. **¿Dónde está el punto medio de nuestro público?** ¿Qué da por sabido un productor de trap o reggaetón en 2026? Sin eso no se sabe qué es obvio y qué es incomprensible. (K-10)
3. **¿Qué estado de conocimiento retiene mejor: curiosidad, suspense o sorpresa?** Solo contrastable con videos propios. (K-04)
4. **¿Cuándo una mención comercial declarada suma credibilidad?** Hay un estudio localizado y sin leer. (K-09)
5. **¿Cómo se forma el gusto?** (K-11)
6. **¿Qué puede decirse con honestidad de las tradiciones esotéricas en un video?** Propuesta de esta biblioteca: presentarlas como enseñanza con fuente y dejar decidir al espectador. Es una decisión editorial del propietario. (K-15)
7. **¿Rinde como contenido el puente oficio → comunicación** (enseñar al productor cosas sobre atención y narrativa usando lo que ya hace con sonido)? Hipótesis sin probar. (`CONEXIONES.md`, 3.2)
8. `Q-001` del pipeline queda con respuesta parcial; `Q-002` a `Q-007` no reciben nada nuevo de esta ronda.

---

## 5. Siguiente ronda sugerida

1. Rehacer B3 en cuatro agentes con verificación real de páginas.
2. Leer las trece fuentes de prioridad 1.
3. Búsqueda dedicada: cómo eligen beats los artistas; términos de licencia de plataformas; regalías en el país o países que indique el propietario.
4. Sesión de preguntas al propietario sobre su propio oficio.
5. Solo entonces, decidir cómo conecta esta biblioteca con los módulos 2 y 3 del pipeline. **Esta ronda no genera guiones ni toca el sistema de hooks.**
