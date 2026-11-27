# Topic 4 exercise 1, hardware

`Normal` mode, real stand, 12 tiles, 4 movers.

## What it does

One closed track `Loop`. The PLC enables the movers; the track is used by hand.

## Run

1. Open `T04_E1_HW.sln`, platform `TwinCAT RT (x64)`, target = the XPlanar controller.
2. Make sure the table is clear.
3. *Activate Configuration* and switch to Run Mode.
4. Log in to the PLC and press *Start*.
5. Enable the track: *MOTION > Groups > Loop > Motion UI > Enable Dialog*.
6. In *TwinCAT > MC3 > XPlanar Environment View*: *Join Track* (with *Use Orientation*), *Jog On Track*, then *Leave Track*.

## Notes

- A mover does not join a disabled track and no error is shown.
- Use a gap of 240 mm when jogging.
