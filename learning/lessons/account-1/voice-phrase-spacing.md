# voice-phrase-spacing

- Scope: `account-1`
- Origin: `add-finder-test-v2`
- Verified: `add-finder-full-v5-approved`
- Owner approval: Propietario, 2026-11-14 18:37 (America/Mexico_City), sesion Claude https://claude.ai/code/session_015kcBBsCG9a1mA8keWZkft4, sobre beatgaler-anuncio-v5.mp4: «me encanta manda versión final solo cambia el final para q el mouse no esté del lado derecho y esté centrada». Aprobacion previa parcial (03:38, prueba 4): «ok ya me gusto mucho solo las letras no».

## Problem observed
Propietario: «las frases las pusiste pegadas creo y tienes q analizar el timing para q queden natural y donde queremos, ahora mismo la frase q divide en 2 audios siento q estan muiy pegados esos dos audios, puedes darle un ligero esapcio» y «agrega video al inicio lo que creas necesario aunq no haya beat todavia».

## Hypothesized cause
Las frases se colocaron una tras otra para que cupieran antes del primer golpe; la musica mandaba sobre la respiracion de la voz.

## Validated prevention rule
Dejar una pausa audible (0.2 s o mas) entre las dos mitades de una frase y mas entre frases. Si la voz no cabe antes del golpe musical, se alarga la imagen o la intro de la musica: nunca se aprieta la voz.

## Verification required for future videos
El propietario no percibe frases pegadas.

## Passing evidence
«You have hundreds of beats» termina en 2.27 s y «but no idea which one's which» empieza en 2.50 s; la voz acaba en 4.57 s y el clic cae en 4.80 s. Para que cupiera se movio el inicio de la musica, no la voz.
