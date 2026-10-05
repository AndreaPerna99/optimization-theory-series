# Open Questions

To be answered by the author before the related episodes are scripted. Each episode README also marks its own open points with **[CONFIRM]**; `./kg status` counts them per episode. When a question is answered, write the answer into the episode README (and remove its [CONFIRM] marker) and strike it here.

1. **Quadrotor (Ep 0, 9, maybe 10):** hardware or simulation? Which controller (MPC, LQR, cascaded PID, other)? Was RL ever used on it? What footage exists?
2. **SAR robots (Ep 8):** platform, number of robots, simulation or real? Which algorithms (consensus on what quantity, coverage formulation, task allocation)? What results and footage can be shown?
3. **Camera calibration (Ep 5):** own setup and data, or simulated?
4. **Sensitivity research (Ep 4):** include a short example or leave it out entirely? Is it publicly shareable?
5. **Audience:** confirm the target viewer described in [SERIES.md](../SERIES.md#audience-and-style).
6. **Narration voice:** own voice or TTS (Piper, Kokoro, ElevenLabs were used before)?
7. **Language:** English only, or also Italian subtitles or versions?
8. **Footage storage:** raw and finished footage is not versioned in git (see [PRODUCTION.md](PRODUCTION.md#footage-and-large-files)). Where does the master copy live: an external drive, cloud storage, or Git LFS?
9. **Brand:** is the channel name the same as the series name? Logo, brand font (for `gradkit/style.py` and `shared/fonts/`), thumbnail style, intro/outro sting?
10. **Palette:** the colours in `gradkit/style.py` are provisional; fix them during the Episode 1 pilot (and check them for colour-blind readability).
