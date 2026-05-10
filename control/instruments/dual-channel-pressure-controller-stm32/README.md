# Dual-channel pressure controller (STM32 + electronic regulator)

**Status: stub.** A working open-source pressure controller analog to the
Elveflow OB1 (commercial, ~$5k) and Fluigent MFCS (commercial, ~$10k).
Targets the architectural pattern of pneumatic-pressure-driven microfluidics
with two independent channels and PID feedback.

## Specifications (target)

- 2 independent pressure channels, ±2000 mbar range each
- 1 mbar resolution
- PID feedback control with 100 Hz update rate
- USB-CDC serial protocol for host control
- Closed-loop with onboard pressure sensors
- Optional gas-input pressure regulator (target 1 bar input)

## Required deliverables

- `hardware/` — KiCad PCB project (CERN-OHL-P or CC0)
- `firmware/` — Rust firmware (MIT or CC0)
- `docs/BOM.csv` — bill of materials
- `docs/CALIBRATION.md` — pressure-sensor calibration procedure
- Performance characterization (step response, overshoot, drift) co-deposited

## License (when populated)

Mixed:
- Hardware: CERN-OHL-P
- Firmware: MIT
- Docs: CC0-1.0
