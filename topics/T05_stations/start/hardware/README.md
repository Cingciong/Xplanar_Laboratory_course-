# Topic 5 start, hardware

`Normal` mode, real stand, 12 tiles, 4 movers.

## What it does

Starting point of topic 5 (same program as topic 4, exercise 2).

4 movers drive in loops on three tracks. `Main` is shared; at its end a mover goes to `Top` or `Bottom` (upper movers use `Top`, lower ones `Bottom`) and returns to `Main`. Collision avoidance keeps the gap (`fGap` = 200 mm).

Start-up: reset -> group, environment and tracks -> enable movers -> join tracks.

## Run

1. Open `T05_start_HW.sln`, platform `TwinCAT RT (x64)`, target = the XPlanar controller.
2. Make sure the table is clear.
3. *Activate Configuration* and switch to Run Mode.
4. Log in to the PLC and press *Start*.

## Notes

- On a motion error see `nErrorStep` and `nErrorID` in `MAIN.fbMotionSystem`.
