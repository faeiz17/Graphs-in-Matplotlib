import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PIL import Image  

x = np.arange(20)
birth_years = np.random.randint(1950, 2005, size=20)

fig, ax = plt.subplots()
ax.set_xlim(0, 20)
ax.set_ylim(1950, 2005)
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(frame):
    y_data = birth_years[:frame+1]  
    x_data = x[:frame+1]  
    line.set_data(x_data, y_data)
    return line,

ani = FuncAnimation(fig, animate, frames=len(x), init_func=init, blit=True, interval=20)

plt.xlabel('x')
plt.ylabel('Birth Year')
plt.title('Birth Year Data')
plt.grid(True)
plt.show()

ani.save('birth_year_animation.gif', writer='pillow')
