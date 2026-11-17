# text-inside-attention-margins

- Scope: `account-1`
- Origin: `fuck-v1`
- Verified: `fuck-final-approved`
- Owner approval: Propietario, 2026-11-16 18:09 (America/Mexico_City), sesion Claude https://claude.ai/code/session_015kcBBvgw9cB8YaopAoPsVD, sobre beatgaler_fuck_FINAL.mp4 (final 2): «perfecto ok quedo bien anota todo lo q aprendiste y cerramos».

## Problem observed
Propietario, 17:00: «el fuck llega a ser demasiado grande y puede salirse de la pantalla». Dio margenes de atencion: arriba 120 px, abajo 330, izquierda 120, derecha 120: «no significa q no puedan haber cosas ahi pero q talvez no se vean entonces cosas como el texto no pueden quedar ahi».

## Hypothesized cause
El texto se dibujaba en coordenadas de mundo y con una salida que lo escalaba hasta 8x; cualquier zoom o paneo de la camara lo sacaba del cuadro. No habia una zona segura definida para este video.

## Validated prevention rule
Todo texto queda dentro de la zona de atencion (120 px arriba, 330 abajo, 120 a cada lado, en 1080x1920). Se dibuja fijo en pantalla, no en el mundo de la camara, encogido hasta caber en 760 px de ancho y con el rebote de entrada limitado a 1.1x.

## Verification required for future videos
En una hoja de contactos con el recuadro de la zona de atencion dibujado, ningun texto de ningun frame toca ni cruza el recuadro.

## Passing evidence
Todo el texto (F**K, UPLOAD, STORE, ORGANIZE, PROPER, WAY y el CTA) se dibuja fijo en pantalla con ancho maximo de 760 px; verificado en hojas de contactos con el recuadro 120/330/120/120 dibujado.
