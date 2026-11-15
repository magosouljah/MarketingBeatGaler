# cover-mutation-random-fast

- Scope: `account-1`
- Origin: `add-finder-full-v1`
- Verified: `add-finder-full-v5-approved`
- Owner approval: Propietario, 2026-11-14 18:37 (America/Mexico_City), sesion Claude https://claude.ai/code/session_015kcBBsCG9a1mA8keWZkft4, sobre beatgaler-anuncio-v5.mp4: «me encanta manda versión final solo cambia el final para q el mouse no esté del lado derecho y esté centrada». Aprobacion previa parcial (03:38, prueba 4): «ok ya me gusto mucho solo las letras no».

## Problem observed
Propietario en la prueba 1: «puedes hacer q se vallan agregando portadas a lo random pero me gustaria q al ponerse portadas q tengan animacion las portadas como q crecen». En el completo v1: «como mutan los beats a beats con portada y tags debe verse más rápido y random».

## Hypothesized cause
Revelar todo en ondas uniformes y en dos golpes globales (portadas, luego datos) se ve mecanico y lento.

## Validated prevention rule
Cada tarjeta muta con su propio reloj, en orden aleatorio y en rafagas sobre los golpes: la portada crece desde un punto (~0.2 s) y sus datos entran ~0.1 s despues.

## Verification required for future videos
No se distingue un patron de barrido y toda la mutacion dura 1.3 s o menos.

## Passing evidence
Mutacion entre 6.14 y 7.46 s (1.3 s): 36 tarjetas en cinco rafagas sobre el redoble y el resto al azar; cada portada crece desde un punto en 0.2 s y sus datos entran 0.09-0.14 s despues.
