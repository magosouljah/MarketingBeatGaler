# old-beats-h2 — «Before buying another melody pack, listen to some of your old beats.» (C-C1-H2)

Variante de [old-beats](../old-beats/README.md): mismo cuerpo de locución y mismo CTA, proyecto independiente. 1080×1920, 30 fps, 29.23 s. Brief del cuerpo: [old-beats/BRIEF.md](../old-beats/BRIEF.md). Técnicas: [pipeline/video](../../../pipeline/video/TECNICAS.md).

Todo lo que distingue a esta versión está en [`project/js/variant.js`](project/js/variant.js); el resto de módulos es idéntico al de [old-beats-h3](../old-beats-h3/) y sale del proyecto original parametrizado (que no se tocó).

| Qué | Aquí |
| --- | --- |
| Fondo | Negro |
| Intro | Ficha de un melody pack ficticio en el «ahora» de la línea del tiempo; el cursor llega al botón y no compra. La cámara lo deja atrás, pasa despacio por YOUR OLD BEATS y se detiene en bosque (2023) |
| Tipografía del hook | BEFORE / BUYING / ANOTHER sobre la ficha; YOUR / OLD / BEATS anclado a la regla |
| Notas | «Stuck again», «Pack #9», «First sale», «Made 200 beats», «Forgot this one» junto a bosque |
| Gallery | bosque en la columna izquierda, con otra portada y otras vecinas |
| FL | Beat viejo desde 9.50 s, beat nuevo desde 4.02 s (igual que el original) |
| Drag & drop | El clip cae por debajo, con más peso y retraso |
| Subtítulos | Amarillos |
| Cierre | Tarjeta final alineada a la izquierda |

Tiempos: hook 0.00–3.64 · «Your mixing…» 3.69–9.55 · cámara en bosque 4.90 (F147) · beat viejo 6.93 (F208) · batería 8.78 (F263, en «fire») · arrastre 11.75–17.75 · beat nuevo 17.85 (F536) · rueda 24.57 (F737) · CTA 24.59–28.04.

```bash
bash tools/prepare.sh && bash tools/render.sh     # con el material en inputs/ (ver inputs/README.md)
```
