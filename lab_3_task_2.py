import numpy as np

h = 100
a = np.pi / 3
g = 9,8
B = 30

V = ((g*h * (np.tan(B**2))) / ((2 * ((np.cos(a))**2)) - (1 - np.tan(B) * np.tan(a))))**0.5
print(V)

from lab_3_task_1 import h as H
from lab_3_task_1 import k as k 
from lab_3_task_1 import e as e
E = 300
T = 200
N = (2 / np.pi) * (H / (k * T)**(3 / 2)) * (e**(-E / k * T)) (E**(T / 2))
print(N)