
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def update(i):
    data = pd.read_csv("data_log.csv")
    plt.cla()
    plt.plot(data["Timestamp"], data["Temperature"], label="Temperature")
    plt.plot(data["Timestamp"], data["Humidity"], label="Humidity")
    plt.legend(loc="upper left")
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), update, interval=2000)
plt.show()
