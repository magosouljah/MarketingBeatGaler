# scroll-inertia-curve

- Scope: `account-1`
- Origin: `add-finder-full-v1`
- Verified: `add-finder-full-v5-approved`
- Owner approval: Propietario, 2026-11-14 18:37 (America/Mexico_City), sesion Claude https://claude.ai/code/session_015kcBBsCG9a1mA8keWZkft4, sobre beatgaler-anuncio-v5.mp4: «me encanta manda versión final solo cambia el final para q el mouse no esté del lado derecho y esté centrada». Aprobacion previa parcial (03:38, prueba 4): «ok ya me gusto mucho solo las letras no».

## Problem observed
Propietario: «en el segundo 2:13 el frenado después del scroll rápido debe ser más lento y natural. mejora la curva».

## Hypothesized cause
La curva era simetrica (ease in-out): frenaba tan rapido como arrancaba.

## Validated prevention rule
Un scroll largo es un impulso con inercia: ataque rapido y cola exponencial larga (posicion proporcional a 1 - e^(-5.2 * u^1.25)).

## Verification required for future videos
El propietario no percibe un frenon al final del scroll.

## Passing evidence
Scroll de 8150 px entre 0.84 y 2.94 s con curva de inercia: a mitad del tiempo ya recorrio el 89 % y el resto se disipa en ~1 s.
