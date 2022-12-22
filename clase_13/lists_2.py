
COUNTRIES = ("Canada", "Mexico", "Peru", "China", "Ecuador")


def show_countries():
    """exercise: 069
    crea un tuple que contenga los nombres de cinco paises y muestra
    todo el tuple, pida al usuario que escriba uno de los paises que se le mostraron y que
    luego le muestre el número de indice index de ese item en el tuple"""

    print(f'{", ".join(COUNTRIES) }')
    user_select = input("Escribe el pais del que quieres saber el Indice: ").title()
    if user_select not in COUNTRIES:
        print(f'El pais: "{user_select}", No esta en la lista')
    else:
        print(f'El pais: " {user_select} " tiene el indice: " {COUNTRIES.index(user_select)} " Si esta en la lista')
        return user_select

# show_countries()


def show_country():
    """
    Exercise: 070
    aguregue al programa 069 que le pida al usuario que escriba un numero y muestre el pais en esa posicion.
    """
    print(f'{", ".join(COUNTRIES)}')
    user_index = int(input("Seleccione un numero de indice del 1 al 4 para mostrar el pais en ese indice: "))
    if user_index > 4:
        print("El numero esta fuera de rango")
    else:
        print(f'{COUNTRIES[user_index]}')
        return user_index

# show_country()


SPORTS = ['Soccer', 'Baseball']
def get_new_sport():
    """
    Excercise: 071
    Cree una lista con dos deportes. Pida al usuario cual es su deporte favorito y este agreguelo al final de la lista.
    ordene la lista y muestrela.
    """
    print(f'{", ".join(SPORTS)}')
    new_sport = input("Cual es tu deporte favorito?: ").title()
    SPORTS.append(new_sport)
    SPORTS.sort()
    print(f'{", ".join(SPORTS)}')


# get_new_sport()

ASIGNATURE = ["Math", "Cience", "Spanish II", "Philosofy", "History", "Sports"]
def remove_unwanted_subjet():
    """
    Cree y muestre una lista de seis materias escolares. Pida al usuario cuál de estas materias no le gusta.
     Borre de la lista esa materia que haya escogido y muestre la lista de nuevo.
    """
    print(f'Lista de materias: {", ".join(ASIGNATURE)}')
    delete_class = input("Escribe el nombre de la materia que quieres eliminar: ").title()
    if delete_class not in ASIGNATURE:
        print(f'No tienes la clase de: " {delete_class} "')
    else:
        print(f'Clase: {delete_class} Fue eliminada de la lista.')
        delete_class = ASIGNATURE.index(delete_class)
        ASIGNATURE.pop(delete_class)
        print(ASIGNATURE)


remove_unwanted_subjet()

