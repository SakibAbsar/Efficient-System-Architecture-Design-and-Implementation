import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
df = pd.read_csv('sensor_data.csv')
line, = ax.plot(df['timestamp'], df['sensor_value'])

def update(frame):
    df = pd.read_csv('sensor_data.csv')
    line.set_data(df['timestamp'], df['sensor_value'])
    ax.relim()
    ax.autoscale_view()
    return line,

ani = FuncAnimation(fig, update, interval=1000)
plt.show()
