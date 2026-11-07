# BeatGaler — phase2-songs-v1: 8 videos sobre wheel-v7 con 4 canciones

**Estado:** entregado para revisión del propietario (2026-11-07). La base es `wheel-v7`, aprobado el 2026-11-06 ([LEARNINGS.md](../choreography-lab-v2/LEARNINGS.md)). Su coreografía no se cambió. Caso: `learning/cases/phase2-songs-v1.json`.

## Brief del propietario (chat, 2026-11-07)

- 4 canciones (`work/songs/*.wav`, locales; **los WAV no se versionan**) × 2 versiones = 8 videos.
- **Negra:** igual que v7 (fondo `#0C0C0C`, texto blanco). **Blanca:** fondo claro y texto negro; la pill y la letra pequeña también se invierten.
- Cada video tiene que ser único (para que Instagram no lo trate como spam), con cambios ligeros que no rompan lo aprobado.
- Los cortes de las palabras y la entrada del cierre caen en los golpes de cada canción. Fades cortos y unos −14 LUFS.
- Propuesta de fragmento aprobada antes de renderizar: «va pero estaría bien alargar todo el video hasta que finalice la canción».

## Decisiones

- **Fragmento: desde 0,000 s hasta el final del WAV.** Las cuatro canciones tienen el drop en 1,30 s, justo cuando v7 abre la rueda (de 3 a 12 páginas entre 1,267 y 1,300 s). Por indicación del propietario, cada video dura lo que su canción (redondeado a fotograma). El tiempo extra es cierre: la rueda termina igual que en v7.
- **Cortes al golpe** (`tools/audio_cuts.py`): para cada corte de v7 (1,53 / 2,20 / 3,03 / titular 4,37) se toma el onset con mejor puntaje (fuerza × e^−(Δ/0,1 s)²) dentro de ±0,18 s (±0,15 s para el titular), y se ajusta al fotograma. Si ninguno llega al umbral, se queda el tiempo de v7. El bloque del cierre conserva los 0,07 s de adelanto sobre el titular. Datos: `evidence/audio-analysis.json`.
- **Versión blanca:** fondo `#F3F1EC`, un blanco cálido de papel. Un blanco puro deslumbra en los feeds en modo oscuro y se come el borde de las portadas blancas. El texto va en `#0C0C0C` (el fondo de la negra), la letra pequeña en `#0C0C0C` al 60 % y la pill en negro con letra `#F3F1EC`.
- **Formato:** 1080×1920, 30 fps, H.264 High (CRF 17) + AAC a 256 kbps, 48 kHz, `+faststart`. El cuadro de v7 (720×1280) se dibuja a 1,5× con más resolución real: el WebGL usa `pixelRatio` 1,5 y el texto es CSS escalado, no una imagen ampliada.
- **Audio:** fade de entrada de 0,03 s y de salida de 0,25 s (coseno). Ganancia hasta −14,0 LUFS integrados. Pico real ≤ −1 dBTP: en las canciones 3 y 4 actúa un limitador (`alimiter` a −1,6 dBFS, sobremuestreado ×4). Medido en el MP4 con `ebur128`.
- **Cierre más largo:** se conservan las velocidades de v7 y cada movimiento llega hasta el último fotograma («ningún texto se queda quieto»). El titular hace zoom de 0,93 a 1,02 + 0,015·(segundos extra). La parte inferior sube 14 px por cada 1,7 s y la marca crece +3 % por cada 1,7 s.

## Qué cambió en cada video

Solo se tocó la parte de la rueda anterior a 3,46 s. **La pila (3,75–4,8 s) y la maqueta del cierre son las de v7 en los 8.** Las variaciones están en `variants.json` (generado por `tools/plan_variants.py`):

- **Ángulo inicial:** `RIG.phase0` + Δ.
- **Ritmo:** se multiplican las velocidades angulares (`omega`) antes de 3,46 s; ±4 % como máximo.
- **Posición y escala:** desplazamiento de la rueda en unidades de mundo (el radio es 2,0) y factor de escala, también antes de 3,46 s.
- **Portadas:** cada video baraja las 24 portadas con una semilla y repite 4 en las 28 páginas, sin que una portada quede junto a sí misma.

| Video | Canción | Fondo | Duración | Cortes Unlimited / Free* / Storage (s) | Titular del cierre (s) | Ángulo inicial de la rueda | Ritmo de la rueda | Posición (x, y) | Escala | Entrada de palabras (y px, giro, escala, s) | Palabras x / marca x (px) | Portadas: semilla · repetidas | LUFS / dBTP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v7 | — (referencia) | `#0C0C0C` | 6,00 s | 1,530 / 2,200 / 3,030 | 4,370 | +0.00 rad | ×1.00 | +0.00, +0.00 | ×1.00 | 26, -3.5°, 0.85, 0.16 | 14 / -40 | — · orden v7 · 01–04 | — / — |
| 01-c1-negro | CANCION 1 | `#0C0C0C` | 7.47 s | 1,500 / 2,100 / 3,030 | 4,367 | +0.12 rad | ×1.00 | +0.03, +0.00 | ×1.00 | 26, -3.5°, 0.85, 0.16 | 14 / -40 | 11 · 06, 14, 17, 21 | -14.0 / -2.4 |
| 02-c1-blanco | CANCION 1 | `#F3F1EC` | 7.47 s | 1,500 / 2,100 / 3,030 | 4,367 | -0.20 rad | ×1.02 | -0.04, +0.02 | ×0.98 | 22, +3.0°, 0.86, 0.15 | 8 / -34 | 12 · 05, 06, 10, 24 | -14.0 / -2.4 |
| 03-c2-negro | CANCION 2 DEMBOW | `#0C0C0C` | 6.73 s | 1,530 / 2,333 / 3,067 | 4,367 | +0.30 rad | ×0.98 | +0.05, -0.02 | ×1.02 | 30, -4.5°, 0.84, 0.17 | 18 / -46 | 21 · 03, 09, 10, 12 | -14.0 / -4.6 |
| 04-c2-blanco | CANCION 2 DEMBOW | `#F3F1EC` | 6.73 s | 1,530 / 2,333 / 3,067 | 4,367 | -0.35 rad | ×1.03 | -0.02, -0.03 | ×0.99 | 20, -2.5°, 0.87, 0.14 | 12 / -36 | 22 · 13, 16, 17, 24 | -14.0 / -4.6 |
| 05-c3-negro | CANCION 3 CORRIDO | `#0C0C0C` | 6.33 s | 1,530 / 2,200 / 2,967 | 4,370 | +0.45 rad | ×0.97 | -0.05, +0.02 | ×1.01 | 28, +3.5°, 0.85, 0.18 | 10 / -42 | 31 · 03, 07, 19, 24 | -14.0 / -1.6 |
| 06-c3-blanco | CANCION 3 CORRIDO | `#F3F1EC` | 6.33 s | 1,530 / 2,200 / 2,967 | 4,370 | -0.10 rad | ×1.01 | +0.02, +0.03 | ×1.03 | 24, -3.0°, 0.83, 0.16 | 16 / -38 | 32 · 06, 11, 20, 22 | -14.0 / -1.6 |
| 07-c4-negro | CANCION 4 gym bro | `#0C0C0C` | 6.70 s | 1,600 / 2,133 / 2,933 | 4,300 | +0.22 rad | ×1.04 | +0.00, -0.04 | ×0.97 | 32, -4.0°, 0.86, 0.15 | 20 / -44 | 41 · 12, 17, 19, 21 | -14.0 / -1.3 |
| 08-c4-blanco | CANCION 4 gym bro | `#F3F1EC` | 6.70 s | 1,600 / 2,133 / 2,933 | 4,300 | -0.50 rad | ×0.99 | +0.04, +0.01 | ×1.00 | 26, +2.5°, 0.84, 0.17 | 6 / -32 | 42 · 02, 14, 18, 24 | -14.0 / -1.3 |

La fila «v7» es el control: con esos valores, el pipeline reproduce el video aprobado. Comparado con `beatgaler-orbita-v7.mp4` (reescalado a 720 px), ningún fotograma baja de 31,7 dB de PSNR y el promedio es 37,2 dB. La diferencia viene solo del texto renderizado a otra resolución. Antes del cambio a 1080, el render de v7 a 720×1280 era idéntico bit a bit (PSNR ∞).

## QA (`evidence/qa.json`, `evidence/qa-variation.json`, `evidence/contact-sheets/`)

- **Loudness:** los 8 MP4 dan −14,0 LUFS. Pico real entre −4,6 y −1,3 dBTP.
- **Unicidad:** la diferencia media en gris entre dos videos del mismo fondo es de 23–29 niveles (de 255), en los fotogramas 45–135. Contra v7 es de 26–30.
- **Coreografía:** la ocupación de la rueda en los fotogramas 46–103 tiene una correlación de 0,91–0,99 con v7. En `contact-sheets/stack-frames-107-131-all.png` (v7 y los 8, t = 3,57 / 3,77 / 3,97 / 4,17 / 4,37 s) se ve que la pila está llena, nivelada y paralela en los 8, y que se vacía al mismo tiempo que en v7. En la versión blanca la ocupación medida es menor porque las portadas claras se parecen al fondo: no faltan páginas.
- **Texto en movimiento:** en los dos últimos fotogramas de cada video el cierre todavía cambia (diferencia media de 0,08–0,39 por píxel en la zona del texto).
- **Contact sheets:** fotogramas cada 0,25 s más la forma de onda con los cortes. Hay que revisarlas a ojo; ninguna métrica sustituye la revisión del propietario.

## Puntos abiertos

- **v7 superpone «Free*» y «Storage» 0,04 s** (1–2 fotogramas; «Free*» dura 0,87 s y el siguiente corte llega 0,83 s después). Se conservó porque v7 está aprobado. Si el propietario quiere un corte limpio, se cambia `W2_OVERLAP` a 0.
- **Cortes sin golpe claro** (se quedaron en el tiempo de v7): canción 1 «Storage»; canción 2 «Unlimited»; canción 3 «Unlimited», «Free*» y el titular (ahí la canción va en decay).
- **FREEGALER** sigue siendo un código de laboratorio: hay que darlo de alta en BeatGaler antes de publicar.
- En la canción 4 el cierre entra 2 fotogramas antes que en v7 (4,30 s). La última página de la pila cruza el cierre ya visible durante unos fotogramas (en v7 pasa lo mismo, a partir de 4,30 s).

## Reproducir

Desde la raíz del repo, con los WAV en `work/songs/`:

```bash
pip install numpy soundfile librosa pyloudnorm scipy pillow
python account-1/creative-assets/phase2-songs-v1/tools/audio_cuts.py work/songs account-1/creative-assets/phase2-songs-v1/evidence/audio-analysis.json
python account-1/creative-assets/phase2-songs-v1/tools/plan_variants.py
# Linux: export HYPERFRAMES_BROWSER_PATH=/usr/bin/google-chrome
python account-1/creative-assets/phase2-songs-v1/tools/build.py v7 01-c1-negro 02-c1-blanco 03-c2-negro 04-c2-blanco 05-c3-negro 06-c3-blanco 07-c4-negro 08-c4-blanco
```

`build.py` arma cada proyecto HyperFrames en `work/phase2-songs/build/<id>/` con `lib/`, `assets/` y `src/wheel.js` de v7. A `wheel.js` le aplica dos parches que no cambian ninguna pose: `rig.pixelRatio` y `rig.covers`; ambos tienen v7 como valor por defecto y el script verifica que cada uno se aplique exactamente una vez. Después renderiza la secuencia PNG con `hyperframes@0.9.17`, prepara el audio, codifica a `work/phase2-songs/beatgaler-<id>.mp4` y escribe la contact sheet y el QA. Para editar un video en el preview: `cd work/phase2-songs/build/<id> && npx --yes hyperframes@0.9.17 preview`.

`DIRECCION.md` no se tocó. La app de BeatGaler tampoco: solo se leyeron sus portadas, a través de los assets de v7.
