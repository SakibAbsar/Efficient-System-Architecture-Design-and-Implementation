import serial
import pandas as pd
from datetime import datetime

ser = serial.Serial('/dev/ttyUSB0', 9600)
data = []

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        data.append({'timestamp': datetime.now(), 'sensor_value': line})

        if len(data) > 10:
            df = pd.DataFrame(data)
            df.to_csv('sensor_data.csv', mode='a', header=False, index=False)
            data = []
