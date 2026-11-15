# real-product-ui-components

- Scope: `account-1`
- Origin: `add-finder-full-v1`
- Verified: `add-finder-full-v5-approved`
- Owner approval: Propietario, 2026-11-14 18:37 (America/Mexico_City), sesion Claude https://claude.ai/code/session_015kcBBsCG9a1mA8keWZkft4, sobre beatgaler-anuncio-v5.mp4: «me encanta manda versión final solo cambia el final para q el mouse no esté del lado derecho y esté centrada». Aprobacion previa parcial (03:38, prueba 4): «ok ya me gusto mucho solo las letras no».

## Problem observed
Propietario: «los tags donde clicka el louse no se ven así en la galería. usaste los asstes pero de los tags de los beats hay otro tags q son la barra de tags usala y asegúrate de q tenga los colores reales de los tags q decidiste colorear».

## Hypothesized cause
Se reutilizo el estilo de pildora de las tarjetas para inventar una barra de filtros que no existe en el producto.

## Validated prevention rule
Cada elemento de interfaz que se muestra se copia del componente real de la app (estructura, tipografia, estados y paleta), leyendo su codigo fuente. No se improvisa uno parecido.

## Verification required for future videos
Comparado con el codigo de la app, el elemento coincide en estructura, estados y colores.

## Passing evidence
Barra de tags reconstruida desde TagNavigation.tsx y gallery.css de la app: etiquetas de texto sin pildora, «All» primero, peso 430 que pasa a 720 al activarse, desvanecido a la derecha y paleta real (#FF3B30, #FF9500, #FFCC00, #34C759, #007AFF, #AF52DE, #8E8E93).
