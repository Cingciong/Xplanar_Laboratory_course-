# XPlanar lab topics

| Instruction chapter | Folder |
|---|---|
| 1 Introduction | `T01_introduction/` |
| 2 Configuration and startup | `T02_configuration/` |
| 3 Controlled motion | `T03_motion/` |
| 4 Tracks and collision avoidance | `T04_tracks/` |
| 5 Dynamic routing to stations | `T05_stations/` |

## Naming

- Topic folder: `TNN_name`.
- Inside: `start/`, `solution/` (single solution) or `solution_exercise_N/`.
- Inside each of them: `simulation/` and `hardware/`.
- Solution and TwinCAT project: `TNN_<start|EN>_SIM` or `_HW` (e.g. `T04_E2_SIM.sln`); `TNN_SIM` for a single solution.
- PLC project: `PLC` (the demo keeps the Beckhoff name).
- Every folder level has a short `README.md` in English: topic, task folder, and each `simulation` / `hardware`.
