
def display_name():
    nombre = input("Cual es tu nombre?: ")
    veces = range(0, int(input("Cuantas veces quieres que se muestre tu nombre?: ")), 1)
    for i in veces:
        print(f'{nombre}')
    print(f'{"*" * 5}\n Fin \n{"*" * 5}')


display_name()
