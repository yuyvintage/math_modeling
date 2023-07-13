import numpy as np

N = int(input('напишите количество столбиков:'))
M = int(input('напишите длину строк:'))

A = np.ones((N, M))

for i in range(0, 1-M, 1):
    for j in range(0, 1-N, 1):
if A[i, j] < 0:
    A[i, j] = 0

print(A)