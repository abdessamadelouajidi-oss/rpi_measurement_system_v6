# Raspberry Pi Vibration Measurement System v5

A console-only vibration measurement system for Raspberry Pi using the same interaction model as v3 (BEGIN/POWER buttons + state machine + LEDs), with optional ToF and Hall sensors.

## Features

- BEGIN button toggles IDLE/MEASURING states
- POWER button hold stops measurement and saves CSV
- IDLE/MEASURING status LEDs + USB copy status LED
- Accelerometer (I2C/MMA8452) vibration readings
- Optional VL53L0X ToF distance readings
- Optional Hall sensor spin counter (one-count-per-interaction, logged per sample)
- CSV export to `measurements.csv`
- Optional USB auto-copy when a drive is inserted

## Project Structure

```
rpi_measurement_system_v5/
|- main.py              # Main application entry point
|- sensors.py           # Accelerometer, ToF, Hall sensor classes
|- config.py            # Configuration settings (pins, intervals)
|- state_machine.py     # State transitions (IDLE/MEASURING)
|- buttons.py           # BEGIN/POWER button handlers
|- leds.py              # IDLE/MEASURING/USB status LEDs
|- requirements.txt     # Python dependencies
`- README.md            # This file
```

## Hardware Configuration

### GPIO Controls
- BEGIN Button: GPIO 17
- POWER Button: GPIO 27
- IDLE LED: GPIO 5
- MEASURING LED: GPIO 6
- USB COPY LED: GPIO 13

### I2C Sensors
- Accelerometer (MMA8452): I2C address 0x1C
- ToF (VL53L0X): I2C address 0x29 (optional)

### Hall Sensor (Spin Counter)
- GPIO pin configured in `config.py` (default GPIO 22)
- Use pull-up if your Hall sensor is open-collector
- One magnet per revolution for 1 pulse per spin
- Re-arm behavior is configurable via `HALL_STABLE_SAMPLES`

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Update settings in `config.py` as needed (pins, intervals, optional sensors).

3. Run directly or via your service:
   ```bash
   python main.py
   ```

## Usage

- Program starts in IDLE with IDLE LED on.
- Press BEGIN to start/stop measuring.
- Hold POWER for 2+ seconds to stop measurement and save.
- Data is saved to `measurements.csv` on shutdown and during USB copy events.

## Output Example

```
============================================================
Raspberry Pi Vibration Measurement System
============================================================

[ACCELEROMETER] Initialized on bus 1, address 0x1C
[TOF] Initialized VL53L0X on I2C (0x29)
[HALL_SENSOR] Polling GPIO 22 at ~800 Hz (one-count-per-interaction, stable_samples=5)
[BEGIN_BUTTON] Button initialized on GPIO 17
[POWER_BUTTON] Button initialized on GPIO 27
[IDLE_LED] LED initialized on GPIO 5
[MEASURING_LED] LED initialized on GPIO 6

System ready. Press BEGIN button to start measuring.
Hold POWER button for 2+ seconds to stop and save.
------------------------------------------------------------

[2026-02-18 14:32:45] Vibration - X=+0.12m/s^2 Y=-0.08m/s^2 Z=+9.81m/s^2
[2026-02-18 14:32:46] Vibration - X=+0.11m/s^2 Y=-0.09m/s^2 Z=+9.80m/s^2
```

## Notes

- All pins and options are configurable in `config.py`
- The Hall sensor count is logged per row as `spin_count`
- If you see double counts, increase `HALL_STABLE_SAMPLES` and check wiring quality
- Press Ctrl+C to safely stop when running manually

## Dependencies

- `RPi.GPIO` - Raspberry Pi GPIO control
- `smbus-cffi` - I2C communication for sensors
- `adafruit-blinka` and `adafruit-circuitpython-vl53l0x` for ToF sensor support
