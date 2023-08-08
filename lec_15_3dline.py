import numpy as np 
import matplotlib.pyplot as plt 

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

t = np.arange(0.01, 4*np.pi, 0.01)
R = 1

x = R * np.cos(t)
y = R * t**0,5
z = R * np.log10(t)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title('3D test')

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-3, 3)

plt.savefig("jkhbk.png")