import numpy as np

a = np.arange(1, 5 ,1)

def new_func(a):
    for i in range(1, 3, 1):
        x = 1
        x *= i
    return x


print(new_func(a))