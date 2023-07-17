import numpy as np

b = np.arange(4, -1, -1)

for i in range(0, 4, 1):
    b[i] = float(input(f'b[{i}]'))
print(b)

c = float(input('значение элемента 5'))
d = int(input('Позиция элемента 5'))

while d < 1 or d > 5:
    d = float(input('Позиция элемента 5 (0 < d < 6)'))

e = b
print(e)

for j in range(d, 5, 1):
    b[j] = e[j-1]
b[d-1] = c

print(b)

