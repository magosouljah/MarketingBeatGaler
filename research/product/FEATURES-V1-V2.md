# Features de BeatGaler — V1 y V2

**Estado:** lista aportada por el propietario el 21 de noviembre de 2026. Sirve para saber qué se puede mostrar en los videos. **V2 puede cambiar**: cuando cambie, se actualiza este archivo.

## Regla para los videos (decisión del propietario, 2026-11-21)

- Un video puede mostrar cualquier feature de **V1** o de **V2**, aunque la app publicada siga en V1.
- **No se inventan features fuera de estas dos listas.**
- Si un video necesita una feature que no está aquí, se le propone al propietario. Si él la agrega a V2, entra en esta lista y entonces se puede usar.
- El «Share» del video [`fuck`](../../content/videos/fuck/) corresponde a los espacios compartidos de V2 (Quick Packs y Cowork). El menú de V1 no lo tiene.

## Origen y límites

- Lista elaborada a partir de [`magosouljah/beatgaler-arq`](https://github.com/magosouljah/beatgaler-arq) (mapa de sistemas e investigaciones P01–P07) y del contexto de producto del propietario; él la entregó tal cual.
- V1 está sustentada en código documentado, **no** en una prueba manual de cada función.
- V2 es visión y decisiones anteriores: no está implementada ni es un roadmap oficial.
- Este archivo no modifica `DIRECCION.md` ni la aplicación.

---

## **V1 — BeatGaler actual**

Implementada en código

### **1. Cuentas y usuarios**

1. Registro con correo electrónico.
2. Verificación de correo.
3. Inicio de sesión con correo y contraseña.
4. Autenticación con Google y X.
5. Recuperación de contraseña.
6. Autenticación de dos factores (MFA).
7. Códigos de recuperación de MFA.
8. Cambio de correo con verificación.
9. Administración y revocación de sesiones.
10. Cierre de sesión y protección de cuenta.

### **2. Gallery y organización**

11. Biblioteca privada de beats por usuario.
12. Gallery visual con portadas.
13. BeatCards con nombre, estrellas, BPM, Key y tags.
14. Búsqueda textual de beats.
15. Filtrado por tags incluidos y excluidos.
16. Combinación de tags con lógica ANY/ALL.
17. Ordenamiento por nombre, BPM, estrellas y orden manual.
18. Barra de tags interactiva.
19. Renombrado global de tags, incluyendo beats en papelera.
20. Scroll infinito virtualizado, sin paginación visual.
21. Navegación mediante URL, con compatibilidad para enlaces antiguos.
22. Selección individual y múltiple de beats.
23. Selección global de resultados, incluso si no están cargados en pantalla.
24. Edición masiva de metadatos y envío masivo a papelera.

### **3. Archivos y edición**

25. Subida de beats mediante botón o arrastrar y soltar.
26. Importación y revisión de archivos antes de guardarlos.
27. Almacenamiento de audio MASTER/MP3.
28. Almacenamiento de WAV.
29. Almacenamiento de portadas.
30. Almacenamiento de archivos PROJECT.
31. Preparación automática de MASTER MP3 desde WAV.
32. Edición de nombre, tags, estrellas, BPM y Key.
33. Reemplazo de audio, portada y PROJECT.
34. Eliminación de portada sin eliminar el beat.
35. Arrastrar archivos directamente sobre una BeatCard para reemplazarlos.
36. Descarga de archivos asociados al beat.
37. Recuperación y reconciliación de transferencias interrumpidas.
38. Comprobación de duplicados de nombre.

### **4. Reproductor musical**

39. Reproducción de beats desde Gallery.
40. Playbar persistente con reproducción, pausa, progreso y volumen.
41. Adelantar y retroceder dentro del audio.
42. Siguiente y anterior.
43. Shuffle sin repetir dentro de una ronda.
44. Modos de repetición.
45. Navegación musical según los resultados filtrados.
46. Continuidad de reproducción al cambiar filtros.
47. Streaming de audio con MSE y alternativa Blob.
48. Cachés de audio y portadas para acelerar la experiencia.
49. Sistema MAIN de prefijos para acelerar el inicio de reproducción.

### **5. Papelera y seguridad de datos**

50. Enviar beats a papelera.
51. Consultar la papelera.
52. Restaurar beats.
53. Solicitar vaciado/purga mediante operaciones controladas.
54. Control de versiones y conflictos de edición.
55. Operaciones duraderas para evitar pérdidas o duplicaciones.

### **6. Suscripciones e infraestructura**

56. Planes Free, Paid Entry y Highest.
57. Límites de beats y archivos según el plan.
58. Checkout de suscripciones con Polar.
59. Portal de administración de suscripción.
60. Gestión de pagos, renovaciones y derechos de acceso.
61. PostgreSQL como autoridad del catálogo.
62. Telegram como almacenamiento de archivos.
63. Cloud y worker para verificar subidas y completar operaciones.
64. Respaldos de catálogo y mecanismos de recuperación.
65. Landing pública de BeatGaler.

**Importante:** esta lista está sustentada principalmente en código documentado, no en una prueba manual de cada función. La purga física, algunas integraciones de autenticación y la recuperación completa de bytes todavía requieren distinguir implementación de funcionamiento demostrado.

## **V2 — Futuro de BeatGaler**

Visión y decisiones anteriores. No significa que estén implementadas ni que todas estén aprobadas definitivamente.

### **1. Perfiles y galerías públicas**

1. Perfiles de productores y artistas.
2. Galerías públicas y privadas.
3. Publicación de beats seleccionados desde la biblioteca privada.
4. Visualización de portadas, tags y metadatos en perfiles públicos.
5. Búsqueda, filtros y reproducción de beats publicados.
6. Buscador de perfiles de usuarios.
7. Nombres de usuario vinculados a X.
8. Botón de contacto que abre los DM de X.

### **2. Personalización**

9. Colores y fondos personalizados de la galería.
10. Personalización del puntero/cursor.
11. Foto y apariencia de perfil personalizables.
12. Accesorios y elementos visuales desbloqueables.
13. Recompensas estéticas por logros o eventos.

### **3. Quick Packs**

14. Crear paquetes de hasta 20 beats.
15. Seleccionar los beats de un paquete sin crear una carpeta.
16. Compartir mediante enlaces.
17. Enlaces permanentes y revocables.
18. Permisos para escuchar o descargar.
19. Presentación compacta con portadas y metadatos.
20. Filtros por BPM, Key y tags dentro del pack (propuestos).
21. Escuchar beats recibidos.
22. Descargar beats con permiso.
23. Marcar beats como favoritos.
24. Guardar beats recibidos en la biblioteca propia.
25. Crear una copia independiente al guardarlos, sin vínculo con el original.
26. Heredar portada, nombre, BPM, Key y tags.
27. Permitir que el destinatario edite su copia.
28. Indicador para el productor: **Pack abierto**.
29. Indicador: **Interacción** (guardado, descarga o favorito; escuchar no cuenta).
30. Seguimiento relacionado con destinatarios y beats, con detalles aún pendientes.

### **4. Inbox musical**

31. Recibir Quick Packs directamente dentro de BeatGaler.
32. Activar o desactivar la Inbox.
33. Inbox pública o restringida.
34. Lista de remitentes autorizados.
35. Bloqueo de usuarios.
36. Solicitudes de permiso para enviar.
37. Relaciones mutuas tipo Friends, sin convertirlas en un feed social.
38. Posibilidad de permitir envíos entre Friends aunque la Inbox sea privada.
39. Requisitos mínimos de suscripción para enviar (propuesta antispam).
40. Límites de frecuencia de envío para evitar spam (cantidad exacta pendiente).
41. Acceder, escuchar, guardar y descargar contenido recibido.

### **5. Folders y Playlists**

42. Crear carpetas de beats.
43. Crear playlists.
44. Organizar mediante referencias, sin duplicar archivos.
45. Tener un mismo beat en múltiples carpetas.
46. Reorganizar colecciones sin modificar los archivos originales.

### **6. Cowork**

47. Espacios o carpetas colaborativas.
48. Compartir proyectos entre productores autorizados.
49. Editar conjuntamente nombres, tags y portadas.
50. Reemplazar o modificar archivos de audio y PROJECT compartidos.
51. Trabajar con copias independientes del beat privado original (provisional).
52. Permisos especiales para propietarios y colaboradores.
53. Referenciar material Cowork en colecciones normales (propuesto).

### **7. Comercialización**

54. Vender beats.
55. Comprar beats.
56. Gestionar licencias y derechos de compra (diseño pendiente).
57. Entregar archivos después de una compra.
58. Venta de canciones completas, como posibilidad más lejana.

### **8. YouTube y analíticas**

59. Publicación masiva de type beats en YouTube.
60. Analíticas de rendimiento de los videos.
61. Análisis de retención de audiencia.
62. Comparación del rendimiento por género musical.
63. Métricas para mejorar la publicación y comercialización de beats.

### **9. Otras ideas exploradas**

64. Historial recuperable de versiones anteriores de audio, con una idea histórica de conservar hasta 10 versiones. **No está consolidado como requisito vigente.**
65. Limpieza periódica de archivos residuales, solo con garantías de recuperación.
66. Posible almacenamiento híbrido o alternativo a Telegram cuando los ingresos lo justifiquen.

## **Lo que V2 no busca ser**

- No habrá una página tipo Explore como eje del producto.
- No será una red social tradicional.
- No habrá chat ni DM internos; el contacto directo utilizaría X.
- No se pretende crear una biblioteca de visuales independiente.
- No se desarrollará todo V2 en un solo lanzamiento.

**Conclusión:** V1 es la biblioteca privada para organizar, almacenar y escuchar beats. V2 amplía esa biblioteca hacia **compartir, colaborar, personalizar, publicar y comercializar música**.
