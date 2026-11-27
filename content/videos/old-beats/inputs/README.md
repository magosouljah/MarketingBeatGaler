# inputs/ — material fuente que NO va al repositorio (público)

| Archivo | Qué es |
| --- | --- |
| `beat_viejo.mp4` | Grabación real de FL Studio del beat antiguo (`bosque.flp`, 130 BPM, 16.8 s). La melodía es ZENOLOGY en Track 1. |
| `beat_nuevo.mp4` | Grabación real del beat nuevo (`bosque pero jerk.flp`, 143 BPM, 15.5 s). La melodía cae en Pattern 2 de Track 1. |
| `vo_hooks_body.mp3` | Locución de ElevenLabs con los tres hooks y el cuerpo compartido. |
| `vo_cta.mp3` | Locución del CTA: «Comment gah-LERR to store all your beat history online». |
| `C-H1.wav`, `C-H2.wav`, `C-H3.wav` | Los tres hooks cortados de `vo_hooks_body.mp3` (0.00–2.80, 3.18–6.82, 7.06–9.44 s). |
| `C-C1a.wav`, `C-C1b.wav`, `C-C1c.wav` | Las tres frases del cuerpo (9.70–15.56, 15.85–19.13, 19.29–21.89 s). |
| `C-CTA.wav` | El CTA completo (0.00–3.45 s de `vo_cta.mp3`). |

Los cortes se hicieron por silencios (`silencedetect`) y se comprobaron con `shared/transcription/align_words.py`.
