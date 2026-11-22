# 2. Razonamiento

**Responsabilidad:** explicar causalmente por qué un estímulo podría captar y mantener la atención de un productor, y qué relación editorial o comercial —directa, indirecta o discreta— puede tener con BeatGaler. Preguntar «¿por qué?» hasta distinguir mecanismo, evidencia y supuestos.

| | |
| --- | --- |
| Entra | `evidencia.csv` y `preguntas.csv` del módulo 1 |
| Sale | `mecanismos.csv` (uno por explicación) y `nodos.csv` (su árbol) |

## Cómo es un árbol

Un mecanismo tiene cinco ramas obligatorias: `mecanismo`, `audiencia` (quién sí y quién no), `fallo` (cuándo deja de funcionar), `alternativas` (qué más explicaría el efecto) y `camino` (qué relación editorial o comercial podría tener con BeatGaler, sin exigir que sea una solución directa).

Cada nodo es una pregunta con su respuesta. Un nodo con hijos sigue abierto. Un nodo sin hijos es una hoja y declara en qué termina:

| `cierre` | Significa | Exige |
| --- | --- | --- |
| `dato` | Observación o resultado propio | Evidencia citada |
| `fuente` | Lo afirma un texto | Evidencia citada |
| `testimonio` | Lo contó alguien | Evidencia citada |
| `supuesto` | Lo creemos sin respaldo suficiente | Pregunta abierta |
| `no_sabemos` | No hay respuesta | Pregunta abierta |

Una hoja puede citar un texto y seguir siendo `supuesto` si ese texto no basta.

## Cuándo parar

Una rama se detiene al llegar a una hoja, o cuando otro «¿por qué?» no cambiaría qué producimos ni qué medimos. El árbol se hace una vez por mecanismo; cada hook lo hereda.

`python pipeline/pipeline.py arbol M-001` muestra el árbol y qué porcentaje de hojas está anclado. El umbral para considerar un árbol listo no está decidido: es decisión del propietario.

## Protocolo causal para alimentar el módulo 3

No empezar por una emoción etiquetada ni por un hook escrito. Para cada mecanismo, recorrer y cuestionar esta cadena:

**Productor específico → deseo, temor o vulnerabilidad → situación concreta → estímulo perceptible (palabra, imagen, resultado, contradicción, riesgo) → reacción emocional inmediata hipotética → pregunta/tensión que mantiene la atención → desarrollo que responde → presencia opcional de BeatGaler.**

En cada flecha preguntar **«¿por qué produciría ese efecto?»**, «¿en quién no?», «¿qué explicación alternativa existe?» y «¿qué observación podría refutarlo?». No basta con decir «provoca miedo» o «aplica Atkinson»: identificar exactamente qué se perdería, por qué importa, qué expectativa se rompe y qué vería u oiría el espectador.

**Diferenciar:**
- **Provocar** una emoción con una amenaza, contradicción, sorpresa o recompensa concreta, frente a **describir** una emoción o pedir que recuerde una.
- **Deseo** del productor frente a **estímulo** del video: el primero no garantiza el segundo.
- **Hook** (detener el scroll), **retención** (mantener y pagar la tensión) y **visita a BeatGaler** (conexión de valor): son efectos diferentes y requieren hipótesis diferentes.
- **Preferencia creativa** del propietario frente a **evidencia de audiencia**: los resultados comparables de publicaciones pesan más; no convertir gustos aislados en leyes ni guardar listas exhaustivas de preferencias.

### Relación flexible con BeatGaler

El video puede aportar valor por sí mismo, mencionar BeatGaler indirectamente, mostrarlo como herramienta, o ser un anuncio completo. El árbol **no debe obligar** a introducir BeatGaler en el hook ni a presentarlo como solución de un problema que no resuelve. Explicitar el grado de presencia comercial propuesto, la transición creíble y cualquier capacidad V2 aún no disponible. Si la conexión es débil, marcarla como tal; una pieza de alcance sin promoción directa puede seguir siendo válida.

### Pruebas de razonamiento con casos, sin sobreajuste

- «Mañana podrías perder todos los beats que has hecho en tu vida»: situación de pérdida irreversible y concreta; posible miedo inmediato; BeatGaler se conecta con almacenamiento en la nube, sin prometer respaldo infalible.
- «Tu peor beat podría ser el que más dinero te haga ganar»: contradice una expectativa sobre calidad y ventas; posible sorpresa y curiosidad; verificar que el cuerpo justifique la posibilidad.
- «¿Conoces esa sensación cuando terminas un beat...?»: pide recordar orgullo, pero no demuestra que el estímulo provoque orgullo en el momento.
- «Alguien podría hacerse famoso con tu beat y tú no recibir ni el crédito»: tensión potente, pero BeatGaler no garantiza atribución ni evita robos.

Son **ejemplos de diagnóstico creativo**, no resultados de audiencia ni fórmulas obligatorias. Buscar mecanismos y situaciones nuevas; no limitarse a imitar estos ejemplos.

### Criterio de salida al módulo 3

Un mecanismo está **listo para proponer candidatos** cuando declara la cadena causal, al menos una explicación alternativa, una condición de fallo, una pregunta refutable y la fuerza real de su evidencia. Las partes sin respaldo se etiquetan `supuesto`/`no_sabemos` y enlazan a preguntas abiertas conforme al esquema existente. Esto **no** equivale a estar validado ni a autorización para producir. El umbral cuantitativo de hojas ancladas sigue sin decidirse; no inventarlo.

Mantener `mecanismos.csv`, `nodos.csv` y la trazabilidad actual sin migraciones ni cambios de identificadores. El árbol M-001 «Autoexamen» es histórico y no autoriza reutilizar el hook rechazado «400 beats. Name ten.».
