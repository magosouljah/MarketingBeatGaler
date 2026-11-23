# HyperFrames — cómo lo usamos

HyperFrames convierte una página HTML/CSS/JS en MP4, frame por frame. Versión fijada: **0.9.44**. Proyecto de ejemplo completo: [`content/videos/add-finder/project/`](../../content/videos/add-finder/project/).

## Comandos

```bash
export HYPERFRAMES_SKIP_SKILLS=1 HYPERFRAMES_NO_UPDATE_CHECK=1
cd <proyecto>                                   # carpeta con index.html, hyperframes.json, meta.json
npx --yes hyperframes@0.9.44 lint               # siempre primero
npx --yes hyperframes@0.9.44 snapshot           # capturas sueltas para revisar composición
npx --yes hyperframes@0.9.44 render --start 0 --end 7.8 --fps 30 -o a.mp4 --quiet
```

Si no puede descargar su navegador: `HYPERFRAMES_BROWSER_PATH=/usr/bin/google-chrome`.

## Patrón: una función pura `frame(t)`

```js
const driver = { _t: 0, get t(){ return this._t; }, set t(v){ this._t = v; frame(v); } };
const tl = gsap.timeline({ paused: true });
tl.to(driver, { t: DUR, duration: DUR, ease: "none" });
function frame(t){ /* calcula TODOS los estilos a partir de t, sin estado previo */ }
```

- GSAP solo mueve el reloj; la animación es código propio (curvas, `kf()` de fotogramas clave, `pulse()` para impactos, PRNG con semilla para lo aleatorio).
- Sin estado acumulado, cualquier frame se renderiza suelto y los tramos se unen sin saltos.
- Nada de `Math.random()` ni `Date.now()`: el mismo `t` debe dar siempre la misma imagen.
- Los tiempos importantes van como constantes con nombre al inicio del script, ancladas al audio medido.
- Cámara 3D: un contenedor con `perspective` y un «mundo» al que se le aplica la transformación inversa de la cámara.

## Render

- Cuesta ~0.7 s por frame en 2 CPU (1080×1920). Un anuncio de 12 s son unos 4 minutos por versión.
- Renderizar en tramos (`--start/--end`), unir con el demuxer `concat` y `-c copy`, y añadir el audio con `-c:v copy`. Cambiar la mezcla no obliga a renderizar de nuevo.
- Escribir a un nombre temporal y renombrar al terminar: un render interrumpido deja un archivo corto que sí se reproduce.
- El audio no pasa por HyperFrames: se mezcla con FFmpeg ([`../ffmpeg/README.md`](../ffmpeg/README.md)).

## Tropiezos conocidos

| Síntoma | Causa | Solución |
| --- | --- | --- |
| Todos los frames en blanco, sin error | Variable declarada dos veces en el script | Correr `lint` antes de mirar capturas |
| `lint` falla por un archivo que no es el tuyo | Lee cualquier `.html` de la raíz | Respaldos fuera del proyecto |
| `lint` rechaza la fuente | Fuente del sistema | `@font-face` con archivo local en `assets/fonts/` |
| Palabras repetidas descolocadas | `text-indent` se hereda a los `inline-block` | `margin-left` en el primer hijo |
| Tarjetas 3D que se atraviesan | `preserve-3d` parte planos que se cruzan | Resolver la disposición antes de animar; inclinación ≤ ~32° |
| No baja Chrome | Red restringida | `HYPERFRAMES_BROWSER_PATH` |

## Dos temas con una sola fuente

`theme.js` define `window.BG_THEME = "dark" | "light"` y se carga antes del script principal; el CSS del tema claro cuelga de `html[data-theme="light"]`. El script de render reescribe ese archivo antes de cada versión y lo restaura al salir.
