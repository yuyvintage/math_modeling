names = ['Jhon', 'David', 'Maria', 'Richard']
ages = [16, 25, 19, 41]

def chacker(user):
    name, age = user
    return age > 21

users = list(zip(names, ages))
canDrinkAlcohol = list(filter(chacker, users))
print(canDrinkAlcohol)