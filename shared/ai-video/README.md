# Clips generados con IA (Higgsfield)

Notas del único clip generado hasta ahora: el chico de [llama](../../content/videos/llama/) (2026-11-12, Seedance 2.5 desde el conector de Higgsfield en claude.ai). Los datos de precios y límites son los de ese día y esa cuenta; pueden haber cambiado.

## Antes de generar

- **Preguntar con qué se paga.** Es la cuenta del propietario. Ese día: 10 créditos; un clip de 6 s a 720p costaba 42; la prueba ilimitada cubría Seedance 2.5 **solo a 480p** (hasta 30 s). Se usó la ilimitada.
- **Pedir el costo sin generar**: `generate_video` con `get_cost: true`.
- **Una generación por vez.** La segunda, lanzada al mismo tiempo, falló con `rate_limit_reached`.
- Tarda unos 4 minutos. Mientras tanto se puede avanzar todo lo demás.

## El prompt que funcionó (texto a video, 9:16, 6 s, sin audio)

> Vertical front-facing phone camera shot, chest-up close-up, in a dark bedroom music studio at night lit by the cold blue-white glow of a computer monitor, studio speakers and a MIDI keyboard blurred behind. A fictional young adult man, about 24, with short curly dark hair, light stubble, a black hoodie and headphones around his neck, stares just below the lens at his screen, exhausted and frustrated: he drags both hands down his face, exhales and shakes his head in disbelief. Then his face goes completely deadpan. He calmly lifts a small lighter in his left hand and a glass perfume bottle in his right hand up in front of the camera, flicks the lighter so a small flame appears, and sprays the perfume through the flame straight toward the lens. A huge rolling burst of bright orange and yellow fire erupts toward the camera and completely fills the frame in the final moment. Single continuous take, realistic, cinematic, slight handheld shake, no text, no captions, no logos.

Qué hizo bien: un solo plano continuo, las acciones en el orden en que deben pasar, un personaje ficticio y adulto descrito con rasgos concretos, cómo debe terminar el cuadro, y «sin texto ni logos».

Qué le faltó: decir **cuánto del cuadro ocupa el sujeto**. Salió en el 45 % superior, con la mitad de abajo en negro. Hubo que recortar a 360×640 y ampliar 3×. La próxima vez: «face and hands fill the frame from top to bottom», o generar a 720p.

## Traer el clip

- El resultado queda en un CDN de Higgsfield que el entorno del agente puede tener bloqueado. No hay rodeo: el propietario lo descarga y lo adjunta, o permite ese dominio.
- Mientras llega, **entregar el montaje con un suplente** en vez de esperar. Decir claramente que es provisional.
- El agente no ve el clip hasta tener el archivo: no describirlo ni darlo por bueno antes.

## Montarlo

- Sale a 24 fps. Para encajarlo en una escena más corta, ver «Metraje dentro del video» en [`../rendering/README.md`](../rendering/README.md).
- Clavar con puntos clave los instantes que importan (aquí: llama, rociado, fuego lleno) sobre eventos del audio.
- No confiar en que el efecto del clip llegue justo a tiempo: reforzarlo con uno propio encima (aquí, fuego procedural hasta blanco en el drop).
- Se generó **una sola toma** y se usó esa. No hubo de dónde elegir.
