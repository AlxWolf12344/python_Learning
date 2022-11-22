"""Pedir al usuario que escriba su nombre y luego lo mostramos 3 veces
    Constrains: Dar formato al nombre para que inicie con mayuscula.
    Tips:
         1. Usar input() para obtener el dato del usuario
         2. Podemos buscar en los metodos de los strings y elegir el apropiado
         3. Podemos usar el metodo range() con la for loop
    """


def display_name():
    print("Hola, ingresa tu nombre porfavor: ")
    name = str(input())
    for i in [1, 2, 3]:
        print(name.title())


display_name()
