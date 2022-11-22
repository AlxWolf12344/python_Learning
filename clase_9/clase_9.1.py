
def display_name():
    name = input("Hola, ingresa tu nombre porfavor: ")
    times = int(input("Cuantas veces quieres que se repita el nombre?: "))
    times = range(0, times, 1)
    for i in times:
        print(name.title())


display_name()
