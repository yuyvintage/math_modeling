import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation 

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label'Ball')

def circle_move(R, vx0, time):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = x0 + R * np.cos(alpha)
    y = y0 + R * np.sin(alpha)
    return x,y

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylin(-edge, edge)

def animate(i):
    ball.set_data(circle_move(r=0.5, vx0=0.01, vy0 = 0.01, time=i))

ani = animation.