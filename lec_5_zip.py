ages = [16, 25, 19, 41]
names = ['Jhon', 'David', 'Maria', 'Richard']
isTeenager = [True, False, True, False]

users = list(zip(names, ages, isTeenager))
print(users)

print('User ages',dict(zip(names, ages)) )



