#Pedir el nombre del vendedor y cuanto ha vendido este mes, y entregarle el total con 2 decimales
def comisionador():
    vendedor = input("Cual es tu nombre?: ")
    total_ventas = int(input("cuanto es el total de tus ventas este mes?: "))
    print(f'Hola {vendedor} tu comisión es de ${round(total_ventas*13/100,2)}')
comisionador()

