import numpy as np

Yo = int(input('напишите параметр начального положения:'))
Xo = int(input('напишите параметр начального положения:'))
Vo = int(input('напишите параметр скорости тела:'))

t = 

g = 9.8

X = Xo + (Vo * t)
Y = Yo + (Vo * t) - (g(t**2)/2)

print(X, Y)