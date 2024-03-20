import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.arange(2000, 2020, 1)
petrol_prices = np.random.randint(60, 300, size=20)

fig, ax = plt.subplots()
ax.set_xlim(2000, 2019)
ax.set_ylim(60, 300)
sc = ax.scatter([], [])

def init():
    sc.set_offsets(np.zeros((0, 2)))  
    return sc,

def animate(frame):
    y_data = petrol_prices[:frame+1]
    x_data = x[:frame+1]
    sc.set_offsets(np.column_stack((x_data, y_data)))
    return sc,

ani = FuncAnimation(fig, animate, frames=len(petrol_prices), init_func=init, blit=True, interval=200)

plt.xlabel('Years')
plt.ylabel('Petrol Price')
plt.title('Petrol Price Over Time')
plt.grid(True)
plt.show()

ani.save('Petrol_Prices.gif', writer='pillow')

