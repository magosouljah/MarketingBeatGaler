# type-never-covers-or-fakes-ui

- Scope: `account-1`
- Origin: `add-finder-full-v2`
- Verified: `add-finder-full-v5-approved`
- Owner approval: Propietario, 2026-11-14 18:37 (America/Mexico_City), sesion Claude https://claude.ai/code/session_015kcBBsCG9a1mA8keWZkft4, sobre beatgaler-anuncio-v5.mp4: «me encanta manda versión final solo cambia el final para q el mouse no esté del lado derecho y esté centrada». Aprobacion previa parcial (03:38, prueba 4): «ok ya me gusto mucho solo las letras no».

## Problem observed
Propietario (16:24): «el hundreds of beats tapa el finder eso definitivamente no se ve bien; lo q creo es q simulaste q las letras eran parte del finder hasta pusiste el highlight azul». Sobre la correccion propuesta (17:14): «si se ve bien pero prefiero negro y q no sea continuo todo. entonces sería hundreds varias veces y luego espacio luego los OF y luego los beats; y también q estén alineados como hubdreds y no como of y como beats».

## Hypothesized cause
Para integrar el texto se disfrazo de interfaz (franjas de fila y seleccion azul) y se hizo opaco a pantalla completa: escondia justo lo que el anuncio estaba mostrando.

## Validated prevention rule
El texto va encima de la escena sin fondo propio y sin imitar la interfaz; la escena sigue visible detras. Las palabras repetidas van en bloques separados por aire, todos con el mismo margen izquierdo y el mismo ancho.

## Verification required for future videos
Con el texto en pantalla se sigue viendo la interfaz detras y los bloques comparten margen y ancho.

## Passing evidence
Tres bloques (HUNDREDS x3, OF x8, BEATS x4) en negro, sin fondo ni seleccion, con el mismo margen y el mismo ancho, y la lista del Finder visible detras (F25-F78).
