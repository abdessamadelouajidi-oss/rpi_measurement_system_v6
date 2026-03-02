"""Configuration settings for the measurement system."""

# Button GPIO pins
BEGIN_BUTTON_PIN = 17      # GPIO 17 for BEGIN button
POWER_BUTTON_PIN = 27      # GPIO 27 for POWER button

# Sensor configuration
ACCELEROMETER_I2C_ADDRESS = 0x1C  # Default MMA8452 I2C address
TOF_ENABLED = True  # VL53L0X time-of-flight sensor
TOF_I2C_ADDRESS = 0x29  # Default VL53L0X address

# Hall sensor (spin counter)
HALL_ENABLED = True  # Set False to disable spin counting
HALL_SENSOR_PIN = 22  # GPIO pin for Hall sensor input
HALL_PULL_UP = True  # Use pull-up resistor if sensor is open-collector
HALL_POLL_HZ = 800  # Polling frequency for threaded Hall reader
HALL_STABLE_SAMPLES = 5  # Re-arm after N consecutive HIGH samples

# LED pins
IDLE_LED_PIN = 5        # GPIO 5 - lights up when in IDLE state
MEASURING_LED_PIN = 6   # GPIO 6 - blinks while measuring
MEASURING_LED_BLINK_INTERVAL = 0.5  # Blink every 0.5 seconds
USB_COPY_LED_PIN = 13   # GPIO 13 - indicates USB copy status
USB_COPY_LED_BLINK_INTERVAL = 0.2  # Blink while copying

# Measurement settings
READING_INTERVAL = 1.0  # Read vibration every 1.0 second while measuring

# CSV output
CSV_OUTPUT_PATH = "measurements.csv"  # Saved after shutdown

# USB copy settings
USB_COPY_ANY = True  # Copy to all mounted USB drives found under /media or /run/media
USB_CHECK_INTERVAL = 1.0  # Seconds between USB mount checks
