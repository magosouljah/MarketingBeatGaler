# placements A-C1-H1 — decisiones y aprendizajes (v1, sin validar)

Nada de esto es lección validada: son decisiones de producción y feedback textual del propietario, a registrar como caso en `learning/cases/`.

## Medidas
- Beat: 150 BPM (negra 0.4 s), bucle de 16 tiempos con ~3.5 s de solo hats. 808 en T = .06 1.26 5.86 6.46 7.66 11.66 12.26 12.86 14.06 18.66 19.26 20.46; cajas en 8.85 10.45 13.65 15.25 16.85.
- Voz alineada con `align_words.py` (`--say asap="EY S AE P"`). Los archivos llegaron con los nombres cruzados (C1 contenía el hook y H1 el cuerpo).
- La voz dura ~15.5 s y las acciones de la escena 3 no caben en la frase: el cuerpo se cortó en dos silencios medidos (5.98 s y 9.20 s del archivo) y se abrieron 0.30 s y 2.5 s de música sola. No se reescribió ni se aceleró nada.

## Sincronía elegida
| Momento | T | Ancla |
| --- | --- | --- |
| (tabla de la v1; en la v2 el hook se adelanta y el cuerpo va +0.40 s, ver `timing.js`) | | |
| Enviar respuesta en la Story | 1.26 | 808 |
| HUNDREDS | 6.47 | palabra + 808 de 6.46 |
| Despegue de archivos | 8.85 | caja |
| Portadas caen en la rejilla | 10.45 | caja |
| ORGANIZE / clic `rnb` (GENRE) / clic `dark` (MOOD) | 11.72 / 12.86 / 13.65 | 808, 808, caja |
| Select, tres tarjetas, Create pack, Copy link | 14.06 · 14.66 15.05 15.45 · 15.85 · 16.45 | rejilla de semicorcheas |
| Vuelta al chat | 16.85 | caja |
| READY / FIRE 🔥 / acento final | 18.64 / 19.26 / 20.46 | 808 |

## Decisiones
- El orden de clics es `rnb` y luego `dark` (el brief decía al revés) para que cada clic caiga sobre «genre» y «mood».
- **Quick Pack es V2 y no tiene diseño.** La barra «n selected · Create pack» y la hoja con el link son propuesta del agente sobre componentes reales (tarjetas, barra de tags, botón Select de la captura del propietario). Pendiente de que el propietario la apruebe o la sustituya.
- El chat se reconoce por convenciones de interfaz; no lleva logotipo ni marca de la plataforma.
- Iconos de archivo neutros: los `.flp`/`.als` de add-finder salían de capturas que no están en el repo.
- Portadas: solo las abstractas que add-finder ya usaba en primer plano, más seis sin marcas ni personas.

## Feedback del propietario (2026-11-25, prueba 1)
- «No está mal».
- Story con foto real y frase «Send beats»; foto de perfil propia.
- F52: acercar la cámara a los tres puntitos para crear expectativa. → hecho.
- No entendió la palabra repetida tres veces (ASAP). Propuso que ASAP salga del mensaje. → una sola, nace sobre la palabra del globo.
- En vez de FIRST×5: FIRST / TO / SEND, sin estorbar. → apiladas abajo a la izquierda, una por golpe de voz.
- Pendiente de confirmar: HUNDREDS sigue repetida tres veces (ahí la repetición dice cantidad).

## Feedback del propietario (2026-11-25, v1 completa) → v2
- «Send beats» más abajo: arriba pero no tan arriba. → `top: 400px` en la tarjeta.
- Sin build-up mientras el artista escribe; todo pasaba demasiado rápido. → el hook dura 0.4 s más (un tiempo), se escribe y envía antes (1.05 s) y los tres puntitos duran ~1 s con empuje lento de cámara. La música entra desde 6.0 s del archivo para que el cuerpo siga cayendo en los mismos golpes; todos los tiempos del cuerpo llevan `+M`.
- F99: FIRST más arriba y completar «FIRST / TO / SEND / YOURS».
- Finder con los iconos reales de `.flp` y `.als`: `desk.js` los usa si existen `assets/icons/flp.png` y `als.png` y `window.FILE_ICONS` es true (capturas del propietario, como en add-finder; no se versionan).
- Mini zoom al FIRE al final. → el globo queda como punto fijo y la cámara crece 14 %.

## Cierre (2026-11-25)
- El propietario mandó las capturas de los iconos `.flp` y `.als` y pidió versionarlas: están en `project/assets/icons/` como PNG con transparencia. Aparecen en las filas del Finder y en el vuelo; al caer en la Gallery las tapa la portada.
- Pidió la versión final tras la v2. Pendiente: evaluación con el scorecard y caso en `learning/cases/`.
- Corrección: el primer recorte del icono `.flp` cortaba el círculo por abajo (recorte por porcentaje). Ahora se corta en el hueco blanco entre icono y nombre, y los dos iconos van a 46 px en la fila.
