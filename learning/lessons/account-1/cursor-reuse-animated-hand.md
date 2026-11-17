# cursor-reuse-animated-hand

- Scope: `account-1`
- Origin: `fuck-v1`
- Verified: `fuck-final-approved`
- Owner approval: Propietario, 2026-11-16 18:09 (America/Mexico_City), sesion Claude https://claude.ai/code/session_015kcBBvgw9cB8YaopAoPsVD, sobre beatgaler_fuck_FINAL.mp4 (final 2): «perfecto ok quedo bien anota todo lo q aprendiste y cerramos».

## Problem observed
Propietario, 17:00, con captura del cursor mostrando un recuadro negro: «te mande imagen de como se ve el mouse por alguna razon, la otra vez tu creaste un mouse animado, ese me gusta puede hacer algo parecido auqn un poco mas pequeño».

## Hypothesized cause
Se dibujo public/beatgaler-custom-cursor.png tal cual: ese PNG tiene fondo negro opaco y no lleva animacion. La mano de pixeles animada de add-finder ya estaba aprobada y no se reutilizo.

## Validated prevention rule
El cursor de los videos es la mano de pixeles animada de add-finder (reconstruida fila a fila, con estiramiento por velocidad, encogimiento al clic y aro), nunca el PNG de la app. El tamano se ajusta al encuadre.

## Verification required for future videos
En la copia con contador el cursor no tiene recuadro, se encoge en cada clic y el propietario no lo corrige.

## Passing evidence
Mano de pixeles al 70%: quieta antes del clic derecho (F272) y del clic en Share (F291), encogida a 0.74x en ambos.
