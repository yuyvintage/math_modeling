def parametrs(**kwargs):
    print(kwargs)

parametrs(first = 1, secont = 'two', something=False)

def discriminant(a, b, c):
    return b * b - 4 * a * c

polynom = {'a': 1, 'b': 0, 'c': 2}

print(f'{discriminant(**polynom) = }')