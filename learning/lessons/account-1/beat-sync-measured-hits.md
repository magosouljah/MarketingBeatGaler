# beat-sync-measured-hits

- Scope: `account-1`
- Origin: `add-finder-test-v1`
- Verified: `add-finder-full-v5-approved`
- Owner approval: Propietario, 2026-11-14 18:37 (America/Mexico_City), sesion Claude https://claude.ai/code/session_015kcBBsCG9a1mA8keWZkft4, sobre beatgaler-anuncio-v5.mp4: «me encanta manda versión final solo cambia el final para q el mouse no esté del lado derecho y esté centrada». Aprobacion previa parcial (03:38, prueba 4): «ok ya me gusto mucho solo las letras no».

## Problem observed
Propietario: «en el segundo 3 ya deberian estar ordenadas las portadas, no por el segundo sino por el beat, quedaria mejor». La cuadricula caia en 4.898 s (inicio teorico del compas 4 a 147 BPM); el kick real medido despues estaba en 4.537 s, y el golpe visual quedaba en mitad de un redoble de caja.

## Hypothesized cause
Los impactos se colocaron sobre una rejilla calculada (BPM x compases) y no sobre los transientes del audio. El MP3 trae ~35 ms de retraso y el patron real de kicks no cae en los tiempos fuertes.

## Validated prevention rule
Antes de animar, medir los transientes reales del audio (shared/editing/find_hits.py) y anclar cada impacto visual a un kick o una caja medidos. Nunca usar segundos redondos ni una rejilla teorica. Si la musica cambia o se recorta, se vuelve a medir.

## Verification required for future videos
En la copia con contador, cada impacto visual cae a 1 frame o menos del transiente medido y el propietario no senala desfase con la musica.

## Passing evidence
Tiempos medidos con shared/editing/find_hits.py sobre el beat (archivo desde 0.546 s): clic F144 = kick 4.800 s; cuadricula F181 = kick 6.031 s; mutacion en rafagas sobre el redoble 6.14-6.69 s; barra de tags F229 = caja 7.645 s; clic en el tag F242 = kick 8.071 s; marca F260 = kick 8.681 s.
