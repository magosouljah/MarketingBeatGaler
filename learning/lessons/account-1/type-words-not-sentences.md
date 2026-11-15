# type-words-not-sentences

- Scope: `account-1`
- Origin: `add-finder-full-v1`
- Verified: `add-finder-full-v5-approved`
- Owner approval: Propietario, 2026-11-14 18:37 (America/Mexico_City), sesion Claude https://claude.ai/code/session_015kcBBsCG9a1mA8keWZkft4, sobre beatgaler-anuncio-v5.mp4: «me encanta manda versión final solo cambia el final para q el mouse no esté del lado derecho y esté centrada». Aprobacion previa parcial (03:38, prueba 4): «ok ya me gusto mucho solo las letras no».

## Problem observed
Propietario: «but no idea wich ones wich eso no se ve bien alado del mouse, todas las letras deben ser grandes; intenta no poner las frases enteras sino palablras; si deberían detenerse un poquito para q se pueda leer por un mini segundo apenas lo necesario para poder leerlo; luego en there’s a better way no se ve nada ni se nota».

## Hypothesized cause
Frases completas en tamano pequeno (etiqueta de 38 px junto al cursor, linea de 70 px) no se leen en un Reel.

## Validated prevention rule
Texto cinetico = palabras clave sueltas, enormes (casi todo el ancho util), una idea a la vez, que entran con el movimiento de la escena y se detienen lo justo para leerse (0.15 a 0.5 s).

## Verification required for future videos
Cada palabra clave de la voz aparece grande y sola, y el propietario puede leerla.

## Passing evidence
HUNDREDS / OF / BEATS (F25, F44, F49), NO IDEA / WHICH / ONE'S / WHICH (F81, F107, F115, F123) y A BETTER / WAY. (F160, F170), todas de 158 px de cuerpo o mas. Las palabras de barra se detienen entre 0.16 y 0.76 s; los tres bloques quedan en pantalla hasta F71.
