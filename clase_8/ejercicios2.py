
def imprimir_pedazos_que_quedan():
    """"
el codigo se usa para pregunta cuantos pedazos de pizza son con los que inicio y cuantos pedazas se ha comido.
encuantra cuantos pedazos se pizza le quedan y muestra la respuesta en un formato amigbale-al-usuario.
"""
    pizza_total = int(input("Con cuantos pedazos de pizza iniciaste?"))
    pedazos_comidos = int(input("Cuantos pedazos te has comido?"))
    pedazos_restantes = pizza_total - pedazos_comidos
    print("Solamente te quedan", pedazos_restantes)
imprimir_pedazos_que_quedan()

def proxima_edad():
    nombre_usuario = input("Porfavor ingresa tu nombre")
    edad_usuario = int(input("Ingresa tu edad"))
    edad_final  = edad_usuario + 1
    print(nombre_usuario, "Tu edad en el proximo cumpleaños sera :", edad_final)
proxima_edad()


def pedir_edad():
    edad_usuario = int(input("Que edad tienes carnal?"))
    if edad_usuario >= 18:
        print("Bienvenido, disfruta el party!")
    else:
        print("Desaparecete carnal, estas morrillo")


pedir_edad()