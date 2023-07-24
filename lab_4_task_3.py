import numpy as np
 
m = int(input('укажите массу тела в кг:'))
h = int(input('укажите высоту на которую подбросили тело в м:'))
V = int(input('укажите начальную скорость тела в м/с:'))
g = 9,8


def energy():
    k = (m * (V**2))/ 2
    P = m * g * h
    x = P - k
    return x
    
print(energy())


