import unittest
from sensor_driver import readSensorData

class TestSensorReading(unittest.TestCase):
    def test_sensor_reading_range(self):
        value = readSensorData()
        self.assertGreaterEqual(value, 0)
        self.assertLessEqual(value, 1023)

if __name__ == '__main__':
    unittest.main()
