# Topic 5 - exercise 2 solution (simulation)

Exercise 1 plus station 6 at [240, 120] on track 1 (right after the merge, before station 1): the mover performs a 6 DoF sequence (`Process6DoF`: Z, C, A, B) and goes on to station 1.

Open `XPlanarPusty.sln`, target = `<Local>`; `maxNumMover` = 4, `maxTrackCount` = 3. Link in MOTION -> Groups: `XPlanar` -> `fbXPlanarSystem.group`, `Environment` -> `fbXPlanarSystem.environment`, `Track1/2/3` -> `fbTrackStandard[1/2/3].stTrackRef`, axes -> `fbXPlanarMover[n].stMoverRef`. Track objects are empty, geometry is built in code (`BuildTrack`).
Built with 0 errors; not verified on the simulation yet.
