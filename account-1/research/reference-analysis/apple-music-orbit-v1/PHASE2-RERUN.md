# Apple Music — reejecución Fase 2 con Reference Intelligence V1

**Estado:** análisis técnico de referencia. **No** es reconstrucción, **no** está aprobado artísticamente. Cuenta: `account-1`. Fecha: 2026-11-05.

## 1. Procedencia del archivo (medida)

| | Original documentado (`MEASUREMENTS.json`) | Archivo local `reference-runs/apple-music/source.MP4` |
| --- | --- | --- |
| SHA-256 | `74301c7f…db` | `885dc1c1c3dd641670405ba637aff5865cc7fd44cbe713614038fa4cebe64c14` |
| Bytes | 2 919 113 | 1 913 426 |
| Resolución | 512 × 910 | 720 × 1280 |
| Fotogramas | 181 (6,033 s) | 178 (5,933 s) |

**No es byte-idéntico.** Para saber si es el mismo anuncio o un sustituto, se comparó la firma temporal (diferencia media de miniaturas grises 64×64 entre fotogramas consecutivos) contra los 8 intervalos documentados:

- Mejor alineación con **desfase −3 fotogramas** (SSE 0,000148; −4: 0,000333; −2: 0,000372). Medias de intervalo a ≤ 7 % de las documentadas.
- Los tres picos de diferencia del archivo local están en los fotogramas 119, 124 y 113 = **122, 127 y 116 del original**, exactamente los picos documentados.
- Inspección visual completa: mismo anuncio (logo, abanico, corona alrededor de «Obtén / 1 mes / gratis*», barrido de primer plano, CTA).

**Conclusión (estimación, no prueba criptográfica):** es **otra codificación del mismo anuncio**, de mayor resolución, a la que le faltan los primeros 3 fotogramas (0,1 s). Tiempo local = tiempo original − 0,1 s. No es ninguno de los renders rechazados de BeatGaler. El MP4 sigue fuera de Git (`/reference-runs/` está ignorado); aquí solo hay datos derivados. Pendiente: confirmar con el propietario de dónde salió este archivo (caso `apple-orbit-phase2-rerun-v1`, check `source-identity`).

## 2. Ejecución

```bash
python -m shared.reference_analysis.pipeline analyze reference-runs/apple-music/source.mp4 reference-runs/apple-music/analysis-v2 \
  --account account-1 --annotations <annotations.json> --tracks <tracks.json>
python -m shared.reference_analysis.pipeline validate reference-runs/apple-music/analysis-v2     # PASS
python -m shared.motion_metrics.motion_field reference-runs/apple-music/source.mp4 <out.json>   # flujo denso
python -m shared.motion_metrics.klt_track   reference-runs/apple-music/source.mp4 klt-seeds.json <tracks.json>
```

Evidencia versionada en [`phase2-rerun/`](phase2-rerun/): `analysis.json`, `report.md`, `probe.json`, `provenance.json`, `manifest.json` (sin los PNG: material de terceros), `annotations.json`, `motion-field.json`, `tracks.json`, `klt-seeds.json`. Los índices de fotograma de esos archivos son **locales** (original = local + 3).

## 3. Medido vs. hipótesis

### Medido (máquina, método fijo)

Campo de movimiento denso (`shared/motion_metrics`, OpenCV Farneback + ajuste afín global sobre píxeles de primer plano en movimiento). Fases en segundos del original:

| Fase | Cobertura | Velocidad (alturas/s) | Residuo afín | CV velocidad | Coherencia | Curl (1/s) | Proxy oclusión |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Abanico 1,2–1,6 | 0,10 | 0,68 | 0,55 | 0,42 | 0,38 | 0,52 | 0,49 |
| Corona 1,6–3,0 | 0,17 | 0,62 | 0,43 | 0,41 | 0,14 | **5,76** | 0,14 |
| Ruptura + barrido 3,0–4,35 | 0,23 | 0,87 | 0,80 | 0,69 | 0,40 | 0,80 | **0,74** |
| Final 4,35–6,0 | 0,06 | 0,00 | — | — | — | — | 0,00 |

- **Arco de energía** (diferencia media de miniaturas, relativa al pico): abanico 0,29 → corona 0,55 → **clímax 1,00** → final 0,07. La pieza *acelera hacia* el clímax.
- **Corona:** curl alto (rotación dominante en el plano de imagen) y aun así 43 % del flujo no lo explica un solo movimiento afín → las portadas no se comportan como un anillo plano rígido.
- **Trayectorias KLT** (corona, fotogramas locales 60–67): la portada naranja recorre x 0,62 → 0,48 en 4 fotogramas (≈ 1,05 anchos/s hacia la izquierda por el arco inferior); la rosa grande x 0,82 → 0,64 en 7.
- **Barrido de primer plano:** el tracker pierde todos los puntos en un paso: desplazamiento mediano **112–170 px/fotograma** a 720×1280 y error ida-vuelta de 45–400 px. La velocidad de flujo de esa ventana está **subestimada**.

### Observaciones (inspección fotograma a fotograma)

- Entrada compacta e inclinada a la derecha del centro que se despliega en ~0,4 s; aún no hay anillo.
- Corona asimétrica: izquierda casi de canto (líneas), derecha con caras completas y más grandes; el centro tipográfico permanece estable.
- 3,0–3,63 s: la corona crece fuera de cuadro; arriba salen láminas finas, abajo-derecha crecen portadas frontales.
- **3,67–4,27 s: «riffle».** 3–4 portadas grandes tumbadas en perspectiva fuerte, en pila diagonal. **En fotogramas consecutivos hay portadas distintas en casi las mismas posiciones** (≈ un cambio de portada por fotograma: rosa, azul, naranja, roja, bosque en los locales 110–114).

### Hipótesis (no observables directamente)

- **H1/H2 del riffle:** (H1) cinta transportadora que avanza ≈ 1 hueco por fotograma y estroboscopia a 30 fps, o (H2) intercambio de portada por fotograma en huecos casi fijos. Ambos producen los mismos fotogramas a 30 fps. Prueba discriminante: renderizar ambos a 60 fps, diezmar a 30 y comparar con la referencia.
- La corona es compatible con portadas radiales sobre un anillo inclinado visto fuera de eje, pero no de forma única. No se infiere cámara, focal ni Z.

## 4. Mecanismos cinematográficos extraídos (para diseño original, no para copiar)

1. **Compacto → despliegue** escalonado en < 0,5 s.
2. **Asimetría de orientación**: mezclar portadas de canto y frontales crea profundidad sin iluminación.
3. **Ancla de espacio negativo** estable mientras todo gira.
4. **Aceleración hacia un clímax** donde el primer plano se llena de portadas grandes que se ocultan entre sí.
5. **Despeje rápido** a una composición quieta.

El laboratorio [`choreography-lab-v1`](../../../creative-assets/choreography-lab-v1/README.md) aplica estos mecanismos a una coreografía original (hélice vertical → peel hacia el lente → galería BeatGaler), sin la corona alrededor de texto ni el riffle de la referencia.

## 5. Límites

- Métricas 2D de imagen: no recuperan profundidad, cámara ni curvas de easing.
- **El residuo afín no distingue una órbita rígida 3D de trayectorias independientes**: el control rígido del laboratorio (variante A) mide 0,79 en su órbita. Sirve para comparar estructuras de imagen, no para probar rigidez. Para nuestras escenas la rigidez se mide con la geometría exacta (residuo Kabsch 3D).
- El fondo blanco y el texto estático de la referencia cuentan como primer plano en `coverage`.
- Audio no examinado perceptualmente.

## 6. Actualización: archivo de Instagram (2026-11-05)

El propietario pasó el MP4 descargado del post: SHA-256 `515901fed702c4f9c1f08d2ac917158201eb7bd789a8174dfaab8797c82ab74a`, 1 368 842 bytes, 720×1280, 180 fotogramas a 29,97 fps, 6,006 s. Tampoco es byte-idéntico al original documentado, pero es el más completo de los disponibles: desfase −1 fotograma (SSE 0,000155), picos en los mismos fotogramas originales 122/127/116. El `source.MP4` usado arriba es una **recodificación de este archivo** (PSNR mediano 45,7 dB con desfase de 2 fotogramas). Desde ahora es la referencia principal: `reference-runs/apple-music/instagram-original.mp4` (local, no versionado). Con él se reinterpretó la estructura como una rueda tipo rolodex: [Lab V2](../../../creative-assets/choreography-lab-v2/RESULTS.md).
