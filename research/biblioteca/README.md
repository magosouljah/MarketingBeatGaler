# Biblioteca de conocimiento — MarketingBeatGaler

**Creada:** 2026-11-24. **Estado:** primera ronda (mapa completo de áreas + primeras lecturas directas) y selección de libros para adquirir. **No contiene guiones ni fórmulas.**

> **Prioridad vigente (2026-11-24, decisión del propietario):** antes de seguir leyendo y extrayendo principios, construir la biblioteca. El propietario conseguirá los libros de [`libros/`](libros/README.md) y después se estudiarán a fondo. Las fichas y principios existentes se conservan.

Sirve para dos cosas: tener **algo extraordinario que decir** a un productor musical (Biblioteca B) y saber **cómo decirlo** (Biblioteca A). Es materia prima para el módulo 1 del [pipeline](../../pipeline/README.md); no sustituye al Mapa de Deseos, al sistema de hooks ni a ninguna decisión de producto.

## Cómo está organizada

| Capa | Dónde | Qué contiene | Quién la escribió |
| --- | --- | --- | --- |
| 1. Mapa bibliográfico | [`mapa/`](mapa/) | Ocho mapas por área con ~230 fuentes localizadas, su respaldo, su acceso legal y qué merece lectura directa | Agentes secundarios de búsqueda (preliminar) |
| 2. Fichas de fuente | [`fichas/`](fichas/) | Una ficha por fuente **realmente leída**: qué dice, por qué importa, límites, nivel de acceso | Agente principal |
| 3. Conocimiento sintetizado | [`conocimiento/`](conocimiento/) | Un archivo por principio: mecanismo, condiciones, cuándo falla, qué lo contradice, fuentes | Agente principal |
| 4. Conexiones | [`CONEXIONES.md`](CONEXIONES.md) | Cómo se tocan las disciplinas: mismo mecanismo con otro nombre, tensiones, cadenas | Agente principal |
| 5. Pendientes | [`PENDIENTES.md`](PENDIENTES.md) | Lecturas priorizadas, vacíos, preguntas abiertas y lo que se necesita del propietario | Agente principal |
| 6. Selección de libros | [`libros/`](libros/README.md) | Qué libros conseguir, por disciplina: 62 imprescindibles en tres tandas de compra, complementarios y descartados con motivo. **Ninguno leído todavía** | Agentes secundarios + decisión del agente principal |
| Índice | [`INDICE.csv`](INDICE.csv) | Una fila por ficha y por principio, para buscar sin abrir todo | — |

Las fuentes originales que ya estaban en el repo siguen en [`../psychology/sources/`](../psychology/sources/) (Atkinson ×2 y el Mapa de Deseos V3). No se duplicaron: las fichas y principios las enlazan.

## Cómo recuperar algo sin leer toda la biblioteca

1. **Por pregunta** («¿cómo sostengo la atención a mitad del video?»): abrir [`conocimiento/README.md`](conocimiento/README.md), que lista cada principio en una línea, y leer solo el `K-…` que toque.
2. **Por fuente** («¿qué decía Poe?»): `grep -i poe research/biblioteca/INDICE.csv` y abrir su ficha.
3. **Por tema amplio** («¿qué hay sobre regalías?»): abrir el mapa del área (`mapa/B4-…`) y buscar la palabra.
4. **Por nivel de confianza:** filtrar la columna `respaldo` de `INDICE.csv`.

## Etiquetas

**Respaldo** (qué tan firme es lo que afirma la fuente):

| Etiqueta | Significa |
| --- | --- |
| `EMPIRICO-SOLIDO` | Estudios replicados o metaanálisis |
| `EMPIRICO-DISPUTADO` | Un estudio, hallazgos mixtos o réplicas fallidas |
| `TEORIA-ACADEMICA` | Modelo con apoyo parcial |
| `OFICIO` | Experiencia profesional demostrable, sin estudio controlado |
| `TEXTO-HISTORICO` | Observación anterior a la psicología experimental moderna: aporta un modelo, no una demostración |
| `FILOSOFICO` | Argumento o postura, no medición |
| `ESOTERICO` | Enseñanza de una tradición espiritual o hermética. **Nunca se presenta como hecho científico** |
| `DIVULGACION` | Libro popular que resume a otros |
| `FUENTE-OFICIAL` | Documento de un organismo público. Fiable para lo que describe, en su jurisdicción y a su fecha |

**Acceso** (qué leímos de verdad):

| Etiqueta | Significa |
| --- | --- |
| `DIRECTA` | El agente principal leyó el texto original (la ficha dice qué capítulos) |
| `EXTRACCION` | Se procesó el texto original completo con una herramienta que devuelve respuestas sobre la página, no el texto crudo. Fiable para datos concretos; puede perder matices |
| `RESUMEN` | Solo abstract, reseña, índice o entrevistas. **El libro no se leyó** |
| `MAPA` | Solo localizada por un agente secundario; ver `mapa/` |

## Reglas de esta biblioteca

1. **No fingir lecturas.** Cada ficha declara su acceso. Si una idea viene de un resumen, lo dice.
2. **No inventar páginas.** Las ediciones digitales usadas no conservan paginación: se cita capítulo y sección.
3. **Citas cortas.** Máximo una cita breve por fuente; el resto se parafrasea.
4. **Separar siempre:** lo que dice el autor / lo que interpretamos / lo que suponemos para productores. Las aplicaciones a productores son **hipótesis nuestras** salvo que se indique lo contrario, igual que en `pipeline/1-investigacion/`.
5. **Preguntar por qué.** Cada principio responde: por qué funciona, cuándo funciona, cuándo deja de funcionar, qué lo contradice.
6. **Un principio no es una regla de guion.** Nada de aquí obliga a una estructura; el sistema de hooks vigente (`pipeline/hooks/`) no se toca.
7. **Lo esotérico y lo filosófico se conservan como enseñanza**, con su vocabulario, y se señala si existe o no un paralelo empírico honesto.
8. **Sin copias piratas.** Solo dominio público, acceso abierto o web del autor/editor. Los libros de pago se fichan por resumen hasta que el propietario aporte su copia.

## Cómo añadir una fuente

1. Buscarla en `mapa/`; si no está, añadirla al mapa de su área.
2. Leerla (o la parte que importa) y crear `fichas/F-0NN-nombre.md` con la plantilla de [`fichas/README.md`](fichas/README.md).
3. Añadir su fila a `INDICE.csv`.
4. Si cambia, refuerza o contradice un principio, **editar ese `K-…`** en vez de crear uno nuevo; crear uno nuevo solo si el mecanismo es distinto.
5. Si abre una pregunta, anotarla en `PENDIENTES.md`.

Identificadores: `F-…` fichas, `K-…` principios. No chocan con los del pipeline (`EV`, `Q`, `M`, `N`, `H`, `G`, `X`, `P`, `A`).
