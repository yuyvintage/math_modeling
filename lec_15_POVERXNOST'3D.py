import numpy as np 
import matplotlib.pyplot as plt 

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, np.pi, 100)
R = 5

x = R * np.outer(np.cos(phi), np.sin(theta))
y = R * np.outer(np.sin(phi), np.sin(theta))
z = R * np.outer(np.ones(np.size(phi)), np.cos(theta))

ax.plot_surface(x, y, z)

plt.savefig("surface.png")