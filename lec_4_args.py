'''
def my_func(a, b):
    x = 3 * a - b
    return x

tmp = my_func()
'''

def my_func(a=1,b=0):
    x = 3 * a - b
    return x


print(my_func())
print(my_func(3, 4))
print(my_func(3))
print(my_func(b=3))

def my_func(a, b=0):
    x = 3 * a - b
    return x

def my_func(*args):
    x = 3 * args[0] - args[1]
    return x

print(my_func(3, 4))
print(my_func(3, 4, 8))

def my_func(**kwrgs):
    x = 3 * kwrgs['(obj_1=3'] - kwrgs['obj_2=2']
    return x
