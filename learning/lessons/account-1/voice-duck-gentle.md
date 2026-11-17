# voice-duck-gentle

- Scope: `account-1`
- Origin: `fuck-v1`
- Verified: `fuck-final-approved`
- Owner approval: Propietario, 2026-11-16 18:09 (America/Mexico_City), sesion Claude https://claude.ai/code/session_015kcBBvgw9cB8YaopAoPsVD, sobre beatgaler_fuck_FINAL.mp4 (final 2): «perfecto ok quedo bien anota todo lo q aprendiste y cerramos».

## Problem observed
Propietario, 17:00: «el sidechain de la voz y el beat no me gusta es muy brusco esta bien q suene mas el beat y menos ducking». La v1 usaba sidechaincompress con ratio 5, umbral 0.03, ataque 15 ms y liberacion 250 ms, con el beat a 0.5.

## Hypothesized cause
Con ratio alto y ataque corto el beat se hunde de golpe en cada silaba; en un beat con graves sostenidos ese bombeo se oye mas que la voz.

## Validated prevention rule
El ducking del beat bajo la voz es casi imperceptible: ratio 2 o menos, ataque de 50 ms o mas, liberacion de 400 ms o mas, y el beat alto. Si la voz no se entiende, se sube la voz antes que hundir el beat.

## Verification required for future videos
El propietario escucha la mezcla y no menciona el sidechain ni el ducking.

## Passing evidence
Misma mezcla que la v2 (ratio 1.6, ataque 60 ms, liberacion 500 ms, beat a 0.66); sin comentarios sobre el audio desde entonces.
