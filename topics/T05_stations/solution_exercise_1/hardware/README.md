# Topic 5 exercise 1, hardware

`Normal` mode, real stand, 12 tiles, 4 movers.

## What it does

4 movers run through stations on three tracks:

- station 1: process, rotate
- station 4: switch to the track of station 2 or 3
- stations 2 / 3: process, rotate 180 deg
- station 5: merge, one mover at a time

Start-up: build the tracks -> reset and enable -> movers join track 1.

## Run

1. Open `T05_E1_HW.sln`, platform `TwinCAT RT (x64)`, target = the XPlanar controller.
2. Make sure the table is clear.
3. *Activate Configuration* and switch to Run Mode.
4. Log in to the PLC and press *Start*.

## Notes

- `FB_Routing` chooses station 2 or 3. Change `MAIN.fbMotionSystem.fbRouting.eMode` online: `Alternate`, `ByMover`, `FreeStation`, `ShortestQueue`, `Priority`, `Random`.
- Track geometry is built in code (`BuildTrack`).
- On a motion error see `nErrorStep` and `nErrorID` in `MAIN.fbMotionSystem`.
