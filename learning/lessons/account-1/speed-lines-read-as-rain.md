# speed-lines-read-as-rain

- Scope: `account-1`
- Origin: `add-finder-test-v1`
- Verified: `add-finder-full-v5-approved`
- Owner approval: Propietario, 2026-11-14 18:37 (America/Mexico_City), sesion Claude https://claude.ai/code/session_015kcBBsCG9a1mA8keWZkft4, sobre beatgaler-anuncio-v5.mp4: «me encanta manda versión final solo cambia el final para q el mouse no esté del lado derecho y esté centrada». Aprobacion previa parcial (03:38, prueba 4): «ok ya me gusto mucho solo las letras no».

## Problem observed
Autoevaluacion del agente al entregar la prueba: «las blancas del viaje pueden leerse como lluvia». Propietario: «de aceurdo».

## Hypothesized cause
Particulas blancas muy estiradas en vertical y con mucha opacidad dejan de leerse como velocidad y pasan a leerse como lluvia.

## Validated prevention rule
Para dar sensacion de viaje usar motas suaves y desenfocadas, con estiramiento maximo de ~3x y opacidad baja. La velocidad la comunican los objetos que viajan con la camara y la profundidad, no lineas.

## Verification required for future videos
Ningun frame del viaje muestra trazos largos y el propietario no menciona lluvia ni lineas.

## Passing evidence
Entre F147 y F202 el viaje usa motas con desenfoque de 2 px, estiramiento maximo 3.2x y opacidad media; el propietario no volvio a mencionar lluvia ni lineas.
