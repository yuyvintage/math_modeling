a = input('напишите число:')

for i in range(1, len(a)+1, 1):
    print(a[-i], end='')
