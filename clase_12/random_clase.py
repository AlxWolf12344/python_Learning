import random


def generate_random():
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    print(f'Number 1 is: {number1}\nNumber2 is: {number2}')
    return number1 + number2


def generate_random_range():
    number = random.randrange(0, 100, 5)
    return number


colors = ["red", "blue", "black", "green", "lila"]


def generate_random_color():
    color = random.choice(colors)
    return color


# print(generate_random())
# print(generate_random_range())
# print(generate_random_color())


def russian_rulette():
    ammo = [0, 0, 0, 0, 0, 1]
    shot = random.choice(ammo)
    if shot == 1:
        print("Bang!")
    else:
        print("saved!")


NUMERO = [range(10)]


def adivina_el_numero():
    print("El numero es un numero del 1 al 10!")


russian_rulette()
