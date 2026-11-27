# old-beats — «Not every beat you made three years ago is bad» (C-C1-H1)

Video vertical 1080×1920, 30 fps, 28.75 s. Línea del tiempo de 2022 a 2027 → portada de `bosque` → Gallery → clic derecho «Open project» → arranque de FL → grabación real del beat viejo → drag & drop del clip de la melodía al proyecto nuevo → grabación real del beat nuevo → las portadas de la línea del tiempo forman la rueda → CTA «Comment GALER to store all your beat history online».

Brief original: [BRIEF.md](BRIEF.md). Decisiones y feedback: [LEARNINGS.md](LEARNINGS.md). Técnicas de animación que salieron de aquí: [pipeline/video](../../../pipeline/video/TECNICAS.md).

## Cómo se produce

```bash
# 1. poner el material en inputs/ (ver inputs/README.md)
bash tools/prepare.sh      # frames de las dos grabaciones, recorte del clip, fuentes, portadas, sonido de arranque
bash tools/render.sh       # out/old-beats-C-C1-H1.mp4 y copia con contador de frames
python3 tools/render.py frames /tmp/f 4.6 17.4 24.1          # frames sueltos (segundos)
python3 tools/render.py seg out/final.mp4 22.3 28.75         # solo un tramo
```

No usa HyperFrames: `tools/render.py` filma `project/index.html` con Chrome (Playwright) llamando a `renderT(t)`, que es una función pura del tiempo y espera a que se decodifique el frame de FL antes de capturar. Necesita `pip install playwright opencv-python` y Chrome en `/usr/bin/google-chrome` (o `CHROME=`).

## Módulos (`project/js`)

| Archivo | Qué hace |
| --- | --- |
| `timing.js` | Todos los tiempos, anclados a audio medido. `HOOK` es lo intercambiable para H2/H3. |
| `timeline.js` | Línea del tiempo con cámara (spline con velocidades), cajas reservadas para que nada se encime, Gallery, menú y arranque de FL. |
| `fl.js` | Las dos ventanas de FL a pantalla completa y el arrastre del clip (muelle con inclinación). |
| `fly.js` | Portadas de la regla → páginas de la rueda (homografía a las esquinas proyectadas; líder, cola y capas). |
| `wheel.js` | Copia parametrizada del rig de [wheel/lab-v2](../wheel/lab-v2/hyperframes/src/wheel.js): portadas y nacimiento de cada página por parámetro. |
| `cta.js`, `subs.js`, `cursor.js` | Palabras del CTA y tarjeta final, subtítulos sobre FL, cursor de píxeles. |

## Tiempos de la versión final

| Momento | Segundo | Frame |
| --- | --- | --- |
| Hook | 0.00–2.80 | F0–F84 |
| «Your mixing… fire» | 2.85–8.71 | F85–F261 |
| Cámara centrada en bosque | 4.60 | F138 |
| Empieza el beat viejo | 6.45 | F193 |
| Batería del beat viejo (en «fire») | 8.30 | F249 |
| Frases del arrastre | 11.27–17.27 | F338–F518 |
| Se suelta el clip, arranca el beat nuevo | 17.37 | F521 |
| Batería del beat nuevo | 20.73 | F622 |
| La líder se engancha y arranca la rueda | 24.09 | F723 |
| CTA (voz) | 24.11–27.56 | F723–F827 |

Beat viejo sin voz: 2.6 s. Beat nuevo sin voz: 6.7 s. Mezcla a −10.5 LUFS.
