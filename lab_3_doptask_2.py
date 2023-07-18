import numpy as np

a = np.arange(0, 4, 1)

for i in range(0, 4, 1):
    a[i] = int(input('напишите элементы массива'))

print(a)

b = int(input('напишите число'))

c = a[0:b:-1]

print(c) 