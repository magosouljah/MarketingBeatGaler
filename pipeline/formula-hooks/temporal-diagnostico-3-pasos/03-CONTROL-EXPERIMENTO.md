# Diagnóstico temporal, paso 3 — control del experimento A/B/C

> **TEMPORAL.** Carpeta destinada a eliminarse cuando el propietario cierre el diagnóstico. No modifica la fórmula, `REGLA.md`, las bibliotecas, `DIRECCION.md` ni producción.

**Estado:** pendientes las 30 evaluaciones humanas de Impacto y Naturalidad. No se ha hecho ninguna comparación ni se ha calificado ningún hook.

## Situaciones (nuevas, distintas de las del paso 2)

Una emoción objetivo por situación; las diez emociones de `emocion/EMOCIONES.md` aparecen una vez, igual que en el paso 2. Las situaciones se tomaron del Mapa de Deseos V3 (sección 7 y ramas E/P) antes de generar ningún hook.

| ID | Emoción | Situación |
|---|---|---|
| S01 | Ira | Un artista acepta el precio de un beat y, justo antes de pagar, ofrece una fracción de lo acordado. |
| S02 | Miedo | Herramientas de IA generan beats completos en segundos y el productor teme volverse reemplazable. |
| S03 | Ansiedad | Lleva semanas sin abrir el DAW y siente que se está quedando atrás mientras otros siguen publicando. |
| S04 | Sorpresa | Un beat que hizo en veinte minutos gusta más que otro en el que trabajó semanas. |
| S05 | Confusión | La mezcla que anoche sonaba perfecta suena mal a la mañana siguiente, sin haber cambiado nada. |
| S06 | Nostalgia | Recordar las madrugadas haciendo beats con amigos por pura diversión, antes de pensar en vender. |
| S07 | Anhelo intenso | Soñar con dejar el empleo y vivir únicamente de producir música. |
| S08 | Entusiasmo | Un artista publica una canción hecha sobre su beat y el productor la escucha por primera vez. |
| S09 | Interés | Otro productor con menos experiencia consigue placements y él no entiende qué hace distinto. |
| S10 | Curiosidad | Sigue retocando un beat sin saber si ya está terminado o si lo está empeorando. |

## Métodos y qué recibió cada generador

Los tres recibieron **el mismo texto** de situaciones y el mismo bloque de condiciones comunes (un hook por situación, ~3 s de voz, máxima intensidad y expectativa, razón concreta para seguir viendo, no resolver el video, exageración sin inventar hechos, hooks nuevos, prohibido autocalificarse). Ninguno recibió hooks, resultados ni diagnósticos de rondas anteriores, y se les prohibió abrir `experimentos/` y esta carpeta.

- **A — Fórmula completa:** leyó `REGLA.md`, `README.md`, las bibliotecas de emoción, valoración, espectador y expresión verbal, y el Mapa V3. Aplicó `M → (V + E) → (C + X[I → S → R → T]) → Hook`.
- **B — Psicología sin retórica obligatoria:** leyó solo emoción, valoración, espectador y el Mapa V3. Proceso `M → (V + E) → expectativa → C`, redacción libre. No abrió `REGLA.md` ni `expresion-verbal/`.
- **C — Generación libre:** solo situación y emoción objetivo. No leyó ningún archivo.

## Modelo y configuración

- **Modelo:** `claude-fable-5-2` (Claude Fable 5.2) en las tres generaciones; cada generador informó ese mismo ID.
- **Configuración:** un agente nuevo por método, con contexto propio y sin el historial de la sesión que preparó el experimento. Modelo heredado de la sesión. Temperatura, top_p y esfuerzo de razonamiento: valores por defecto de la plataforma, **no expuestos ni modificados** (no se puede registrar su valor numérico). Una sola pasada por método, sin regeneración.
- **Fecha:** 2026-11-22 (America/Mexico_City).

## Independencia: qué se puede afirmar y qué no

- **Sí:** los tres métodos se generaron en **tres contextos de modelo separados**, lanzados en paralelo; ninguno vio los hooks de los otros. Esto corrige el límite principal del paso 2 (una sola sesión).
- **No es independencia total:**
  1. Es **el mismo modelo** en los tres; comparten gustos y muletillas de origen.
  2. Los generadores **A y B recibieron automáticamente `AGENTS.md`** del repositorio al leer archivos. Su punto 17 resume el orden de la fórmula, incluida la notación `X[I → S → R → T]`. B informó haberlo visto y no haberlo aplicado, y no abrió las bibliotecas de expresión verbal; aun así **B conoció que existe una etapa retórica**, aunque no sus opciones. C informó no haber recibido `AGENTS.md`.
  3. C vio el nombre del proyecto en su contexto de entorno, sin reglas sobre hooks.
  4. Las restricciones de lectura se dieron por instrucción y se comprobaron con el informe de cada generador (`archivos_leidos`), no con un aislamiento técnico del disco.
  5. La sesión orquestadora sí leyó los resultados del paso 2 antes de elegir las situaciones; las eligió sin ver ningún hook nuevo.

## Mezcla ciega

Orden de creación: S01A, S01B, S01C … S10A, S10B, S10C. Barajado con `random.Random(202611222256).shuffle(records)` (Python 3); después se asignaron H001–H030.

Controles mecánicos, sin juicio de calidad: 30 IDs, 10 tríos completos, emoción coincidente con la situación, 0 textos duplicados entre sí, 0 coincidencias con las rondas anteriores (`experimentos/*.csv` y `02-HOOKS-CIEGOS.csv`, 1.063 textos normalizados), calificaciones vacías. Longitud: 9 a 14 palabras.

No hubo selección entre candidatos por parte del orquestador ni edición de ningún hook después de recibirlo. Los descartes internos de A y B (previos a su entrega, por las reglas de cada método) quedarán registrados al revelar la clave.

**Límite de secreto:** el repositorio es público. `03-CLAVE.csv` está en esta misma carpeta; el cegamiento exige **no abrirlo** antes de evaluar.

## Archivos

- [Hooks ciegos](03-HOOKS-CIEGOS.csv) — para calificar Impacto y Naturalidad.
- `03-CLAVE.csv` — método, situación, emoción, modelo, variables y razonamiento. No abrir todavía.
