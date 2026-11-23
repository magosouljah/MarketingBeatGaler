# inputs/ — material fuente que NO está en el repositorio

El repositorio es público. Los logos de terceros, las fotos del bote, la voz y el beat se dejaron fuera; `tools/prepare.py` los espera aquí con estos nombres exactos:

| Archivo | Qué es | Uso |
| --- | --- | --- |
| `dropbox.png` | Logo de Dropbox sobre fondo transparente o blanco | Ficha blanca tipo icono de app |
| `drive.jpg` | Logo de Google Drive sobre blanco | Ficha blanca tipo icono de app |
| `untitled.webp` | Icono de la app Untitled (cuadrado, con su fondo oscuro) | Ficha; conserva su fondo |
| `bin.jpg` | Foto del bote metálico con la tapa flotando, **1080×1920**, fondo blanco | Cuerpo y tapa del bote; los recortes están en coordenadas de esta foto |
| `bin-paper.jpg` | La misma foto del bote con papel arrugado dentro, **675×1200**, fondo blanco | Solo el papel que asoma |
| `voice.mp3` | Locución completa de corrido (ElevenLabs, 9.8 s) | Se corta en seis frases por sus silencios |
| `beat.mp3` | Beat del propietario («TIRED OF LOVING U LIKE A BROSKI», ~136 BPM) | Entra desde 7.94 s; su drop (13.94 s) cae en 6.00 s del video |

Además hace falta un checkout de BeatGaler en `BEATGALER_REPO` (solo lectura): de ahí salen las portadas (`DESIGN/shared/assets/real-covers`), el logo (`src-tauri/icons/icon.png`) y el cursor (`public/beatgaler-custom-cursor.png`).

Todo lo que se ponga en esta carpeta está ignorado por Git (ver `.gitignore`).
