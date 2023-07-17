import numpy as np

N = int(input('напишите количество строк:'))
M = int(input('напишите длину строк:'))

a = np.zeros((N, M))

for i in range(0, N, 1):
    for j in range(0, M, 1):
        a[i, j] = int(input('напишите числа элементов массива:'))


print(a)

if b = 