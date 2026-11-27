# Topic 5 - solution, exercise 1

Stations 1-5 with dynamic routing to station 2 or 3 (`FB_Routing`, mode `fbRouting.eMode`).

Links in *MOTION > Groups*: `XPlanar` -> `fbXPlanarSystem.group`, `Environment` -> `fbXPlanarSystem.environment`, `Track1/2/3` -> `fbTrackStandard[1/2/3].stTrackRef`; axes -> `fbXPlanarMover[n].stMoverRef`. Track objects are empty, the geometry is built in code (`BuildTrack`).

- `simulation/` - runs on a PC
- `hardware/` - runs on the real stand
