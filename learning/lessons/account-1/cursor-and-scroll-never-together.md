# cursor-and-scroll-never-together

- Scope: `account-1`
- Origin: `add-finder-test-v3`
- Verified: `add-finder-full-v5-approved`
- Owner approval: Propietario, 2026-11-14 18:37 (America/Mexico_City), sesion Claude https://claude.ai/code/session_015kcBBsCG9a1mA8keWZkft4, sobre beatgaler-anuncio-v5.mp4: «me encanta manda versión final solo cambia el final para q el mouse no esté del lado derecho y esté centrada». Aprobacion previa parcial (03:38, prueba 4): «ok ya me gusto mucho solo las letras no».

## Problem observed
Propietario: «cuando en 104 el mouse sube al mismo tiempo q el scrolll se me hace sentir como q la mano sube la pagina o nose creo q fue un accidente pero intenta q no sean los movimientos al mismo tiempo».

## Hypothesized cause
Cursor y lista moviendose a la vez en la misma direccion se leen como si la mano arrastrara la pagina.

## Validated prevention rule
El cursor nunca se desplaza mientras la lista hace scroll: se alternan. Durante un scroll el cursor queda quieto.

## Verification required for future videos
En la copia con contador no hay frames con scroll y desplazamiento de cursor simultaneos (se admite la cola de inercia casi detenida).

## Passing evidence
Scroll unico de F25 a F88. Desplazamientos del cursor: F87-F103, F111-F122 y F125-F135 (el primero arranca sobre el ultimo frame de la cola de inercia).
