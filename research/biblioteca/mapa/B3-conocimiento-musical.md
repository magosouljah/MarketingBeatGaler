# Mapa B3 — Conocimiento musical

**Biblioteca B. Estado: descubrimiento preliminar (2026-11-24).** Este mapa lo elaboró un agente secundario de búsqueda; el agente principal solo revisó su estructura, sus prioridades y sus advertencias. **No es una ficha de lectura.**

Cómo leer las marcas: `[WEB: url]` = dato visto en la web en esa sesión (a menudo a través de un resumen automático de la página, no del texto crudo); `[MEMORIA]` = conocimiento previo del modelo, **sin verificar**; «sin verificar» = no comprobado. Ningún dato marcado `[MEMORIA]` debe usarse en un video sin comprobarlo antes. Las etiquetas de respaldo se explican en [`../README.md`](../README.md).

> **Aviso de calidad:** en esta área el agente no pudo abrir páginas (solo vio títulos y direcciones en el buscador). Aquí `[WEB: …]` significa únicamente «la dirección apareció en una búsqueda»; ideas, capítulos y cifras son `[MEMORIA]` sin verificar. Es el mapa más débil de los ocho y el primero que hay que rehacer (ver `../PENDIENTES.md`).

---

## 0. Aviso de verificación (leer primero)

Esta sesión tuvo una limitación fuerte: **WebFetch fue bloqueado** (respuesta PROVENANCE_REQUIRED, permiso no concedido a tiempo) en las 5 primeras URLs que intenté y no reintenté (soundonsound.com/series/synth-secrets, learningsynths.ableton.com, makingmusic.ableton.com, redbullmusicacademy.com/lectures, support.spotify.com/…/loudness-normalization). Solo funcionó WebSearch, que devuelve **títulos y URLs, sin texto de las páginas**. Consecuencias:

- `[WEB: url]` en este informe significa **solo que la URL apareció en un resultado de búsqueda** (existe y el título coincide). **No leí el contenido** de ninguna página.
- Todo lo demás (ideas centrales, capítulos, cifras, cualidades de los autores) es `[MEMORIA]` y no está verificado hoy.
- **No pude verificar** nada sobre Sound On Sound «Inside Track», Pensado's Place, Tape Op, Genius Deconstructed, Rhythm Roulette, The Cave, ni URLs concretas de entrevistas de productores. No las invento: en la sección de productores doy *qué buscar* y marco «URL sin verificar».
- Se usaron 11 llamadas (6 fallidas por bloqueo/o sin contenido útil). Presupuesto de 25–45 no alcanzado por esa causa. El agente principal debería **re-verificar con WebFetch habilitado** los puntos marcados «PENDIENTE».

---

## 1. Panorama

El conocimiento musical útil para un productor se divide en capas con respaldo muy distinto:

1. **Psicoacústica y percepción auditiva (EMPIRICO-SOLIDO en lo básico):** enmascaramiento, bandas críticas, curvas de igual sonoridad (ISO 226), efecto de precedencia, fundamental ausente. Es la base física de la mezcla y de «por qué un 808 se oye en un móvil» (el cerebro reconstruye la fundamental a partir de los armónicos; el altavoz pequeño solo reproduce los armónicos). Fuentes duras: Moore, Fastl & Zwicker, Bregman.
2. **Expectativa, recompensa y repetición (mezcla de sólido y teórico):** Meyer → Huron (ITPRA) → Margulis. Mecanismo común: la música es predicción; el placer viene de predicciones cumplidas, retrasadas o violadas con seguridad. La dopamina anticipatoria (Salimpoor 2011) lo apoya en neurociencia, pero n pequeños.
3. **Ritmo y groove (EMPIRICO-DISPUTADO en el detalle):** U invertida de sincopación vs. groove (Witek 2014) razonablemente consistente; el papel del **microtiming** (swing, «Dilla feel») es **mixto**: muchos estudios no encuentran que desviaciones aumenten el groove, mientras que la tradición de oficio (Dilla, Questlove) y los análisis de Danielsen lo sostienen como rasgo estilístico.
4. **Armonía/melodía/forma (TEORIA-ACADEMICA + OFICIO):** libros de composición (Perricone, Pattison, Webb), análisis de corpus de pop/rock (de Clercq & Temperley; Hooktheory). Los loops modales de trap/pop están estudiados en Music Theory Online (abierta).
5. **Sampling (etnografía, derecho, historia):** Schloss, Katz, Rose, McLeod & DiCola. Fuerte en cultura y ética; el derecho cambió (Bridgeport vs. VMG v. Ciccone), así que hay que fechar todo.
6. **Mezcla/mastering (OFICIO + algo de ciencia):** Senior, Izhaki, Katz, Worrall; contrapeso científico: Winer (pruebas ciegas, mitos). La «loudness war» tiene datos propios: la normalización por plataformas la ha vuelto menos rentable, pero los umbrales exactos cambian.
7. **Identidad sonora de productores:** conocimiento OFICIO, riquísimo pero sesgado por la autonarración (los productores explican a posteriori).

Más sólido: psicoacústica clásica, ITPRA como marco, U invertida de sincopación. Más flojo: afirmaciones virales de «frecuencias que causan emociones», «el microtiming hace el groove», «la música pop se ha vuelto peor» (Serrà 2012 mide algo, pero la interpretación se discute), y casi todo en divulgación de YouTube.

---

## 2. Fuentes

### Verificadas solo en existencia (URL en resultados de búsqueda)

### Syncopation, Body-Movement and Pleasure in Groove Music — Witek, Clarke, Wallentin, Kringelbach, Vuust (2014)
- Tipo: paper (PLoS ONE) [MEMORIA]
- Credibilidad: grupo de Aarhus/Oxford, autores de referencia en groove. [MEMORIA]
- Ideas centrales: relación en U invertida entre grado de sincopación en breaks de funk/batería y (a) deseo de moverse y (b) placer; el máximo está en sincopación media. Mecanismo: hay que tener marco métrico estable (predicción) y suficiente violación para que el cuerpo «complete» el pulso. [MEMORIA]
- Capítulos: sin verificar. Existencia y acceso abierto: [WEB: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3989225/] (también hay corrección publicada: [WEB: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4581707/] — **leerla**, puede afectar a cifras)
- Respaldo: EMPIRICO-SOLIDO en la forma general; limitado: estímulos de batería sintética, oyentes mayoritariamente occidentales, sin vocal ni armonía.
- Acceso legal: texto completo libre (PMC).
- Aplicación: justifica «ni todo en el grid ni todo fuera»: hi-hats de trap que solo funcionan sobre un kick/snare claro.
- Recomendación: LEER DIRECTO.

### Measuring the evolution of contemporary western popular music — Serrà, Corral, Boguñá, Haro, Arcos (2012)
- Tipo: paper (Scientific Reports). [WEB: https://pmc.ncbi.nlm.nih.gov/articles/PMC3405292] y [WEB: https://arxiv.org/abs/1205.5651] (URLs en resultados, contenido no leído)
- Ideas centrales [MEMORIA]: análisis del Million Song Dataset 1955–2010: transiciones armónicas más restringidas, homogeneización de paleta tímbrica y aumento de sonoridad (loudness). Mecanismo propuesto: «convergencia» sobre un vocabulario común.
- Respaldo: EMPIRICO-DISPUTADO. Críticas conocidas [MEMORIA]: las métricas de timbre (MFCC sobre audio de baja resolución, sin etiquetado de género) pueden confundir producción con composición; el dataset sesga hacia lo disponible; no mide «calidad». Buscar réplicas/críticas recientes: PENDIENTE (no lo hice).
- Acceso legal: abierto (Sci. Rep./PMC y arXiv).
- Aplicación: ojo, no usar como «prueba de que todo suena igual»; sí para hablar de loudness war con datos.
- Recomendación: FICHA CON RESUMEN + leer discusión y limitaciones.

### Dissecting an Earworm — Jakubowski, Finkel, Stewart, Müllensiefen (2017)
- Tipo: paper (Psychology of Aesthetics, Creativity, and the Arts). [WEB: https://research.gold.ac.uk/19405] (repositorio Goldsmiths)
- Ideas centrales [MEMORIA]: las canciones que más se reportan como earworm son populares y sus melodías tienen contorno más común/«genérico»: intervalos pequeños, contorno ascenso-descenso, ritmo con notas repetidas y tempo relativamente rápido. Mecanismo: predictibilidad + distintividad leve.
- Respaldo: EMPIRICO-DISPUTADO (muestra de autorreporte de ~3000 personas del Reino Unido, correlacional; la popularidad confunde).
- Acceso: repositorio Goldsmiths (aparentemente abierto; no verificado el PDF).
- Aplicación: hooks: pocas notas, repetición con un giro, evitar saltos grandes en la frase central.
- Recomendación: FICHA CON RESUMEN.

### Intensely pleasurable responses to music… — Blood & Zatorre (2001) / Salimpoor et al. (2011)
- Tipo: papers (PNAS 2001; Nature Neuroscience 2011). [WEB: https://pubmed.ncbi.nlm.nih.gov/11573015/] (Blood & Zatorre); [WEB: https://www.zlab.mcgill.ca/publications/docs/salimpoor_2011_nn.pdf] (Salimpoor 2011, PDF del laboratorio)
- Ideas centrales [MEMORIA]: «escalofríos» activan circuitos de recompensa (estriado, ínsula, mesencéfalo) y se reduce actividad en amígdala; en 2011 se mide liberación de dopamina: **caudado durante la anticipación del clímax, núcleo accumbens durante el pico**. Mecanismo: el placer musical incluye un «querer» (anticipación) antes del «gustar».
- Respaldo: EMPIRICO-SOLIDO para el hecho de la implicación del sistema de recompensa; limitado: n pequeños (10 en Blood&Zatorre, 8 en Salimpoor), oyentes que elegían su propia música, «frisson» solo lo experimenta ~50–70 % de la gente [MEMORIA].
- Acceso legal: PDF en laboratorio (zlab.mcgill.ca) y resumen PubMed.
- Aplicación: construir el drop como tensión-anticipación (risers, silencio previo), no solo «hacerlo fuerte».
- Recomendación: FICHA CON RESUMEN; leer Salimpoor directo.

### The Geometry of Musical Rhythm — Godfried Toussaint (2013 libro) y «The Euclidean Algorithm Generates Traditional Musical Rhythms» (2005)
- Tipo: libro + paper (Bridges). [WEB: https://cgm.cs.mcgill.ca/~godfried/publications/banff.pdf] (PDF alojado en McGill por el autor, 2005, título coincide con el paper de Bridges: [WEB: https://archive.bridgesmathart.org/2005/bridges2005-47.html]); libro: [WEB: https://en.wikipedia.org/wiki/The_Geometry_of_Musical_Rhythm] (solo ficha enciclopédica)
- Ideas centrales [MEMORIA]: muchos ritmos tradicionales (tresillo, cinquillo, clave son, bembé, etc.) son «euclidianos»: distribuyen k pulsos en n pasos lo más uniformemente posible. Medidas de «síncopa», distancia de edición entre ritmos y propiedad de «iamb vs. trochee». Mecanismo: ritmos casi regulares pero con asimetría = cuadro mínimo de tensión/regularidad (coincide con Witek).
- Respaldo: TEORIA-ACADEMICA (matemática sólida; que explique preferencia perceptiva está menos probado).
- Acceso: paper del autor en abierto (McGill); libro de pago.
- Aplicación: E(3,8) = tresillo = base de dembow/trap; generar patrones de hi-hat con E(k,16).
- Recomendación: LEER DIRECTO el PDF de 2005.

### Dem Bow, Dembow, Dembo — Wayne Marshall (varios textos)
- Tipo: ensayo académico/periodístico. Aparecen: [WEB: https://scalar.usc.edu/works/turbofolk/media/dembow-rhythm] (recurso USC), un PDF de Scribd (no enlazo, copia no autorizada), [WEB: https://college.berklee.edu/news/what-is-dembow-tracing-the-roots-of-a-global-phenomenon] (Berklee, divulgación), y entradas de Harvard tagteam que indexan «Dembow Complex», «Desperately Seeking Dembow» (blog de Marshall/Wax Poetics).
- Ideas centrales [MEMORIA]: el dembow nace de «Dem Bow» de Shabba Ranks (1990) y del riddim de Bam Bam (Steely & Clevie) y es parte de una cadena Jamaica–Panamá–Puerto Rico–Dominicana; es un patrón «3+3+2» en el kick/snare que reaparece en reggaetón, dancehall, perreo, y en parte del trap latino. Mecanismo: el tresillo como unidad de circulación diaspórica.
- Respaldo: TEORIA-ACADEMICA/OFICIO histórico. Texto exacto de los artículos de Marshall: PENDIENTE verificar vía wayneandwax.com.
- Aplicación: contenido en español sobre «de dónde viene el reggaetón» con mecanismo rítmico.
- Recomendación: LEER DIRECTO (Marshall) cuando haya acceso a la URL; Berklee como entrada rápida.

### Everyday Tonality / Everyday Tonality II — Philip Tagg (2009/2014)
- Tipo: libro. [WEB: reseña Cambridge https://cambridge.org/core/journals/popular-music/article/everyday-tonality-…] (existe; reseña de Popular Music). Las otras URLs de la búsqueda son copias no autorizadas (hugoribeiro.com.br, Scribd): **no usar**.
- Ideas centrales [MEMORIA]: musemas (unidades mínimas de significado musical), análisis por hipótesis intersubjetiva (IOCM, «interobjective comparison material»): se compara una pieza con otras que comparten el rasgo y se mira el contexto cultural. Mecanismo: el significado musical es convención aprendida, no universal.
- Acceso legal: PENDIENTE verificar tagg.org (mi memoria: el autor ha publicado material en abierto en tagg.org, no verificado hoy).
- Respaldo: TEORIA-ACADEMICA.
- Recomendación: FICHA CON RESUMEN; leer capítulos abiertos tras confirmar.

### Red Bull Music Academy — archivo de lecturas
- Tipo: archivo de charlas en vídeo. Resultados de búsqueda indican que RBMA **liberó todo su archivo de lecciones y entrevistas** al cerrar: [WEB: https://factmag.com/2019/10/29/red-bull-music-academy-shares-free-digital-content-archive-ahead-of-closure], [WEB: https://www.electronicbeats.net/the-feed/explore-20-years-fascinating-red-bull-music-academy-lectures-archive/], [WEB: https://en.wikipedia.org/wiki/List_of_Red_Bull_Music_Academy_lecturers] (lista de ponentes), [WEB: https://www.redbullmusicacademy.com/] (portal, no pude cargarlo).
- Estado actual (2026) del archivo: PENDIENTE verificar (los títulos de prensa son de 2018–2019; también puede haber copias en YouTube/Apple TV: [WEB: https://tv.apple.com/no/show/red-bull-music-academy-lectures/umc.cmc.6n79i98aa0h1t89e5gf9779ee]).
- Respaldo: OFICIO. Lecturas de gran interés [MEMORIA, sin URL]: J Dilla-adyacentes (Pete Rock, DJ Premier, Madlib, Questlove), Just Blaze, Hudson Mohawke, Kaytranada, Flying Lotus, Timbaland. Buscar títulos exactos con WebFetch.
- Recomendación: LEER DIRECTO (ver sección 3).

### Making Music: 74 Creative Strategies for Electronic Music Producers — Dennis DeSantis (Ableton, 2015)
- Tipo: libro. [WEB: https://musicradar.com/news/free-ableton-book-download-74-creative-strategies-for-electronic-music-producers-for-free] (noticia de 2020 de que es gratis), [WEB: https://happymag.tv/making-music-in-isolation-upskill-yourself-with-abletons-free-book/], [WEB: https://xlr8r.com/features/qa-abletons-dennis-desantis/] (entrevista al autor), [WEB: https://cdm.link/non-oblique-strategies-author-tells-us-discipline-making-music/] (entrevista en CDM).
- Ideas centrales [MEMORIA]: estrategias tipo «Estrategias Oblicuas» pero **disciplinadas**: restricciones, terminar, trabajar con patrones, etc. Mecanismo: la restricción reduce la parálisis de opciones (conecta con la sección g).
- Acceso: la noticia de MusicRadar dice que se liberó gratis en 2020. Enlace exacto de descarga: PENDIENTE (el sitio makingmusic.ableton.com no se pudo abrir).
- Respaldo: OFICIO.
- Recomendación: LEER DIRECTO (breve; 74 capítulos cortos).

### Ableton Learning Music / Learning Synths
- Tipo: web interactiva gratuita. [WEB: https://www.ableton.com/es/blog/learn-music-in-your-browser] (blog oficial de Ableton, indica en español que es en el navegador), [WEB: https://direct.djmag.com/tech/ableton-drop-new-learning-music-website]. Learning Synths: URL no abierta, existencia confirmada solo por memoria.
- Respaldo: OFICIO + pedagogía bien diseñada.
- Recomendación: FICHA (no hay mucho que leer; sirve de referencia y para ver «cómo se enseña»).

### Synth Secrets — Gordon Reid (Sound On Sound, 1999–2004)
- Tipo: serie de artículos (63 partes según pidió el dueño). Resultados: [WEB: https://www.soundonsound.com/series/synth-secrets], [WEB: https://www.soundonsound.com/synthesizers/synth-secrets], [WEB: https://github.com/rupa/synth-secrets] (repositorio de terceros que reúne la serie: **no usar como fuente legal**, podría ser copia no autorizada).
- Estado: la serie parece estar en soundonsound.com/series/synth-secrets con varias páginas de listado (page=2, page=3), lo que sugiere abierta sin muro, pero **no abrí artículos**. El número de partes (63) y si todo es gratis: PENDIENTE.
- Ideas centrales [MEMORIA]: de la acústica de las ondas (Fourier) a síntesis sustractiva, FM, aditiva, físicas y de modelado, emulando instrumentos (campanas, cuerdas, percusión), con mecanismo.
- Respaldo: OFICIO + física de sonido.
- Recomendación: LEER DIRECTO (partes sobre envolventes, filtros, percusión sintética: base de 808/kicks/snares).

### Sin verificar en absoluto (solo MEMORIA, todo PENDIENTE)
Marca: ninguna de estas entradas fue consultada en la web hoy.

- **Huron, *Sweet Anticipation* (MIT Press, 2006)** — ITPRA: Imagination, Tension, Prediction, Reaction, Appraisal. Mecanismo: distintas respuestas emocionales según fase; la sorpresa de menos de 1 s activa reacción rápida; luego valoración lenta (por eso risa/escalofrío). EMPIRICO-DISPUTADO/TEORIA-ACADEMICA. De pago. Recomendación: LEER DIRECTO caps. sobre expectativa (sin verificar numeración). Huron, *Voice Leading* (2016): reglas de conducción de voces derivadas de principios de percepción (fusión, enmascaramiento); relaciona directamente con Bregman. TEORIA-ACADEMICA.
- **Meyer, *Emotion and Meaning in Music* (1956)**: emoción por inhibición de tendencias; origen de toda la línea de expectativa. TEORIA-ACADEMICA (influye, no se probó por completo).
- **Margulis, *On Repeat* (2014)**: repetición hace que la música se perciba como «música» (ilusión speech-to-song de Deutsch); participación imaginada. Respaldo mixto: experimentos pequeños, ideas más teóricas. Leer cap. sobre «Speech to song».
- **Bregman, *Auditory Scene Analysis* (MIT Press, 1990)**: principios de agrupamiento (proximidad en frecuencia/tiempo, destino común, continuidad) → qué sonidos se fusionan o se segregan. Base científica de arreglo (dos partes con el mismo ritmo y octava se funden) y mezcla (panorama, enmascaramiento). EMPIRICO-SOLIDO como paradigma. De pago; la web de McGill alberga material (URL no verificada).
- **Moore, *An Introduction to the Psychology of Hearing*; Fastl & Zwicker, *Psychoacoustics*; Helmholtz, *On the Sensations of Tone***: referencia técnica para bandas críticas (~ERB), enmascaramiento, fundamental ausente (residue pitch), curvas ISO 226 (la sensibilidad cae en graves a bajo volumen: por eso la mezcla cambia al subir el volumen). EMPIRICO-SOLIDO. Helmholtz (1863/1877, trad. Ellis) es dominio público; copia en Internet Archive PENDIENTE.
- **Sethares, *Tuning, Timbre, Spectrum, Scale***: relación entre timbre y escala (la disonancia depende del espectro). TEORIA-ACADEMICA con base física. PENDIENTE verificar si Sethares aloja PDF.
- **Levitin, *This Is Your Brain on Music* (2006)**: DIVULGACION; usar con cuidado (algunas afirmaciones han sido criticadas).
- **Charnas, *Dilla Time* (2022)**: historia y análisis del feel de J Dilla (bateo «borracho», cuantización, MPC). Libro de periodismo musical con entrevistas y análisis de Charnas; **leer** para el mecanismo (offset de kick/snare, swing de MPC a 62 %, etc. — cifras sin verificar). OFICIO/DIVULGACION. De pago.
- **Danielsen, *Musical Rhythm in the Age of Digital Reproduction* (2010, ed.)** y trabajos sobre «beat bins» y microritmo en D'Angelo/Dilla/funk: tesis de que la ejecución crea «zonas» de onset en vez de puntos. TEORIA-ACADEMICA. Por lo que mostró la búsqueda: [WEB: https://academic.oup.com/book/56186/chapter/443058577] aparece (no sé qué capítulo); y papers de microtiming en [WEB: https://pmc.ncbi.nlm.nih.gov/articles/PMC5050221], [WEB: https://pmc.ncbi.nlm.nih.gov/articles/PMC4542135], [WEB: https://pmc.ncbi.nlm.nih.gov/articles/PMC6025871], [WEB: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016.01487/pdf] y [WEB: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2015.01232/pdf] **no leídos**: las usé como candidatos para la tesis «el microtiming a veces no aumenta el groove» (Davies, Madison, Senn; Frühauf 2013; Câmara et al.), pero no verifico que sean esos.
- **Schloss, *Making Beats* (2004)**: etnografía de beatmakers de Nueva York (sample-based): la ética del digging, lo «obscuro» como capital, el beat como colaboración con ancestros del sample. TEORIA-ACADEMICA/etnografía. De pago.
- **Katz, *Capturing Sound* (2004/2010) y *Groove Music* (2012)**; **Rose, *Black Noise* (1994)**; **McLeod & DiCola, *Creative License* (2011)**: historia tecnológica, estética de la comunidad y economía/derecho del sampling (Grand Upright 1991 «thou shalt not steal»; Bridgeport v. Dimension 2005 «get a license»; VMG Salsoul v. Ciccone, 9º Circuito 2016, de minimis: casos importantes pero **estado del derecho dividido por circuito: verificar con abogado**). OFICIO jurídico / TEORIA-ACADEMICA.
- **Senior, *Mixing Secrets for the Small Studio***: libro con sitio de apoyo «cambridge-mt.com» con audio multipista descargable y artículos «Mix Rescue» (SOS). Usable y bien valorado como referencia de oficio. Sitio y estado: PENDIENTE.
- **Izhaki, Owsinski, Moylan, Katz *Mastering Audio*, Zagorski-Thomas, Zak, Burgess, Moorefield, Seabrook *The Song Machine*, Eno 1979 «The Studio as Compositional Tool», Q on Producing**: referencias estándar, todas de pago salvo el texto de Eno (circula; verificar copia legal). Seabrook: DIVULGACION con entrevistas; sirve para «track and hook» y «melodic math» de Max Martin.
- **Dan Worrall (FabFilter, YouTube)**: vídeos técnicos rigurosos sobre saturación, aliasing, dither, EQ de fase lineal; mecanismo antes que receta. OFICIO+DSP. URL concreta PENDIENTE.
- **Ethan Winer (*The Audio Expert*, 2012; sitio ethanwiner.com)**: pruebas ciegas contra mitos (cables, 96 kHz...). Es un corrector útil para el exceso de supersticiones. Respaldo: EMPIRICO (aunque sesgado a favor del «no se oye»).
- **Hooktheory (Trends / «Theorytab»), de Clercq & Temperley (2011, «A corpus analysis of rock harmony», Popular Music)**: estadística de progresiones en rock; «Millennial Whoop» (patrón melódico alternando 5 y 3 con salto a 6 en pop 2010s): origen divulgativo; verificar si hay estudio formal PENDIENTE.
- **Music Theory Online (mtosmt.org)**: revista abierta de la Society for Music Theory; busca Spicer, Nobile (armonía de pop/rock/loops). No abrí ni un artículo.
- **Loudness (LUFS)**: Spotify publica ayuda para artistas [WEB: https://support.spotify.com/artists/article/loudness-normalization/] (existe, no leí). [MEMORIA]: Spotify normaliza a −14 LUFS integrado por defecto (con −11 y −19 como otras opciones en ajustes premium); Apple Music/Sound Check ~−16 LUFS; YouTube ~−14 LUFS (solo atenúa, no sube). **Todas estas cifras están desactualizadas hasta confirmar**. Ian Shepherd (Production Advice, «Dynamic Range Day») y AES TD1008: PENDIENTE.

### Productores: qué buscar (todas las URLs PENDIENTES)
No puedo dar URL verificada de ninguna entrevista. Para cada nombre, el tipo de fuente primaria a localizar (cada uno requiere búsqueda concreta con WebFetch):
- Hip-hop clásico: J Dilla (entrevistas de Stones Throw; *Dilla Time*), Madlib (RBMA, *Rhythm Roulette*), Pete Rock/DJ Premier (RBMA), RZA (*The Wu-Tang Manual*, RBMA), Dr. Dre, Timbaland (RBMA), Pharrell/The Neptunes (Rolling Stone/RBMA), Kanye (documental *Jeen-Yuhs*, entrevistas con Rick Rubin).
- Trap/Atlanta: Metro Boomin, Southside, Zaytoven, Pi'erre Bourne, Wheezy, Tay Keith, Murda Beatz, Mike WiLL, Boi-1da, 40 (Noah Shebib), Hit-Boy, Mustard: fuentes en Genius «Deconstructed», Kenny Beats «The Cave», Rhythm Roulette, Complex, Billboard, SOS Inside Track (40, Mustard, Hit-Boy). Todo PENDIENTE.
- Latino: Tainy, Ovy on the Drums, Bizarrap (Bzrp Music Sessions), Sky Rompiendo; fuentes: entrevistas Billboard Latin/Rolling Stone en español, charlas Berklee; PENDIENTE.
- Pop/Alt: Finneas, Jack Antonoff (SOS), Flying Lotus, Kaytranada, SOPHIE (RBMA), Skrillex.

---

## 3. Top 8 para lectura directa (ordenado; todos sujetos a verificación de acceso)

1. **Witek et al. 2014** — [PMC3989225](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3989225/) y su corrección [PMC4581707](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4581707/). Leer completo; es el mejor puente de ciencia a «cómo programar un hi-hat». Tiene mecanismo y crítica incorporada.
2. **Toussaint 2005** — [PDF McGill](https://cgm.cs.mcgill.ca/~godfried/publications/banff.pdf). Ritmos euclidianos y tresillo; relación directa con dembow/trap.
3. **Salimpoor et al. 2011** — [PDF laboratorio](https://www.zlab.mcgill.ca/publications/docs/salimpoor_2011_nn.pdf). Dopamina anticipatoria; fundamento científico del «build».
4. **Gordon Reid, *Synth Secrets*** (soundonsound.com/series/synth-secrets). Partes sobre percusión sintetizada y envolventes; confirmar acceso gratis y número de partes.
5. **Wayne Marshall sobre dembow** (wayneandwax.com; también el artículo de Berklee [enlace](https://college.berklee.edu/news/what-is-dembow-tracing-the-roots-of-a-global-phenomenon) como entrada). Alto valor para público hispano.
6. **RBMA lectures archivo** — elegir 6–8 charlas (Dilla-círculo, Madlib, Just Blaze, Timbaland...). Confirmar si el archivo sigue en línea.
7. **Serrà 2012** — [PMC3405292](https://pmc.ncbi.nlm.nih.gov/articles/PMC3405292) con crítica: buen ejemplo de «afirmación famosa que hay que cuestionar».
8. **DeSantis, *Making Music*** — buscar enlace gratuito oficial de Ableton; breve, orientado a terminar canciones.

(Los libros de pago que añadiría con presupuesto: Huron *Sweet Anticipation*, Schloss *Making Beats*, Charnas *Dilla Time*, Senior *Mixing Secrets*.)

---

## 4. Conexiones detectadas

- **Expectativa**: Meyer → Huron (ITPRA) → Witek (U invertida de sincopación) → Salimpoor (dopamina anticipatoria) → Margulis: todos dicen que el placer = **predecibilidad calibrada + violación segura**. Es el mismo mecanismo que «curiosity gap» en la biblioteca A (comunicación): tensión sin cierre.
- **Toussaint ↔ Marshall ↔ Witek**: el tresillo/dembow es un ritmo euclidiano con síncopa media; da explicación matemática de por qué se esparce.
- **Bregman ↔ mezcla (Senior/Izhaki)**: la «separación» de elementos en una mezcla = segregación de flujos auditivos; el enmascaramiento (Moore, Fastl/Zwicker) es el lado de la audición.
- **Fundamental ausente ↔ 808**: explica por qué se «oye» en un móvil (armónicos); conecta con saturación (Worrall).
- **DeSantis ↔ parálisis de opciones (g)** ↔ restricciones creativas (Eno, Estrategias Oblicuas).
- **Schloss ↔ Gurdjieff (notas del dueño)**: la ética del digging como disciplina de atención («trabajar sobre uno mismo» a través del oficio). Es una conexión interpretativa mía, no de la fuente.

---

## 5. Controversias y afirmaciones populares SIN buen respaldo

- «El microtiming/swing de Dilla **aumenta el groove**»: hallazgos **mixtos**; varios experimentos no encuentran efecto positivo o encuentran que los desvíos grandes lo reducen. Mantener como OFICIO + hipótesis estilística, no como hecho (candidatos a leer para confirmarlo: los PMC de la sección 2).
- «Toda la música pop se ha vuelto homogénea» (Serrà 2012): medidas indirectas, críticas sobre MFCC y muestras.
- «Frecuencias/432 Hz curan o son más musicales»: sin respaldo científico fiable (de memoria; no busqué).
- «Hay que masterizar a −14 LUFS»: es una **referencia de normalización**, no una regla de calidad; y las plataformas cambian valores. Verificar docs oficiales.
- «La loudness war aumenta las ventas»: no verificado; no encontré estudio en esta sesión.
- Levitin y otros divulgadores: afirmaciones neurocientíficas simplificadas («la música activa dopamina» = cierto en el hecho, pero n pequeños).
- «Escalofríos = calidad musical»: solo ~mitad de oyentes los experimenta; la respuesta depende de la personalidad (apertura a la experiencia), según la literatura que recuerdo.
- «Millennial Whoop» y cualquier «fórmula del hit»: análisis de corpus **descriptivos**, no causales.

## 6. Vacíos

- **No verifiqué** contenidos de ningún sitio: WebFetch bloqueado. Todo el contenido interno es memoria.
- Pendiente: lista y URLs de entrevistas de productores (sección productores), Sound On Sound Inside Track (muro de pago parcial?), Tape Op (registro), Pensado's Place, Mix with the Masters, Kush Audio, Genius Deconstructed, The Cave, Rhythm Roulette.
- Pendiente: estudios sobre «option paralysis» / exceso de plugins en producción (no los busqué; sospecho que no hay estudio específico de producción; sí hay literatura general de «choice overload» —Iyengar & Lepper 2000, con réplicas mixtas / metaanálisis de Scheibehenne 2010, [MEMORIA]), y Adam Bell *Dawn of the DAW*, Théberge *Any Sound You Can Imagine*, etnografías de home studio: sin verificar.
- Pendiente: estudio sobre loudness y ventas/popularidad; AES TD1008; docs YouTube/Apple.
- Pendiente: textos abiertos de Tagg, Sethares, Helmholtz (IA).
- Pendiente: casos legales de sampling actuales (después de 2016), Tracklib, WhoSampled, documentales (*Copyright Criminals*, *Scratch*, *Sample This*, *Our Vinyl Weighs a Ton*).
- **Descubrimientos extra** (de memoria, sin URL): la técnica de «reverse engineering» de samples en MPC (Schloss), literatura sobre «beat bins» de Danielsen, y la revista *Dancecult* (acceso abierto) para cultura de la electrónica — sin verificar.
