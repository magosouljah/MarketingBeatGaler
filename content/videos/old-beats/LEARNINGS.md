# old-beats — decisiones y feedback

Versión final entregada el 2026-11-26 (C-C1-H1). Sin evaluación del propietario ni caso registrado en `learning/` todavía. Las reglas reutilizables están en [pipeline/video/TECNICAS.md](../../../pipeline/video/TECNICAS.md) y la tabla crítica → causa en [pipeline/video/APRENDIZAJE.md](../../../pipeline/video/APRENDIZAJE.md); aquí queda lo específico de este video.

## Cómo fue

1. **Maqueta (v1, 30.45 s).** Ventana de FL pequeña sobre lienzo blanco, hook y cuerpo separados. Feedback: línea del tiempo corta, proyectos todos como icono de FL, notas ilegibles, bosque descentrado, 2 s de silencio tras el hook, volumen bajo, FL debe ir a pantalla completa, sin voz sobre el segundo beat, transición a la rueda sin transformación real.
2. **v2 (30.29 s).** Línea más larga, portadas mezcladas con `.flp`/`.als`, notas rojas con flecha, «Your mixing…» pegado al hook, FL a pantalla completa, «You might already…» antes de soltar el clip, regla que se enrolla en aro.
3. **v3 (28.75 s).** Viaje de 4.6 s que pasa por 2023, frena en el primer beat (≈39 frames nítidos) y vuelve; 2027 visible; tope al inicio de la línea; cuatro carriles sin nada encimado; subtítulos sobre FL; las 28 portadas más recientes vuelan a su página de la rueda.
4. **Cierre (v4–v8, solo el tramo final).** Orden líder/cola, capas, arranque lento que acelera y líder que no se detiene. Aprobado: «muy bien».

## Decisiones que conviene recordar

- **«Open project» no está verificado en la app.** `research/product/FEATURES-V1-V2.md` solo habla de guardar y descargar el archivo PROJECT. El menú lo muestra porque el brief lo pedía; confirmarlo antes de otro video que lo use.
- **La grabación del beat viejo no alcanza.** El audio repite una vez los compases 11.346–15.04 y el video se frena a 0.70× desde la segunda frase. Con una grabación 4 s más larga sobra el truco.
- **El clip arrastrado es un recorte real** del clip ZENOLOGY de Track 1 (`tools/sprites.py` lo localiza por plantilla en el frame en que se despega). En el proyecto nuevo se tapa Track 1 con el carril vacío de Track 2 hasta que cae.
- **El logo del arranque de FL es la captura del icono `.flp` del propietario**, no un logo redibujado. El sonido de arranque es propio: dos notas I→V con pluck senoidal y reverb (`tools/make_sfx.py`).
- **Las notas que pasan a toda velocidad no se leen** («First placement», «Favorite beat»). Se leen las cuatro donde la cámara va lenta.
- **Para H2 y H3** cambian `HOOK` en `timing.js`, la ruta de cámara de la escena 1 (`K` en `timeline.js`) y las palabras ancladas a 2023; el cuerpo cuelga de `HOOK.dur`.

## Pendiente

- Evaluación del propietario (`learning/scorecard`) y caso en `learning/cases/`.
- Variantes C-C1-H2 y C-C1-H3.
