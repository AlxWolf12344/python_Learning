
def pedazos_de_pizza():
    pedados_iniciales = int(input("Con cuantos pedazos de pizza iniciaste?"))
    pedazos_comidos = int(input("Cuantos pedazos de pizza se han comido?"))
    pedazos_restantes = pedados_iniciales - pedazos_comidos
    if pedazos_comidos == 0:
        print("no me vas a buggear ni lo intentes")
    elif pedazos_comidos > pedados_iniciales:
        print("eso va en contra del server te vamos a banear")
    else:
        if pedazos_restantes <= 2:
            print("sera duelo a muerte por la ultima pieza apurate a comerte la orilla! quedan: ", pedazos_restantes)
        elif pedazos_restantes >= 4:
            print("bueno aun queda algo de pizza quedan:", pedazos_restantes,"pedazos restantes")
        elif pedazos_restantes == pedados_iniciales:
            print("aun nadie ha tocado la pizza que esperas para iniciar quedan:", pedazos_restantes)
        elif pedazos_restantes == 0:
            print("valio madre la pizza :c quedan: ", pedazos_restantes)
    if pedazos_restantes == 0:
        print("pedimos otra? :)?")
pedazos_de_pizza()