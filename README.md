# XPlanar — laboratoria TwinCAT 3

Zestaw ćwiczeń laboratoryjnych i instrukcji dydaktycznych dla stanowiska transportowego Beckhoff XPlanar (praca inżynierska, Politechnika Gdańska, WETI).

## Zawartość

| Folder | Co zawiera |
|---|---|
| `instrukcja/` | Instrukcja laboratoryjna w LaTeX (`main.tex`, `main.pdf`), zrzuty ekranu, zasady stylu (`STYL.md`) |
| `demo/` | Projekt demo Starter Kit (`StarterkitBase`, TwinCAT 3.1.4026.27) |
| `topics/` | Kody do ćwiczeń: dla każdego zagadnienia `start/` (wersja dla studenta) i `solution/` (rozwiązanie) |
| `setup/` | Wersje TwinCAT i bibliotek do odtworzenia środowiska |
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

```
tcpkg export -o setup.config
tcpkg install setup.config
```

Pierwsze polecenie uruchamiasz na komputerze referencyjnym, drugie na nowym (po zalogowaniu do feedu Beckhoffa). Sprawdź składnię przez `tcpkg install --help`.

## Uruchomienie dema

1. Otwórz projekt z `demo/` w TcXaeShell.
2. W obiekcie XPlanar ustaw `OperationMode`: `Normal` (maszyna) albo `BasicSimulation` / `AdvancedSimulation` (symulacja).
3. W symulacji ustaw urządzenia I/O (EtherCAT, USB) na `Disable`, target `<Local>`.
4. Wykonaj Activate Configuration, zaloguj się do PLC i uruchom program.

Szczegóły i typowe błędy: rozdział „Odpalenie projektu” w instrukcji.

## Kompilacja instrukcji

`pdflatex main.tex` w folderze `instrukcja/` (dwa przebiegi). W VS Code: rozszerzenie LaTeX Workshop, ustawienia w `.vscode/`.

## Licencja

MIT (plik `LICENSE`). Dokumentacja Beckhoffa i biblioteki producenta podlegają licencjom Beckhoffa.
