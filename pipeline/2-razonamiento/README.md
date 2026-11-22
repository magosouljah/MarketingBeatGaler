# 2. Razonamiento

**Responsabilidad:** explicar por qué algo captaría la atención de un productor y lo llevaría a BeatGaler, preguntando «¿por qué?» hasta que cada rama termine en algo declarado.

| | |
| --- | --- |
| Entra | `evidencia.csv` y `preguntas.csv` del módulo 1 |
| Sale | `mecanismos.csv` (uno por explicación) y `nodos.csv` (su árbol) |

## Cómo es un árbol

Un mecanismo tiene cinco ramas obligatorias: `mecanismo`, `audiencia` (quién sí y quién no), `fallo` (cuándo deja de funcionar), `alternativas` (qué más explicaría el efecto) y `camino` (cómo llega a BeatGaler).

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
