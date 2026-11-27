# Topic 4 - solutions

- `exercise-1/` - one closed rectangular track `Loop` made in the Configurator (exported to MOTION -> Groups -> Loop).
  The PLC code only enables the movers. Joining the track, jogging and leaving it are done by hand in the
  XPlanar Environment View / Motion UI, so this solution is described step by step in the lab instruction (chapter 4, part 1),
  not in code.
- `exercise-2/` - three tracks `Main`, `Top`, `Bottom` and 4 movers driving in loops (Top+Main, Bottom+Main) without stopping.
  `FB_MotionSystem`: `Cycle`, `Startup`, `Starting` (reset, group, environment, tracks, movers, JoinTrack), `Execute`.
  Link in MOTION -> Groups: `XPlanar` -> `fbXPlanarSystem.group`, `Environment` -> `fbXPlanarSystem.environment`,
  `Main`/`Top`/`Bottom` -> `fbTrackStandard[1]/[2]/[3].stTrackRef`. Library parameter `maxTrackCount` = 3.
