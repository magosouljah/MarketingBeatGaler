# voice-word-gaps-even

- Scope: `account-1`
- Origin: `fuck-v1`
- Verified: `fuck-final-approved`
- Owner approval: Propietario, 2026-11-16 18:09 (America/Mexico_City), sesion Claude https://claude.ai/code/session_015kcBBvgw9cB8YaopAoPsVD, sobre beatgaler_fuck_FINAL.mp4 (final 2): «perfecto ok quedo bien anota todo lo q aprendiste y cerramos».

## Problem observed
Propietario, 17:00: «hay demasiado espacio entre upload y store, quiero q sea mas parecido al ti empo entre store y organize». En la v1 habia 3.45 s entre «upload» y «store» y 1.45 s entre «store» y «organize».

## Hypothesized cause
Cada palabra se coloco al inicio de su escena y la escena de la nube duraba 3.5 s; el ritmo de la frase hablada quedo a merced de la duracion de las escenas.

## Validated prevention rule
Las palabras de una misma enumeracion («upload, store, organize») entran con huecos parecidos (diferencia de 0.5 s o menos). Si una escena es mas larga, se comprime la escena o la palabra entra mas tarde dentro de ella; no se estira ni acelera la voz.

## Verification required for future videos
Medidos en la copia con contador, los huecos entre palabras consecutivas de la enumeracion difieren en 0.5 s o menos y el propietario no pide moverlas.

## Passing evidence
«upload» F134, «store» F185, «organize» F228: huecos de 1.70 y 1.45 s (diferencia 0.25 s).
