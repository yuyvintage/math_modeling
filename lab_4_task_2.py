import numpy as np

a = np.arange(0, 5 ,1)

def new_func(a):
    for i in range(0, 5, 1):
        x = 1
        x *= i
        return x


print(new_func(a))