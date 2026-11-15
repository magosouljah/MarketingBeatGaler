# cursor-natural-speed

- Scope: `account-1`
- Origin: `add-finder-test-v3`
- Verified: `add-finder-full-v5-approved`
- Owner approval: Propietario, 2026-11-14 18:37 (America/Mexico_City), sesion Claude https://claude.ai/code/session_015kcBBsCG9a1mA8keWZkft4, sobre beatgaler-anuncio-v5.mp4: «me encanta manda versión final solo cambia el final para q el mouse no esté del lado derecho y esté centrada». Aprobacion previa parcial (03:38, prueba 4): «ok ya me gusto mucho solo las letras no».

## Problem observed
Propietario: «el mouse en F124 a 141 es demasiado rapido porfavor q se sienta mas natural». En ese tramo el cursor hacia tres saltos entre filas en 0.57 s.

## Hypothesized cause
Tres desplazamientos encadenados en medio segundo son mas rapidos que una mano real.

## Validated prevention rule
Un desplazamiento del cursor entre dos puntos dura 0.3 s o mas, con aceleracion y frenado suaves; maximo dos o tres desplazamientos por tramo de duda, con pausa entre ellos.

## Verification required for future videos
Ningun desplazamiento dura menos de 9 frames y el propietario no lo percibe apresurado.

## Passing evidence
Los tres desplazamientos duran 16, 11 y 10 frames, con pausas de 8 y 3 frames entre ellos.
