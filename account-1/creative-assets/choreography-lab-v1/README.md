# BeatGaler — Choreography Lab V1 (Fase 2, primer experimento 3D)

**Estado:** experimento técnico completo · **sin aprobación creativa** · no es el anuncio.
Resultados y evaluación: [RESULTS.md](RESULTS.md). Análisis de referencia: [PHASE2-RERUN.md](../../research/reference-analysis/apple-music-orbit-v1/PHASE2-RERUN.md).

Un solo proyecto HyperFrames editable con **tres modelos de movimiento** sobre la misma escena, las mismas 24 portadas reales y el mismo tempo, para aislar qué aporta cada decisión:

| | Estructura | Cámara | Qué prueba |
| --- | --- | --- | --- |
| **A** | Hélice **rígida**: un solo transform para las 24 portadas | Fija (`[0,0,9]`, FOV 40°) | Control negativo: lo que una órbita simple *no* explica |
| **B** | **Trayectorias individuales**: 3 estratos de profundidad (radio 2,35 / 1,75 / 1,2), velocidad angular y fase propias, orientación variada (±34° yaw, ±20° pitch), banking, salida escalonada desde un mazo, 4 portadas «héroe» que pasan junto al lente y aterrizaje en galería 4×6 | Fija (idéntica a A) | Si el movimiento de objetos crea profundidad y oclusiones sin mover la cámara |
| **C** | **Exactamente el movimiento de objetos de B** | **Animada en 3D**: empieza baja y cerca del mazo, sube por la hélice, empuja, retrocede mientras los héroes vuelan hacia el lente y aterriza en el plano maestro de B a 5,45 s (spline Hermite C¹, roll ±3°) | Qué añade la cámara cuando la coreografía de objetos ya es independiente |

Común a las tres: 720×1280, 30 fps, 6,0 s, fondo `#07070a`, niebla lineal 7–15,5 (única pista de profundidad «de iluminación»), materiales sin luz, portadas de doble cara (el dorso muestra la misma portada sin espejar, 30 % más oscura), perfil de velocidad angular global idéntico (`OMEGA_KNOTS`). Sin shaders, sombras ni bloom: la prioridad es la coreografía.

## Ver las animaciones

- `evidence/renders/variant-a.mp4`, `variant-b.mp4`, `variant-c.mp4` (render HyperFrames, calidad draft).
- `evidence/comparison-abc-side-by-side.mp4`: las tres sincronizadas y rotuladas.
- `evidence/contact-sheets/`: hojas de contacto a 5 fps y de la ventana de clímax a 10 fps.

## Editar y previsualizar

```powershell
cd account-1/creative-assets/choreography-lab-v1/hyperframes
npx --yes hyperframes@0.9.17 preview          # Studio; cambia la variable "variant" a a | b | c
npx --yes hyperframes@0.9.17 check --json
```

O sin HyperFrames: `python -m http.server` en `hyperframes/` y abrir `index.html?variant=b`.

- **Toda la coreografía** está en [`hyperframes/src/choreography.js`](hyperframes/src/choreography.js): `poseA`, `poseB`, `CAM_POS/CAM_TARGET/CAM_ROLL`, `OMEGA_KNOTS`, `buildCards()` (semilla `20261105`).
- Cada pose es función pura de `t` (sin reloj, timers ni `Math.random`). Ángulo global integrado una vez al cargar (tabla 1/1200 s).
- Three.js **0.184.0** y GSAP **3.15.0** vendorizados en `hyperframes/lib/` (sin red en render). Three.js MIT; GSAP licencia estándar sin coste.

## Renderizar y regenerar evidencia

```powershell
# las tres variantes desde la misma fuente (variables por fila en rows.json)
npx --yes hyperframes@0.9.17 render --batch rows.json --output "../evidence/renders/variant-{variant}.mp4" --batch-concurrency 1 --strict-variables --quality draft
# geometría exacta + métricas (necesita playwright + Chrome)
python tools/lab_capture.py geometry geometry.json --variants a,b,c
python tools/geometry_metrics.py geometry.json evidence/geometry-metrics.json
# desde la raíz del repo: medición de imagen con el mismo método que la referencia
python -m shared.motion_metrics.motion_field <render.mp4> <out.json>
python -m shared.reference_analysis.pipeline analyze <render.mp4> reference-runs/lab-v1/variant-x --account account-1
python account-1/creative-assets/choreography-lab-v1/tools/compare_reference.py <ref-motion.json> <ref-analysis.json> <evidence-dir> <out.json>
```

Linux sin `chrome-headless-shell` descargable: `HYPERFRAMES_BROWSER_PATH=/usr/bin/google-chrome`. Render medido: ~26 s por variante (captura por screenshot, GPU software). **Determinismo comprobado:** dos renders independientes de A dieron el mismo SHA-256 (`2ed7629a…`).

## Skills usadas (fijadas en `skillpack/catalog.json`)

| Skill | Commit | Para qué |
| --- | --- | --- |
| `beatgaler-motion-hub` (propia) | — | Ruta de Fase 2, límites y orden |
| `reference-analysis` (propia) | — | Pipeline V1 sobre la referencia y sobre los 3 renders |
| `hyperframes`, `hyperframes-cli` | heygen-com/hyperframes `4935d673` (= CLI 0.9.17) | Contrato de render, `hf-seek`/`buildReady`, `lint`, `check`, `snapshot`, `render --batch` |
| `hyperframes-registry` | `4935d673` | Revisado: el bloque `three-orbiting-cards` es exactamente una órbita rígida → base conceptual de A; carga Three.js desde CDN, aquí se vendoriza |
| `title-sequence-3d` | charlie947 `229022eb` | Three.js fijado, cámara dolly continua, todo derivado de `t`, revisión por fotogramas |
| `motion-animate` | blixvip `b8b7e23c` | 4 leyes (nada lineal, escalonado 40–120 ms, cámara nunca quieta, nada metronómico); salidas más rápidas que entradas |
| `motion-plan`, `reference-to-motion` | blixvip / charlie947 | Desglose «moves» de la referencia en mecanismos, no en copia; una idea por fase |

No usadas a propósito: `reverse-any-video` (copia una pieza; el encargo prohíbe copiar), `apple-launch-film` (estética de UI de Mac), sonido, `media-use`. No se ejecutó el «usage beacon» de telemetría de las skills de HyperFrames ni scripts de setup de terceros (regla 8 de `AGENTS.md`).

## Portadas

24 archivos de `assets/covers/` **byte-idénticos** (blob SHA de Git) a `magosouljah/BeatGaler`, rama `design/beatgaler-design-system-lab-v1`, `DESIGN/shared/assets/real-covers/` (verificado de nuevo el 2026-11-05, solo lectura). **Derechos publicitarios sin verificar**: no publicar fuera de pruebas internas.

## Estructura

```
hyperframes/        proyecto HyperFrames (index.html, src/choreography.js, lib/, assets/covers/, rows.json)
tools/              lab_capture.py (stills + geometría exacta), geometry_metrics.py, compare_reference.py
evidence/           renders, comparativa, hojas de contacto, métricas, check de HyperFrames, iteration-1/
RESULTS.md          evaluación, diagnóstico y propuestas
```
