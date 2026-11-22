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

No empezar por una emoción etiquetada, un hook escrito ni un requisito de diversidad. Primero explicar **qué valor o consecuencia** tiene la situación para un productor concreto. Para cada mecanismo, recorrer y cuestionar esta cadena:

**Productor específico ↔ deseos y conflictos ↔ situaciones ↔ estímulos perceptibles (palabra, imagen, resultado, pregunta, riesgo o demostración) ↔ reacción, utilidad o curiosidad hipotética ↔ desarrollo que cumple la promesa ↔ posible relación con BeatGaler.** No hay una sola ruta causal ni es obligatorio provocar una emoción intensa. **Si no sabemos por qué la consecuencia importa o qué respuesta puede suscitar el estímulo, todavía no hay idea lista para guion.**

Preguntar **«¿por qué?»** en varias direcciones: por qué importa el deseo, por qué ocurre la situación, por qué ese estímulo importaría, qué otro resultado es posible y por qué cambiaría la atención. Además, «¿en quién no?», «¿qué explicación alternativa existe?» y «¿qué observación podría refutarlo?». No basta con decir «provoca miedo» o «aplica Atkinson»: identificar exactamente qué se perdería, por qué importa, qué expectativa se rompe y qué vería u oiría el espectador.

**Diferenciar:**
- **Provocar** una emoción con una amenaza, contradicción, sorpresa o recompensa concreta, frente a **describir** una emoción o pedir que recuerde una.
- **Deseo** del productor frente a **estímulo** del video: el primero no garantiza el segundo.
- **Hook** (detener el scroll), **retención** (mantener y pagar la tensión) y **visita a BeatGaler** (conexión de valor): son efectos diferentes y requieren hipótesis diferentes.
- **Preferencia creativa** del propietario frente a **evidencia de audiencia**: los resultados comparables de publicaciones pesan más; no convertir gustos aislados en leyes ni guardar listas exhaustivas de preferencias.

### Relación flexible con BeatGaler

El video puede aportar valor por sí mismo, mencionar BeatGaler indirectamente, mostrarlo como herramienta, o ser un anuncio completo. El árbol **no debe obligar** a introducir BeatGaler en el hook ni a presentarlo como solución de un problema que no resuelve. Explicitar el grado de presencia comercial propuesto, la transición creíble y cualquier capacidad V2 aún no disponible. Si la conexión es débil, marcarla como tal; una pieza de alcance sin promoción directa puede seguir siendo válida.

### Entrega mínima al módulo 3

En una frase por elemento: **deseo concreto → consecuencia relevante → situación → estímulo → reacción/curiosidad hipotética → por qué → evidencia o supuesto → qué lo refutaría**. No exigir una emoción intensa: también sirven utilidad, humor, demostración o una pregunta interesante. Profundizar el árbol solo donde la incertidumbre cambie una decisión.

### Criterio de salida al módulo 3

Un mecanismo está **listo para proponer candidatos** cuando declara la cadena causal, al menos una explicación alternativa, una condición de fallo, una pregunta refutable y la fuerza real de su evidencia. Las partes sin respaldo se etiquetan `supuesto`/`no_sabemos` y enlazan a preguntas abiertas conforme al esquema existente. Esto **no** equivale a estar validado ni a autorización para producir. El umbral cuantitativo de hojas ancladas sigue sin decidirse; no inventarlo.

Mantener `mecanismos.csv`, `nodos.csv` y la trazabilidad actual sin migraciones ni cambios de identificadores. El árbol M-001 es histórico y no constituye un candidato activo de generación.

## Relevancia antes de converger

No partir del mecanismo histórico por inercia. Recorrer las ramas del deseo que sean pertinentes (sin cuota de raíces): comparar perspectivas, momentos, consecuencias y medios **solo cuando añada valor**. Descubrir rutas alternativas, pero descartar ideas triviales o vagas aunque sean nuevas. Enviar al módulo 3 solo las situaciones con una consecuencia identificada, un estímulo plausible, un porqué causal y su mayor objeción. Primero puede explorarse sin dar de alta un árbol completo para cada idea; **solo los mecanismos de las ideas seleccionadas** se formalizan en `mecanismos.csv` y `nodos.csv` con las cinco ramas, antes de registrar hipótesis.
