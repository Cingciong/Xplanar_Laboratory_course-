# Repository review: structure, thesis chapters, literature, documentation

State of 2026-10-13, describing the **earlier working repository** (`Xplanar_inzynierka`), not the layout of this one. Thesis topic: *Development of laboratory exercises and a teaching instruction for the Beckhoff XPlanar transport stand*. The ratings are the reviewer's opinion; not all 174 PDFs were read in full.

## 1. Map

```
Xplanar_inzynierka/
|- README.md, TODO.md          summary README (partly outdated) and the plan of 5 labs
|- 26.08.10_StarterkitBase.tnzip   Beckhoff starter kit archive
|- thesis/                     written thesis
|  |- outline.md, README.md    thesis plan and folder layout
|  |- guidelines/              faculty guidelines 2026, rector's order 45/2024, summary
|  |- template-pl/, template-en/   LaTeX templates (LuaLaTeX)
|  |- comparison/competitors.md    XPlanar competitors
|  |- materials/               literature (174 PDF, about 570 MB), by chapter
|- instrukcja/                 lab instruction (LaTeX), future appendix
|- topics/                     lab code (start/ and solution/)
|- kontekst/                   working material from earlier work: 2 PLC project branches, Beckhoff docs, handoff notes
```

## 2. Thesis chapters and materials

Plan from `thesis/outline.md`: 1 Introduction, 2 Theory, 3 Existing solutions, 4 XPlanar capabilities, 5 Exercises, 6 (empty), 7 Summary, Appendices.

| Ch. | Folder in `thesis/materials/` | Content | PDFs | Source notes |
|---|---|---|---|---|
| 1 | `1-introduction/` | Industry 4.0, flexible manufacturing, labour market (Barometr zawodow 2026), Industry 4.0 labs, applications (micro-assembly, pharma) | 9 | none |
| 2 | `2-theory/planar-motor-physics/` | Planar motor physics: commutation, Halbach arrays, Hall sensors, levitation control, PhD theses (Jansen, van Lierop), classic patents (Sawyer 1968, Trumper) | 28 | none |
| 2 | `2-theory/xplanar/` | Beckhoff patents (stator, mover, sensors, collisions), UBC base, papers (Janning, Hartmann, SOLEIL, Lund) | 34 | **`sources.md` (39 KB, every item described)** |
| 3 | `3-existing-solutions/direct-2d/` | Planar competitors: Bosch Rexroth ctrlX FLOW6D, Planar Motor, patents, Waterloo | 13 | none |
| 3 | `3-existing-solutions/indirect-linear/` | Linear systems: ATS SuperTrak, Rockwell iTRAK/MagneMover/QuickStick, XTS, MCS, patents | 27 | none |
| 4.1 | `4-xplanar-capabilities/trajectories/` | Path planning: MAPF/CBS, MPC, minimum-jerk, Ruckig, CBF, TF5430 manual, Lund and Ghent works | 24 | none |
| 4.2 | `4-xplanar-capabilities/communication/` | OPC UA, MQTT, PROFINET, TSN, cycle time | 6 | none |
| 5 | `5-lab-exercises/` | Teaching: Kolb, Biggs (constructive alignment), CDIO, ECTS, Polish qualification frameworks, virtual labs, PBL, course cards | 25 | none |
| 7 | `7-summary/` | README skeleton only | 0 | n/a |
| app. | `appendices-lab-instructions/` | points to `instrukcja/` | 0 | n/a |

Also: `thesis/comparison/competitors.md` (5 KB) compares competitors and notes that several brands use Planar Motor Inc. technology; it states "no data" where data is missing. `thesis/guidelines/guidelines-summary.md` (2.7 KB) summarizes the formal requirements (Arial 10 pt, 1.5 spacing, PN-ISO 690, GenAI statement, chapter layout).

## 3. Labs: instruction, code, plan

**`TODO.md`** (teaching plan) is the most valuable concept document. Five labs in order:

1. Introduction (demonstration on the machine, SK12 demo, `BasicSimulation` on a laptop)
2. Configuration and startup (backup, packages, EtherCAT, levitation)
3. Controlled motion (6 DoF: `MoveToPosition`, `MoveZ`, `MoveA/B/C`)
4. Tracks and collision avoidance (Group, error 33158, 2 tasks)
5. Dynamic routing (stations, switches)

It gives teaching reasons, concrete parameters and honest notes about limitations.

**`instrukcja/`** (at that time): LaTeX document (636 lines, with PDF), 6 steps, screenshot macro with placeholders, style file, screenshots for chapters 1 and 2. Later chapters were mostly a skeleton.

**`topics/`** (at that time): real code only in the demo and in an empty configuration project; the other READMEs said "code to be written".

## 4. Technical documentation (`kontekst/`)

| Element | What it is | Value |
|---|---|---|
| `kontekst/dokumentacja/*.pdf` | Official Beckhoff DRAFT manuals for `Tc3_XPlanarStandard` and `Tc3_XPlanarUtility` | Key source of truth for the exercises |
| `.../error_codes.md` | XPlanar error code sheet (13 KB) | Very practical for students |
| `.../readme.md` | From zero to moving movers: symptom, cause, solution (12 KB) | Very good base for the instruction and ch. 5 |
| `.../latex/` | 9 LaTeX chapters: system, PLC, environment, diagnostics, problems, log (110 KB), mover detection, shared zone, BTN | Ready knowledge, not organized |
| `.../html/DMMS_architecture.html` | Application architecture diagram | Visual help |
| `.../setup_env/` | Package install script, `setup.md`, `Tc3_XPlanarStandard` library (3.3.2411.0, 3.3.2505.0) | Needed to rebuild the environment |
| two `dmms-...` folders | Two complete TwinCAT projects from earlier work | Architecture reference, not direct exercise material |
| `kontekst/.claude/handoffs/` | Code analysis notes (architecture, bugs, dependency on an external PC) | Saves weeks of reading code |

## 5. Usefulness for the thesis

- **High:** `2-theory/xplanar/sources.md` and patents (base for ch. 2 and part of ch. 3); `5-lab-exercises/` (justifies the teaching approach); `TODO.md` with the instruction and documentation (the author's own contribution); `trajectories/` (scientific context for 4.1).
- **Medium:** `planar-motor-physics/` is very broad, a few items are enough (Jansen, van Lierop, Kim and Trumper, Xia 2004, Mikroniek); `3-existing-solutions/` has good data but `competitors.md` is short; `communication/` does not cover ADS/pyads, which the project really uses.
- **Low / risk:** `kontekst/` as a whole (about 80k files) clutters the repository; many scanned patents have no text layer.

## 6. Readability and consistency

**Good:** chapter folders match the thesis plan; consistent English names; `autor-year-topic.pdf` file names; `sources.md` is a model; short guideline summary; `TODO.md` and the style file are concrete.

**Problems, most serious first:**
1. Incomplete bibliography: only one of eight folders has source notes and the `.bib` has 4 template entries.
2. Outdated main README with folders that do not exist; check the encoding is UTF-8.
3. Inconsistent chapter numbering between `outline.md`, `7-summary/README.md` and the template.
4. Chapter READMEs are almost empty.
5. The same knowledge is spread over several files with no leading one.
6. Size: about 570 MB of PDFs and 80k files make syncing slow; move PDFs out of git or ignore them.
7. Working leftovers: build logs, `.vs/`, broken files, a loose `.tnzip` in the root.
8. No clear line between the thesis contribution and the reused context.

**Ratings (1-5):** literature completeness 4; literature indexing 2; folder structure 4; documentation consistency 2.5; practical part 3; overall usefulness 4.

## 7. Recommended next steps

1. Settle the chapter numbering and fix `7-summary/README.md` and `outline.md`.
2. Write `sources.md` for the other folders and move entries into the `.bib`.
3. Update the main README with the right paths.
4. Fill chapter READMEs: what is here, 3-5 key sources, what still has to be read.
5. Remove working files; move `.tnzip` archives to their own folder.
6. Add sources on ADS/pyads and EtherCAT for chapter 4.2.
7. Decide what to do with `kontekst/`: a separate repository or a list of what was reused.
