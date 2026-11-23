# FFmpeg — utilidades y recetas

## Copia de revisión con contador de frames

```bash
bash shared/ffmpeg/review_copy.sh video.mp4            # -> video-frames.mp4
```

Quema `F <frame>   <segundos>s` abajo a la izquierda. Toda prueba que se manda al propietario lleva esta copia (lección `review-copy-frame-counter`).

## Unir tramos sin recodificar

```bash
printf "file 'a.mp4'\nfile 'b.mp4'\n" > concat.txt
ffmpeg -f concat -safe 0 -i concat.txt -an -c:v copy video.mp4
ffmpeg -i video.mp4 -i audio.m4a -map 0:v -map 1:a -c:v copy -c:a copy -shortest -movflags +faststart final.mp4
```

Los tramos deben compartir tamaño, fps y ajustes del codificador.

## Mezcla de voz, música y efectos

Receta real: [`content/videos/add-finder/tools/render.sh`](../../content/videos/add-finder/tools/render.sh).

- Cada pista se coloca con `adelay=<ms>|<ms>`.
- `amix=inputs=N:normalize=0`, y `alimiter=limit=0.95` al final. Con la normalización por defecto todo baja según el número de entradas.
- Música que empieza a mitad del archivo: `atrim=<inicio>:<fin>,asetpts=PTS-STARTPTS`.
- Bajar la música bajo la voz: `volume='if(lt(t,8.5),0.85,…)':eval=frame`.
- Voces mono a estéreo centrado: `pan=stereo|c0=c0|c1=c0`.
- Clics de interfaz ~15 ms antes del frame donde ocurren.
- Recorte de locuciones: quitar el silencio inicial y cerrar con `afade` de 80 ms para que no quede un chasquido.

## Medir antes de colocar

- Golpes del beat: [`../editing/find_hits.py`](../editing/find_hits.py).
- Tiempos de cada palabra: [`../transcription/align_words.py`](../transcription/align_words.py).
