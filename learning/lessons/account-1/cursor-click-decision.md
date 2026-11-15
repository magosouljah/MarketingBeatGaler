# cursor-click-decision

- Scope: `account-1`
- Origin: `add-finder-test-v1`
- Verified: `add-finder-full-v5-approved`
- Owner approval: Propietario, 2026-11-14 18:37 (America/Mexico_City), sesion Claude https://claude.ai/code/session_015kcBBsCG9a1mA8keWZkft4, sobre beatgaler-anuncio-v5.mp4: «me encanta manda versión final solo cambia el final para q el mouse no esté del lado derecho y esté centrada». Aprobacion previa parcial (03:38, prueba 4): «ok ya me gusto mucho solo las letras no».

## Problem observed
Propietario: «siento q la mano cuando hace click no se siente como decicion sino como q se siguie moviendo sin nunca detenerse a ahcer click, y tambien puedes poner un sonido de click y q la mano se haga pequeña».

## Hypothesized cause
El cursor llegaba y hacia clic en el mismo gesto, con retroceso inmediato. Sin una pausa previa el ojo no distingue decidir de pasar por ahi.

## Validated prevention rule
Todo clic del cursor se construye en cuatro tiempos: llegar, quedarse completamente quieto al menos 0.2 s, encogerse (~0.75x) al presionar con sonido de clic y un aro en el punto, y soltar. Nada mas se mueve durante la pausa.

## Verification required for future videos
En la copia con contador el cursor permanece inmovil al menos 6 frames antes de cada clic y el propietario lo lee como una decision.

## Passing evidence
El cursor llega al archivo en F135 y queda inmovil 9 frames; en F144 se encoge a 0.74x con sonido de clic y aro, aguanta y suelta. Mismo patron en el tag (quieto F235-F241, clic F242) y en la pildora (quieto F320-F327, clic F328).
