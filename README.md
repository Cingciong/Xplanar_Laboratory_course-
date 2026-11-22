# XPlanar — laboratoria TwinCAT 3

Zestaw ćwiczeń laboratoryjnych i instrukcji dydaktycznych dla stanowiska transportowego Beckhoff XPlanar (praca inżynierska, Politechnika Gdańska, WETI).

## Zawartość

| Folder | Co zawiera |
|---|---|
| `instrukcja/` | Instrukcja laboratoryjna w LaTeX (`main.tex`, `main.pdf`), zrzuty ekranu, zasady stylu (`STYL.md`) |
| `demo/` | Projekt demo Starter Kit (`StarterkitBase.tsproj`, TwinCAT 3.1.4026.27); ta sama kopia z plikiem `.sln` jest w `topics/01-introduction/demo/` |
| `topics/` | Kody do ćwiczeń: dla każdego zagadnienia `start/` (wersja dla studenta) i `solution/` (rozwiązanie) |
| `setup/` | `setup.config` — eksport pakietów TcPkg do odtworzenia środowiska |
| `PRZEGLAD.md` | Przegląd struktury repozytorium |

Zagadnienia: wstęp i demo, konfiguracja systemu, ruch w 6 DoF, tracki i omijanie kolizji, dynamiczne trasowanie (stacje).

## Środowisko (komputer referencyjny)

- Windows 11 Pro 10.0.26200, wirtualizacja (VBS, Hyper-V) wyłączona.
- TcPkg 2.4.77, feed Beckhoff Stable.
- TwinCAT XAE: `TwinCAT.Standard.XAE` 4026.27.0, `TwinCAT.XAE.Shell64` 7.21.11.
- Runtime: `TwinCAT.Standard.XAR` 4026.18.0 oraz pakiety `.KM`: Realtime 2.4.14, DriversBase 3.32.0, PLC 2.4.12, NCPTP 3.1.5049, AdvancedMotion 3.4.67.
- XPlanar: `TF5890.XPlanar.XAE` 5.1.3, `TF5400.AdvancedMotionPack.XAE` 4.0.17, `TwinCAT.XAE.TMX.XPlanar` 5.1.25, `TwinCAT.XAE.XPlanar.Config` 4.5.47.
- Biblioteki w demo: Tc3_XPlanarUtility 5.1.4, Tc3_Mc3PlanarMotion 4.0.17, Tc3_Physics 4.0.17, Tc3_Module 3.4.7, Tc3_EventLogger 3.3.15, Tc2_EtherCAT 3.8.2, Tc2_IoFunctions 3.4.9, Tc2_MC2 3.3.75, Tc2_Math 3.5.3, Tc2_Standard 3.4.7, Tc2_System 3.10.2, Tc2_Utilities 3.10.9.
- `Tc3_XPlanarStandard` (3.3.2411.0, 3.3.2505.0) nie jest dostępna w TcPkg. Trzeba ją wgrać ręcznie do Library Repository (`C:\ProgramData\Beckhoff\TwinCAT\PlcEngineering\Managed Libraries\Beckhoff Automation GmbH\Tc3_XPlanarStandard\`).

### Odtworzenie środowiska

Na nowym komputerze (po zalogowaniu do feedu Beckhoffa), z katalogu repozytorium:

```
tcpkg install setup/setup.config
```

Po zmianie wersji pakietów na komputerze referencyjnym odśwież plik: `tcpkg export -o setup/setup.config`. Składnia: `tcpkg install --help`. Bibliotekę `Tc3_XPlanarStandard` wgraj ręcznie (patrz wyżej).

## Uruchomienie dema

1. Otwórz `topics/01-introduction/demo/StarterkitBase.sln` w TcXaeShell (albo `demo/StarterkitBase.tsproj`).
2. W obiekcie XPlanar ustaw `OperationMode`: `Normal` (maszyna) albo `BasicSimulation` / `AdvancedSimulation` (symulacja).
3. W symulacji ustaw urządzenia I/O (EtherCAT, USB) na `Disable`, target `<Local>`.
4. Wykonaj Activate Configuration, zaloguj się do PLC i uruchom program.

Szczegóły i typowe błędy: rozdział „Odpalenie projektu” w instrukcji.

## Laboratoria

Każde zadanie w `topics/` ma `start/` (wersja dla studenta) i `solution/` (rozwiązanie). Treść zadania jest w `README.md` danego folderu i w odpowiednim rozdziale `instrukcja/main.pdf`.

| Lab | Folder | Co otworzyć | Stan kodu |
|---|---|---|---|
| 1 Wstęp | `topics/01-introduction/` | `demo/StarterkitBase.sln` | gotowy (demo) |
| 2 Konfiguracja i włączenie | `topics/02-configuration/` | `start/TwinCAT Project1/TwinCAT Project1.sln` | pusty projekt startowy |
| 3 Ruch wysterowany (6 DoF) | `topics/03-motion/` | `start/` | do uzupełnienia |
| 4 Tracki — jeden track, dwa movery | `topics/04-tracks/task-1-one-track-two-movers/` | `start/` | do uzupełnienia |
| 4 Tracki — dwa tracki z przecięciem | `topics/04-tracks/task-2-two-tracks-crossing/` | `start/` | do uzupełnienia |
| 5 Stacje (dynamiczne trasowanie) | `topics/05-stations/` | `start/` | do uzupełnienia |

Jak przejść zadanie:

1. Otwórz `.sln` z folderu `start/` w TcXaeShell.
2. Ustaw tryb jak w demo (`BasicSimulation` bez maszyny, `Normal` na stanowisku) i target.
3. Uzupełnij kod PLC zgodnie z treścią zadania.
4. Build, Activate Configuration, Login, Start; sprawdź ruch w wizualizacji lub w XPlanar Configurator (Live View).
5. Porównaj z `solution/`.

## Kompilacja instrukcji

`pdflatex main.tex` w folderze `instrukcja/` (dwa przebiegi). W VS Code: rozszerzenie LaTeX Workshop, ustawienia w `.vscode/`.

## Licencja

MIT (plik `LICENSE`). Dokumentacja Beckhoffa i biblioteki producenta podlegają licencjom Beckhoffa.
