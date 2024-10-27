
import unittest
from firmware import sensor_driver

class TestSensorReading(unittest.TestCase):
    def test_temperature_reading(self):
        temp = sensor_driver.SensorDriver.readTemperature()
        self.assertTrue(-40 <= temp <= 80)  # Typical range for temperature

if __name__ == "__main__":
    unittest.main()
