# Topic 5 - dynamic routing of movers to stations (solution, simulation)

Written from scratch on top of our topic-4 project (`04-tracks/solution/exercise-2`): same `FB_MotionSystem` style
(`Cycle`, `Startup`, `Starting`, `Execute`), same libraries (`Tc3_XPlanarStandard`, `Tc3_Mc3PlanarMotion`), 4 movers.
Layout and station flow are the same as in the Starter Kit demo (`01-introduction/demo`).

Open `simulation/XPlanarPusty.sln`, target = `<Local>`. `maxNumMover` = 4, `maxTrackCount` = 3.
In MOTION -> Groups: `XPlanar` -> `fbXPlanarSystem.group`, `Environment` -> `fbXPlanarSystem.environment`,
`Track1/2/3` -> `fbTrackStandard[1/2/3].stTrackRef`; axes -> `fbXPlanarMover[n].stMoverRef`.
The track objects are empty - the geometry is built in code (`BuildTrack`), like in the demo.

## Layout (same as the demo)

- Track 1 (left loop): station 1 (process, 120/360), station 5 (merge, 480/120); its end (480/600) is station 4 (separate = switch).
- Track 2 (middle, 600/480 -> 600/240): station 2 (process, 600/360).
- Track 3 (right loop): station 3 (process, 840/360).
- Tracks 2 and 3 start at the end of track 1 and end at its start.

Flow of each mover: S1 (rotate +90) -> routing decision -> S4 (switch to the chosen track) -> S2 or S3 (rotate 180) -> S5 (merge, one mover at a time) -> S1 ...

## Dynamic routing

`FB_Routing.SelectStation` returns 2 or 3 for the mover leaving station 1. The behaviour is `FB_Routing.eMode` (`E_RoutingMode`),
change it online (`MAIN.fbMotionSystem.fbRouting.eMode`): `Alternate` (demo, default), `ByMover`, `FreeStation`, `ShortestQueue`, `Priority`, `Random`.

## Not verified

Built with 0 errors (headless). Not run on the simulation yet: the empty track objects in the tsproj and the cross-track `MoveOnTrack` should be checked on first run.
