import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.random.normal(170, 10, 20)

fig, ax = plt.subplots()
ax.set_xlim(140, 200)
ax.set_ylim(0, 20)  
bars = ax.hist([], bins=20, color='skyblue', edgecolor='black')[2]

def init():
    for bar in bars:
        bar.set_height(0)
    return bars

def update(frame):
    data = x[:frame]
    ax.clear()
    ax.hist(data, bins=20, color='skyblue', edgecolor='black')
    ax.set_xlim(140, 200)
    ax.set_ylim(0, 20)  
    ax.set_xlabel('Height')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Heights')
    ax.grid(True)
    return bars

ani = FuncAnimation(fig, update, frames=len(x), init_func=init, blit=False, interval=1)

plt.show()
ani.save('height.gif', writer='pillow')



