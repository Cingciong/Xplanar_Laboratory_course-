# Instruction style (`main.tex`)

Model: the sections about the TwinCAT XAE Shell environment and the SK12 demo code (Introduction). New and revised parts follow them.

## General rules
- The instruction is written in Polish: short, factual sentences. No lectures the author did not ask for.
- **No content added on your own initiative.** The author decides what is written. Mark gaps with `\opisDoUzupelnienia{}`.
- Mark uncertain statements in italics as to be checked. Describe sources not confirmed by Beckhoff documentation in `\uwaga{}`.
- One chapter per topic (5). No own numbered subtopics such as 2.1.

## Chapters and headings
- `\chapter` = topic, `\section` = main blocks, below that unnumbered `\podrozdzial{...}` and `\podpodrozdzial{...}` (both listed in the table of contents).
- Order inside a block: **short introduction, screenshot, description of what it shows** (list).
- Describe the Solution Explorer parts in turn: SYSTEM, MOTION, I/O, PLC, each with its own heading.
- Rules and context first, good practices (for example naming) at the end.
- End a chapter with `\subsection*{Dokumentacja Beckhoff (Infosys)}` and a list of clickable titles (`\href`).

## Lists and sentences
- Avoid nested brackets; use a separate sentence or a dash.
- Definitions: `\textbf{Name} --- short description.` in one sentence.
- Mark statements about the current state with "(currently: ...)" so it is clear which element is meant.
- Program and TwinCAT names in `\texttt{}`; new terms in italics with a translation in brackets.

## Screenshots
- Macro `\zrzutEkranu[width]{path relative to images/}{caption}`.
- Short captions, for example `Solution Explorer --- SYSTEM`.
- File names: lower case, hyphens, no Polish characters or spaces, e.g. `solution-explorer-plc-code.png`.
- Folder: `images/<NN-chapter>/<section>/`, e.g. `images/01-introduction/project-parts/`.
- Figures are fixed in place (`[H]`).

## Technical
- Build: `pdflatex` twice (table of contents). In VS Code: LaTeX Workshop, build on save (`.vscode/settings.json`).
- The author edits the file by hand (auto save). Make targeted changes; do not overwrite whole blocks.
- In generated scripts use raw strings: backslashes and `\t` are easy to break.
