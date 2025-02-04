# Advanced System Architecture

## Project Overview
This project integrates circuit modeling, digital component libraries, and a real-time monitoring and control system with data logging and visualization.

### File Structure
- `main_code.ino`: Arduino code for sensor and actuator control.
- `sensor_driver.cpp` / `sensor_driver.h`: Sensor driver for data acquisition.
- `actuator_control.cpp` / `actuator_control.h`: Actuator control logic.
- `data_logger.py`: Python script for logging sensor data to CSV.
- `monitor_dashboard.py`: Dashboard for real-time data visualization.
- `test_sensor_reading.py`: Script to automate testing of sensor data.
- `sn74_library.v`: Verilog library of SN74 series components.

### Dependencies
Install dependencies with:
```bash
pip install -r requirements.txt
```

### Running the Project
1. Upload `main_code.ino` to your Arduino.
2. Run `data_logger.py` to log sensor data.
3. Run `monitor_dashboard.py` to visualize real-time data.
4. Use `test_sensor_reading.py` to validate sensor functionality.
