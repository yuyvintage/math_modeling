import numpy as np

a = np.arange(0, 10, 1)

def math_func(a):
    for i in range(0, 10, 1):
        x = 0
        x += i
        b = x/10
    return x

print(math_func(a))
