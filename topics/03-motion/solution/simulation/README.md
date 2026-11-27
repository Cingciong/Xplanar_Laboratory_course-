# Topic 3 - end, simulation

Open `XPlanarPusty.sln`, target = `<Local>`. PLC project `Untitled1`: `MAIN` + `FB_MotionSystem` (`Cycle`, `Startup`, `Starting`) using `Tc3_XPlanarStandard`.
After PLC start `EnableMovers` enables all 4 movers. Axes are linked to the PLC; `maxNumMover = moverCount = 4`.
Needs `Tc3_XPlanarStandard` in the Library Repository. The PLC task must not share a core with the XPlanar tasks.