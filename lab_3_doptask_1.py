import numpy as np


A = np.ones((4, 3))


for i in range(0, 4, 1):
    for j in range(0, 3, 1):
        A[i, j] = int(input('напишите число:'))

print(A)

B = np.ones((4, 3))
 
for i in range(0, 4, 1):
    for j in range(0, 3, 1):
        B[i, j] = int(input('напишите число:'))

print(B)

C = np.ones((4, 3))

for i in range(0, 4, 1):
    for j in range(0, 3, 1):
        if A[i, j] > B[i,j]:
            C[i,j] = A[i, j]
    elif:
         C[i,j] = B[i, j]
      
print(C)







      
 
