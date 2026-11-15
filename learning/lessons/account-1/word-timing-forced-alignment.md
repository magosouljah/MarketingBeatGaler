# word-timing-forced-alignment

- Scope: `account-1`
- Origin: `add-finder-full-v3`
- Verified: `add-finder-full-v5-approved`
- Owner approval: Propietario, 2026-11-14 18:37 (America/Mexico_City), sesion Claude https://claude.ai/code/session_015kcBBsCG9a1mA8keWZkft4, sobre beatgaler-anuncio-v5.mp4: «me encanta manda versión final solo cambia el final para q el mouse no esté del lado derecho y esté centrada». Aprobacion previa parcial (03:38, prueba 4): «ok ya me gusto mucho solo las letras no».

## Problem observed
Propietario: «el timing de hundreds of beats no está». Medicion posterior con alineacion forzada: OF entraba 6 frames tarde y BEATS 9; WHICH / ONE'S / WHICH iban ~7 frames adelantadas; «for» aparecia medio segundo antes de que la voz lo dijera.

## Hypothesized cause
Los tiempos de palabra se estimaron mirando la envolvente de volumen. «beats» quedo partido en dos: la «b-ea» se tomo por «of» y la «ts» final por «beats».

## Validated prevention rule
Los tiempos de cada palabra se obtienen con alineacion forzada contra el texto (shared/transcription/align_words.py) y se contrastan con las sibilantes; nunca a ojo sobre el volumen. La palabra llega a su sitio como maximo 2 frames antes de oirse.

## Verification required for future videos
Cada palabra en pantalla queda a 2 frames o menos del inicio medido de su palabra hablada y el propietario no reporta desfase.

## Passing evidence
Alineacion forzada de las cuatro locuciones: HUNDREDS entra en F25 (voz F26), OF F44 (voz F46), BEATS F49 (voz F50), WHICH F107, ONE'S F115, WHICH F123, «for» F322 y «free» F328 con el toque a la pildora.
