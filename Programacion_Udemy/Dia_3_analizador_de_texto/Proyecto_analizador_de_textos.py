#Albion Online es un mmorpg no lineal, en el que escribes tu propia historia sin limitarte a seguir un camino prefijado. Explora un amplio mundo abierto con 5 biomas únicos, todo cuánto hagas tendrá su repercusión en el mundo, con la economía orientada al jugador de Albion, los jugadores crean prácticamente todo el equipo a partir de los recursos que consiguen, el equipo que llevas define quién eres, cambia de arma y armadura para pasar de caballero a mago, o juega como una mezcla de ambas clases. Aventúrate en el mundo abierto frente a los habitantes y las criaturas de Albion, inicia expediciones o adéntrate en mazmorras en las que encontrarás enemigos aún más difíciles, enfréntate a otros jugadores en encuentros en el mundo abierto, lucha por los territorios o por ciudades enteras en batallas tácticas, relájate en tu isla privada, donde podrás construir un hogar, cultivar cosechas y criar animales, únete a un gremio, todo es mejor cuando se trabaja en grupo. Adéntrate ya en el mundo de Albion y escribe tu propia historia?


def text_analisys():
    #cuantas veces se repite una letra
    texto = input("cual es el texto que quieres analizar?: ")
    texto = texto.lower()
    letter_search = input("Cual es la letra que quieres ver cuantas veces se repite?: ")
    print(f' "{letter_search} "se repite un total de: {texto.count(letter_search)} veces')
    #primera y ultima letra
    print(f'La primera letra del escrito es: "{texto[0].upper()}" y la ultima: "{texto[-1].upper()}"')
    palabras = texto.split()
    print(f'El texto tiene: {len(palabras)} palabras')
    #palabras en modo inverso
    palabras.reverse()
    texto_invertido = " ".join(palabras)
    print(f'El texto invertido es: {texto_invertido}')
    #aparece esta palabra?
    search = input("cual es la palabra que quieres buscar en el texto?: ")
    print(f' "{search} " aparece un total de: {texto.count(search)} veces en el texto')
text_analisys()