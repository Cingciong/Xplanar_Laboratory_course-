# XPlanar - TwinCAT 3 laboratory course

Lab exercises and instruction for the Beckhoff XPlanar transport stand (engineering thesis, Gdansk University of Technology).

## Contents

| Folder | Content |
|---|---|
| `instrukcja/` | Lab instruction in LaTeX (Polish): `main.tex`, `main.pdf`, screenshots, style rules |
| `topics/` | TwinCAT projects for each topic, see `topics/README.md` |
| `setup/` | TwinCAT and library versions needed to rebuild the environment |
| `PRZEGLAD.md` | Repository review notes (Polish) |

## Reference environment

- Windows 11 Pro 10.0.26200, virtualization (VBS, Hyper-V) off.
- TcPkg 2.4.77, Beckhoff Stable feed.
- TwinCAT XAE: `TwinCAT.Standard.XAE` 4026.27.0, `TwinCAT.XAE.Shell64` 7.21.11.
- Runtime: `TwinCAT.Standard.XAR` 4026.18.0 and `.KM` packages: Realtime 2.4.14, DriversBase 3.32.0, PLC 2.4.12, NCPTP 3.1.5049, AdvancedMotion 3.4.67.
- XPlanar: `TF5890.XPlanar.XAE` 5.1.3, `TF5400.AdvancedMotionPack.XAE` 4.0.17, `TwinCAT.XAE.TMX.XPlanar` 5.1.25, `TwinCAT.XAE.XPlanar.Config` 4.5.47.
- Demo libraries: Tc3_XPlanarUtility 5.1.4, Tc3_Mc3PlanarMotion 4.0.17, Tc3_Physics 4.0.17, Tc3_Module 3.4.7, Tc3_EventLogger 3.3.15, Tc2_EtherCAT 3.8.2, Tc2_IoFunctions 3.4.9, Tc2_MC2 3.3.75, Tc2_Math 3.5.3, Tc2_Standard 3.4.7, Tc2_System 3.10.2, Tc2_Utilities 3.10.9.

- `Tc3_XPlanarStandard` (3.3.2411.0, 3.3.2505.0) is not available in TcPkg. Install it manually into the Library Repository (`C:\ProgramData\Beckhoff\TwinCAT\PlcEngineering\Managed Libraries\Beckhoff Automation GmbH\Tc3_XPlanarStandard\`).

### Rebuild the environment

On a new PC (logged in to the Beckhoff feed), from the repository folder:

```
tcpkg install setup/setup.config
```

After changing package versions on the reference PC, refresh the file with `tcpkg export -o setup/setup.config`.

## Running a project

Open the `.sln` in the `simulation` or `hardware` folder and follow the `README.md` next to it.

## Building the instruction

`pdflatex main.tex` in `instrukcja/` (two passes).

## License

MIT (`LICENSE`). Beckhoff documentation and libraries are covered by Beckhoff licenses.
