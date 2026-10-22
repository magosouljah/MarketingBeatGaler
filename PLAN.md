# Plan — Sistema de videos para BitGaler

## Objetivo

Construir un sistema repetible para crear videos verticales de **30–60 segundos** para dos cuentas distintas, usando directamente el enfoque descrito en el video de Claude Code:

**research → scripting → editing → design → motion graphics → review → feedback → mejora del sistema**

La prioridad no es automatizar todo lo antes posible. La prioridad es conseguir un estándar visual y editorial alto, y solo después escalarlo.

---

## Las dos cuentas

### Cuenta 1 — BitGaler oficial

**Objetivo:** vender y posicionar BitGaler.

**Videos:**
- anuncios de producto;
- demos;
- features;
- casos de uso;
- UI en acción.

**Sensación:**
- premium;
- limpia;
- minimalista;
- moderna;
- tipo Apple / startup grande;
- todo debe verse intencional, caro y profesional.

### Cuenta 2 — Productor / contenido

**Objetivo:** atraer productores dando valor y convertir parte de esa audiencia hacia BitGaler / Telegram.

**Videos:**
- tips;
- plugins;
- páginas útiles;
- recursos;
- problemas comunes;
- descubrimientos;
- BitGaler integrado de forma natural.

**Sensación:**
- rápida;
- útil;
- entretenida;
- humana;
- nativa de TikTok / Reels;
- menos anuncio y más “esto me sirve / quiero seguir esta cuenta”.

### Regla común

No usar comedia absurda en ninguna de las dos cuentas.

El motor técnico puede compartirse, pero el gusto, los hooks, formatos, referencias, assets y feedback de cada cuenta deben mantenerse separados.

---

# Fase 0 — Completar la especificación antes de construir

Antes de programar el sistema completo, convertir el video de referencia en una especificación ejecutable y resolver únicamente los huecos que la transcripción no deja claros.

El sistema descrito en el video se divide en:

1. Research
2. Scripting
3. Editing
4. Design
5. Motion graphics
6. Review
7. Feedback / mejora de las instrucciones

## 0.1 Verificar el sistema web → video del creador

La transcripción menciona una herramienta que suena como:

> “a free tool from HeyGen called Hyperframes which turns a web page into real video”

Antes de elegir herramientas:

- confirmar el nombre exacto;
- entender exactamente qué función cumple;
- confirmar cómo convierte una página web en video;
- confirmar cómo se sincronizan animaciones con el video;
- determinar cómo reproduciremos esa misma función con Codex.

**No elegir un reemplazo solo para poder continuar.**

## 0.2 Definir cómo obtendremos videos de referencia

El creador recomienda estudiar videos del nicho que rindieron mejor de lo habitual para su propio canal.

Necesitamos definir cómo obtener para cada referencia, cuando sea posible:

- video;
- views;
- canal / creador;
- rendimiento habitual del canal;
- transcripción;
- frames o screenshots relevantes.

La intención es detectar **outliers**, no simplemente videos con muchas views.

## 0.3 Definir implementación en Codex

Traducir las funciones del sistema del video a nuestra implementación:

- research;
- scripting;
- editing;
- design;
- motion graphics;
- review;
- feedback.

Definir también qué trabajo puede dividirse entre subagentes y qué información comparte cada uno.

## Gate de Fase 0

No continuar por inercia.

La fase termina cuando exista una especificación suficientemente clara de cómo ejecutar cada bloque sin rellenar huecos con decisiones arbitrarias.

---

# Fase 1 — Research System

Basado directamente en la parte del video donde el creador indica que Claude debe estudiar los mejores videos del tema, extraer sus hooks y formatos, y guardarlos en una biblioteca reutilizable.

## Proceso

1. Encontrar videos relevantes del nicho.
2. Priorizar videos que hayan superado el rendimiento normal de su propio canal.
3. Analizar sus hooks.
4. Analizar su formato.
5. Guardar patrones reutilizables.

## Cuenta 1

Investigar referencias útiles para:

- anuncios de producto;
- demos;
- features;
- UI;
- casos de uso.

Las referencias deben ser compatibles con el estándar visual definido para la cuenta: premium, limpio, minimalista y moderno.

## Cuenta 2

Investigar referencias útiles para:

- tips de producción;
- plugins;
- recursos;
- páginas útiles;
- problemas;
- descubrimientos.

Aquí interesa especialmente estudiar:

**hook → retención → entrega de valor**

No anuncios tradicionales.

## Salidas

- `HOOK_LIBRARY_ACCOUNT_1`
- `FORMAT_LIBRARY_ACCOUNT_1`
- `HOOK_LIBRARY_ACCOUNT_2`
- `FORMAT_LIBRARY_ACCOUNT_2`

## Gate

No automatizar scripts hasta comprobar que el sistema realmente entiende qué hizo funcionar a las referencias y no se limita a describirlas superficialmente.

---

# Fase 2 — Scripting Skill

El video insiste en que un video visualmente bueno no funcionará si el guion es malo.

La Skill debe utilizar:

**videos ganadores + hook library + format library + objetivo de la cuenta → script**

## Cuenta 1

El guion puede estructurarse alrededor de:

**problema / interés → BitGaler → producto funcionando → beneficio**

Debe respetar el posicionamiento premium de la cuenta.

## Cuenta 2

El guion debe partir de valor para el productor:

**algo útil → valor → más valor → BitGaler cuando tenga sentido**

BitGaler no debe sentirse forzado en cada video.

## Salida

Dos perfiles separados de scripting, uno por cuenta.

---

# Fase 3 — Editing Skill

Basado en el flujo del video:

**raw footage → Whisper → timestamps por palabra → selección de tomas → FFmpeg**

## 3.1 Transcripción

Usar Whisper para crear timestamps por palabra.

## 3.2 Limpieza de tomas

El sistema debe poder identificar:

- errores;
- reinicios de una frase;
- silencios innecesarios;
- retakes.

La regla descrita en el video es conservar la última toma limpia de cada línea y eliminar el resto.

## 3.3 Corte

Usar FFmpeg para ejecutar físicamente los cortes.

El sistema también debe listar qué eliminó.

Ejemplo:

```text
00:03–00:05 retake
00:12–00:14 repeated phrase
```

## Material adicional

El sistema debe poder recibir también screen recordings o video files, tal como se describe en el video.

Esto será especialmente importante para demos y UI de BitGaler.

---

# Fase 4 — Design System

El video advierte que pedir gráficos sin un plan genera resultados genéricos tipo PowerPoint.

Por eso no se deben generar gráficos todavía.

## Proceso

1. Reunir videos, screen recordings y screenshots que realmente representen el estándar que buscamos.
2. Analizar qué hace que funcionen.
3. Convertir esos hallazgos en reglas de diseño.

El análisis debe observar al menos las cosas que el propio video menciona, como:

- cómo entra el texto;
- cómo se mueve;
- cómo una escena pasa a la siguiente;
- cómo están construidos los gráficos.

## Salidas

- `ACCOUNT_1_DESIGN_GUIDELINES`
- `ACCOUNT_2_DESIGN_GUIDELINES`

Las dos cuentas deben tener reglas visuales independientes.

---

# Fase 5 — Beat Map

Antes de construir gráficos, crear un beat map.

El video lo define como una lista de cada idea del guion y lo que aparece en pantalla mientras se dice.

Ejemplo:

```text
00:00–00:03
Idea: problema
Screen: X

00:03–00:07
Idea: explicación
Screen: Y

00:07–00:11
Idea: feature
Screen: Z
```

## Regla importante tomada del video

**Una idea = un gráfico.**

No crear necesariamente un gráfico nuevo por cada oración.

Cada gráfico debe permanecer suficiente tiempo para poder entenderse y leerse.

El beat map es el blueprint visual del video.

---

# Fase 6 — Probar un solo gráfico

Antes de construir un video completo, seguir el consejo directo del creador:

> build one graphic as a web page first

Proceso:

**1 beat → 1 graphic → web page**

## Evaluación Cuenta 1

Pregunta principal:

**¿Se siente caro y profesional o se siente como una plantilla?**

## Evaluación Cuenta 2

Pregunta principal:

**¿Se siente como contenido nativo y útil o como un anuncio disfrazado?**

Si falla, corregir las reglas de diseño antes de continuar.

## Gate

No pasar al storyboard completo simplemente porque el gráfico funciona técnicamente.

Debe pasar el estándar creativo primero.

---

# Fase 7 — Storyboard completo

Una vez que un gráfico individual pase el estándar:

**beat map → storyboard completo**

Todavía no renderizar todo el video.

Revisar primero el plan visual y corregir:

- gráficos innecesarios;
- duración;
- exceso de texto;
- escenas que parecen baratas;
- momentos donde conviene mostrar UI;
- momentos donde no hace falta gráfico.

La lógica viene directamente del video:

> cambiar un plan cuesta casi nada; cambiar un gráfico terminado cuesta mucho.

---

# Fase 8 — Motion Graphics System

Cuando el storyboard esté aprobado, producir los gráficos.

## División del trabajo

El video divide videos largos en secciones y entrega cada sección a un subagente especializado.

Aplicar el mismo principio cuando tenga sentido:

```text
VIDEO

section 1 → agent
section 2 → agent
section 3 → agent
section 4 → agent
```

Cada agente debe recibir un trabajo estrecho y claro.

## Graphics as code

Los gráficos se construyen con código y posteriormente se convierten a video.

La implementación exacta queda pendiente de Fase 0.

## Captions palabra por palabra

Usar los timestamps generados por Whisper para permitir captions sincronizados palabra por palabra, como en el sistema del video.

## Renders concurrentes

El creador reporta que nueve renders simultáneos saturaron su máquina y que después limitó el sistema a cuatro renders concurrentes.

Empezar con:

`MAX_RENDERS = 4`

Cambiarlo únicamente si nuestras propias mediciones justifican otro valor.

---

# Fase 9 — Preview renders

Durante feedback y revisión usar renders pequeños / de menor resolución.

El creador utiliza aproximadamente media resolución durante drafts y solo renderiza en calidad completa cuando el corte está aprobado.

Objetivo:

- reducir tiempo;
- reducir coste;
- evitar render final de material que todavía cambiará.

Formato final del proyecto:

- vertical;
- 30–60 segundos.

---

# Fase 10 — Review Skill

Antes de revisión humana, el sistema debe revisar su propio trabajo.

El video describe una revisión de **10 frames por segundo** buscando seis errores específicos:

1. una animación que se reproduce dos veces;
2. un gráfico que aparece durante una fracción de segundo;
3. texto que llega demasiado tarde para poder leerlo;
4. un gráfico que tapa la cara;
5. una palabra dicha dos veces seguidas;
6. labios que pierden sincronización con la voz.

Empezar con estos checks.

No añadir una lista enorme de reglas inventadas desde el primer día.

Los errores propios que aparezcan después se incorporarán mediante feedback.

---

# Fase 11 — Revisión humana

Después del QA automático, revisar el video y registrar feedback concreto.

Ejemplo:

```text
00:07 esa animación parece plantilla
00:13 demasiado texto
00:21 esto ya parece anuncio y es Account 2
```

La revisión humana sigue teniendo la decisión final, igual que en el sistema descrito por el creador.

---

# Fase 12 — Feedback Skill

Esta es una de las partes centrales del sistema del video.

No basta con corregir el video actual.

Por cada error:

**error → qué instrucción habría evitado esto → actualizar Skill → corregir video actual**

El objetivo es que una corrección hecha hoy reduzca la probabilidad de repetir el mismo error en futuros videos.

El propio creador explica que la calidad de su sistema actual no salió de un solo prompt, sino de meses de notas acumuladas.

Nuestro sistema debe diseñarse desde el principio para aprender de las correcciones.

---

# Fase 13 — Asset Library

Guardar componentes que ya demostraron funcionar para poder reutilizarlos.

Ejemplos:

```text
assets/
├── graphics/
├── transitions/
├── layouts/
├── captions/
├── UI-elements/
└── reusable-components/
```

La lógica viene directamente del video: reutilizar assets reduce el trabajo, tokens y coste de los siguientes videos.

---

# Fase 14 — Separar memoria de las dos cuentas

Compartir solamente el motor técnico.

Ejemplo conceptual:

```text
shared/
  editing
  whisper
  ffmpeg
  rendering
  review-engine

account-1/
  hooks
  formats
  design
  feedback
  assets

account-2/
  hooks
  formats
  design
  feedback
  assets
```

El feedback creativo de una cuenta no debe modificar automáticamente el estilo de la otra.

---

# Orden real de ejecución

No construir todas las fases de golpe.

1. **Completar la spec y verificar los huecos reales del video.**
2. **Construir Research + Hook / Format Library.**
3. **Construir Script Skill.**
4. **Conseguir referencias visuales y construir Design Guidelines.**
5. **Generar un Beat Map.**
6. **Crear un solo gráfico como página web.**
7. **Lograr que ese gráfico pase el estándar de calidad.**
8. **Crear el storyboard completo.**
9. **Construir motion / render / captions.**
10. **Construir review automático.**
11. **Registrar feedback y modificar Skills.**
12. **Crear el primer video completo.**
13. **Repetir y dejar que el sistema acumule aprendizaje.**

---

# Próximo paso

Ejecutar **Fase 0**.

Las primeras incógnitas a cerrar son:

1. cuál es exactamente la herramienta / sistema web → video utilizado en el video de referencia;
2. cómo obtener y analizar videos ganadores / outliers;
3. cómo estructurar las Skills y los subagentes en Codex para reproducir la separación de trabajos del sistema original.

No avanzar a herramientas o arquitectura definitiva hasta cerrar esas incógnitas con suficiente evidencia.
