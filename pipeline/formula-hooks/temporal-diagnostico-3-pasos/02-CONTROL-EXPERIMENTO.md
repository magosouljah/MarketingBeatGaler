# Diagnóstico temporal, paso 2 — control del experimento A/B/C

Estado: pendientes las 30 evaluaciones humanas de Impacto y Naturalidad. No se han analizado resultados.

Orden ciego: 10 situaciones × 3 métodos. El orden de creación fue S01A, S01B, S01C ... S10A, S10B, S10C. Barajado reproducible con `random.Random(202611222234).shuffle(records)`, después se asignaron los IDs H001–H030. No hubo descarte por gusto ni autoevaluación.
Controles técnicos: 30 IDs, 10 tríos completos, 30 textos sin duplicados, evaluaciones vacías, duración aproximada por recuento de palabras.

**Límite de independencia:** los métodos se delimitaron por instrucciones pero se redactaron en una misma sesión de modelo, sin tres contextos computacionales independientes. No se puede afirmar independencia estricta: el ejercicio es exploratorio.
**Límite de secreto:** este repositorio es público. El archivo 02-CLAVE-PRIVADA.csv es accesible si se abre; el cegamiento exige no consultarlo antes de evaluar.
No hubo modificaciones de REGLA.md, bibliotecas, DIRECCION.md o producción. No fue posible ejecutar las pruebas globales/audit sin un clon ejecutable del repositorio; solo se verificó la integridad del lote.

Carpeta temporal; eliminación sujeta a autorización posterior.
