# type-solid-not-transparent

- Scope: `account-1`
- Origin: `add-finder-test-v4`
- Verified: `add-finder-full-v5-approved`
- Owner approval: Propietario, 2026-11-14 18:37 (America/Mexico_City), sesion Claude https://claude.ai/code/session_015kcBBsCG9a1mA8keWZkft4, sobre beatgaler-anuncio-v5.mp4: «me encanta manda versión final solo cambia el final para q el mouse no esté del lado derecho y esté centrada». Aprobacion previa parcial (03:38, prueba 4): «ok ya me gusto mucho solo las letras no».

## Problem observed
Propietario sobre la prueba 4: «ok ya me gusto mucho solo las letras no; se ven bastante mal; no me gusta q queden como trans´parente y solo negro la q dice». Y sobre el siguiente intento (fichas azules con icono, 14:12): «no me gusta q tenga los símbolos cada palabra, ninguna debería tener eso».

## Hypothesized cause
Palabras atenuadas al 30 % de opacidad, y despues adornadas con iconos, hacen que el texto parezca un efecto de plantilla.

## Validated prevention rule
El texto en pantalla es solido (opacidad 100 %), de un solo color pleno, sin iconos ni adornos. La separacion del fondo se logra con halo o sombra, no con transparencia.

## Verification required for future videos
Ninguna palabra aparece semitransparente ni acompanada de simbolos.

## Passing evidence
Palabras en negro pleno con halo claro (F25-F139) y en blanco pleno con sombra (F160-F180); sin opacidad parcial ni iconos.
