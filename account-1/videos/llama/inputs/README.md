# inputs/ — material fuente que NO está en el repositorio

El repositorio es público. Las capturas de la app, la grabación de referencia (con su música), el clip generado y los iconos de terceros se dejaron fuera; `tools/prepare.py` y `project/guy.py` los esperan aquí con estos nombres exactos:

| Archivo | Qué es | Uso |
| --- | --- | --- |
| `landing.jpg` | Captura de la landing de BeatGaler, **1600×769** | Logotipo «BeatGaler» (recorte ampliado y umbralizado) |
| `gallery.jpg` | Captura de la Gallery, **1600×874**, 3 filas × 7 portadas | 19 portadas; los recortes están en coordenadas de esta captura |
| `reference.mov` | Grabación de pantalla del reel de referencia (7.5 s) | Solo el audio: se extiende a 14.7 s |
| `guy.mp4` | Clip de Higgsfield (Seedance 2.5, 480×854, 24 fps, 6 s) | Escena del chico. Si falta, se dibuja una silueta provisional |
| `flp.png` | Captura del icono de un archivo `.flp` sobre blanco, con su nombre debajo | Icono de los `.flp` |
| `als.png` | Captura del icono de un archivo `.als` sobre blanco, con su nombre debajo | Icono de los `.als` |

Todo lo que se ponga en esta carpeta está ignorado por Git (ver `.gitignore`).
