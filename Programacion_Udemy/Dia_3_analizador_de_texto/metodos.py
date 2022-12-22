texto = "Este es el texto de textos por Alex"
resultado = texto.upper()
print(texto)

print(texto.replace('texto','frijol'))

frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
print(frase.upper())
lista_palabras = ["La","legibilidad","cuenta."]
espacio = " ".join(lista_palabras)
print(espacio)

frase = 'Si la implementación es difícil de explicar, puede que sea una mala idea.'
frase = frase.replace("difícil", "facil")
frase = frase.replace("mala","buena")
print(frase)
