# Topic 3 exercise 2, hardware

`Normal` mode, real stand, 12 tiles, 4 movers.

## What it does

After enabling, mover 1 repeats a motion in all six axes:

1. drive to the table centre [480, 360] (X, Y)
2. lift to Z = 4 mm
3. rotate C to 90 deg
4. tilt A, then B by 2 deg
5. A, B and C back to 0
6. lower to Z = 2 mm
7. return to the start position

## Run

1. Open `T03_E2_HW.sln`, platform `TwinCAT RT (x64)`, target = the XPlanar controller.
2. Make sure the table is clear.
3. *Activate Configuration* and switch to Run Mode.
4. Log in to the PLC and press *Start*.

## Notes

- Tilt only while the mover is lifted. Tilting at low Z gives a following error (17744).
- On a motion error see `nErrorStep` and `nErrorID` in `MAIN.fbMotionSystem`.
