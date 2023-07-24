counter = 0

def update(value):
    global counter
    result = counter + value

    print(f'{counter} + {value} = {results}')
    counter = result

update(1)
update(2)
update(3)

print(f'{counter = }')