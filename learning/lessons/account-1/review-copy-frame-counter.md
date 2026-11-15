# review-copy-frame-counter

- Scope: `account-1`
- Origin: `add-finder-test-v1`
- Verified: `add-finder-full-v5-approved`
- Owner approval: Propietario, 2026-11-14 18:37 (America/Mexico_City), sesion Claude https://claude.ai/code/session_015kcBBsCG9a1mA8keWZkft4, sobre beatgaler-anuncio-v5.mp4: «me encanta manda versión final solo cambia el final para q el mouse no esté del lado derecho y esté centrada». Aprobacion previa parcial (03:38, prueba 4): «ok ya me gusto mucho solo las letras no».

## Problem observed
Propietario: «cuando mandes ejemplos quiero q tengan los frames para qte diga donde correguir».

## Hypothesized cause
Sin una referencia de tiempo exacta el feedback llega como descripciones («en el segundo 3») y obliga a adivinar.

## Validated prevention rule
Toda prueba enviada al propietario incluye una copia con contador de frames quemado (shared/ffmpeg/review_copy.sh). El frame 0 es el inicio del anuncio; si el inicio cambia, se avisa que la numeracion se recorrio.

## Verification required for future videos
El propietario da sus correcciones citando frames.

## Passing evidence
Desde la prueba 2 cada entrega llevo copia con contador y el propietario corrigio por frame: «desde el fram 32 hasta 66», «cuando en 104 el mouse sube», «el mouse en F124 a 141».
