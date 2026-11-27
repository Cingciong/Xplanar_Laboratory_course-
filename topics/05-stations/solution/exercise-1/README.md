# Topic 5 - exercise 1 solution (simulation)

4 movers run between stations 1-5 like in the Starter Kit demo (process rotations at stations 1, 2, 3; switch = station 4; merge = station 5) with dynamic routing to station 2 or 3 (`FB_Routing`, mode `fbRouting.eMode`).
No station 6.

Open `XPlanarPusty.sln`, target = `<Local>`; `maxNumMover` = 4, `maxTrackCount` = 3. Link in MOTION -> Groups: `XPlanar` -> `fbXPlanarSystem.group`, `Environment` -> `fbXPlanarSystem.environment`, `Track1/2/3` -> `fbTrackStandard[1/2/3].stTrackRef`, axes -> `fbXPlanarMover[n].stMoverRef`. Track objects are empty, geometry is built in code (`BuildTrack`).
Built with 0 errors; not verified on the simulation yet.
