# Aprendizaje de video

Mismo principio que hooks, scripts y storyboard: aprender para cambiar la forma de animar, no acumular ejemplos.

1. Registrar la crítica exacta con su frame y su versión. Conservar lo que sí gustó.
2. Buscar la causa mecánica antes de tocar nada: qué curva, qué capa, qué orden o qué tiempo produce lo que el propietario ve. Confirmarla midiendo.
3. Cambiar solo esa causa. Si el propietario dice que lo anterior estaba mejor, se vuelve a lo anterior.
4. Si la causa es reutilizable, llevarla a [TECNICAS](TECNICAS.md) como regla con el problema que resuelve. Si no está clara, anotarla aquí como hipótesis.
5. Distinguir defecto de ejecución, decisión que el brief no especificaba y preferencia nueva. Lo segundo alimenta el [traspaso del storyboard](../storyboard/APRENDIZAJE.md).

La aprobación visual del propietario no es dato de audiencia; eso sigue en `6-aprendizaje/`.

## Evidencia — old-beats C-C1-H1 (2026-11-26)

| Crítica del propietario | Causa encontrada | Regla |
| --- | --- | --- |
| «La time quiero que se sienta muy larga», «dura muy poco» | Recorrido de 1.85 s con pocos elementos | Cámara §6: contenido y tiempo |
| «El primer beat debe verse unos 30 frames, ahora son 15» | La cámara giraba sin frenar antes | Cámara §6: 30 frames nítidos |
| «No sirve que escribas las notas si no se pueden leer» | Notas pequeñas en tramos rápidos | Nada encimado §7 |
| «Nada debe quedar encimado» | Objetos y notas colocados sin reservar espacio | Nada encimado §7 |
| «Bosque debería estar centrado y con la portada correcta desde antes» | El archivo se convertía en tarjeta durante un zoom | Cámara §6: objeto centrado y definitivo |
| «F77–F144 es completo silencio» | Menú y arranque de FL sin voz ni música | Tiempo §8: sin huecos |
| «El volumen es muy bajo, pantalla completa» | Beats atenuados bajo la voz; ventana pequeña | Tiempo §8 |
| «Cómo se transforma el timeline es una basura… que las portadas se vuelvan las del círculo» | Las portadas se desvanecían y aparecían otras | Transformar §5 |
| «Se forman hacia adelante en vez de a la cola» | Orden de páginas creciente = delante del líder | Líder y cola §3 |
| «El anterior estaba mucho mejor, solo las capas» | Se rehízo el vuelo como una fila en vez de corregir capas | Líder y cola §3; SKILL: rehacer solo lo pedido |
| «Sigue mal, se enciman hasta F752» | `z-index` de los hijos sin contexto de apilamiento | Capas §4 |
| «Se detiene en 720… que empiece a acelerarse» | El vuelo frenaba a cero y la rueda arrancaba a velocidad plena | Nada se detiene §1; Quién pone en marcha §2 |
| «Que la portada lo inicie y no que el círculo la cache» | Propuesta de tener la rueda girando antes | Quién pone en marcha §2 |
| «La primera se queda quieta 720–726» | Vuelta en U de la curva (1.2 px/frame en F718) | Nada se detiene §1: medir px por frame |

Aprobado por el propietario: el cierre de la versión `v8-final` («muy bien»). El video completo con ese cierre está pendiente de regenerar.
