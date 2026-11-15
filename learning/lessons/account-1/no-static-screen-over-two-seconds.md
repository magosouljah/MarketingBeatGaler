# no-static-screen-over-two-seconds

- Scope: `account-1`
- Origin: `add-finder-full-v1`
- Verified: `add-finder-full-v5-approved`
- Owner approval: Propietario, 2026-11-14 18:37 (America/Mexico_City), sesion Claude https://claude.ai/code/session_015kcBBsCG9a1mA8keWZkft4, sobre beatgaler-anuncio-v5.mp4: «me encanta manda versión final solo cambia el final para q el mouse no esté del lado derecho y esté centrada». Aprobacion previa parcial (03:38, prueba 4): «ok ya me gusto mucho solo las letras no».

## Problem observed
Propietario: «6:64 a 10:30 es la misma pantalla; todo eso debe ser mucho más rápido y dinámico» y «11:27 a 15:40 es la misma pantalla».

## Hypothesized cause
Se dejo la camara quieta esperando golpes musicales lejanos.

## Validated prevention rule
Ningun encuadre permanece mas de ~2 s. Mientras dura una escena la camara sigue moviendose (empuje, giro) y cada medio segundo ocurre un evento nuevo.

## Verification required for future videos
En la copia con contador no hay ningun tramo de mas de 60 frames con el mismo encuadre estatico.

## Passing evidence
La galeria dura de F181 a F242 (2.0 s) con empuje de camara continuo hasta F224 y un evento cada pocos frames: mutaciones F184-F224, marca F218, barra de tags F229, cursor sobre el tag F235, clic F242.
