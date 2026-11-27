# Topic 3 exercise 1, hardware

`Normal` mode, real stand, 12 tiles, 4 movers.

## What it does

The PLC enables the movers automatically: `Startup` (register movers) -> `Starting` (reset, then enable).

## Run

1. Open `T03_E1_HW.sln`, platform `TwinCAT RT (x64)`, target = the XPlanar controller.
2. Make sure the table is clear.
3. *Activate Configuration* and switch to Run Mode.
4. Log in to the PLC and press *Start*.
5. The movers lift and stay enabled.

## Notes

- `nStartingSequence = 90` means reset or enable failed. Fix the cause, then *Reset cold* and *Start*.
