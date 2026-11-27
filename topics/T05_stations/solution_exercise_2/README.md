# Topic 5 - solution, exercise 2

Exercise 1 plus station 6 at [240, 120] with a 6 DoF sequence (`Process6DoF`).

Links in *MOTION > Groups*: `XPlanar` -> `fbXPlanarSystem.group`, `Environment` -> `fbXPlanarSystem.environment`, `Track1/2/3` -> `fbTrackStandard[1/2/3].stTrackRef`; axes -> `fbXPlanarMover[n].stMoverRef`. Track objects are empty, the geometry is built in code (`BuildTrack`).

- `simulation/` - runs on a PC
- `hardware/` - runs on the real stand
