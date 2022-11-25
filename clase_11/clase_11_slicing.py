# slicing
ORDER = []
def pizza_order():
    order = input("Hola bienvenido a aleXpitseria, que va a ordenar?: ")
    ORDER.append(order[::])
    order_trigger = False
    while not order_trigger:
        msg_1 = input("Quieres agregar algo mas a tu pedido?: ")
        if msg_1 == 'si':
            complemento = input("Que mas quieres añadir al pedido?: ")
            ORDER.append(complemento[::])
        else:
            print(f'{"*" * 20}\nFinalizando la orden\n{"*" * 20}')
            order_trigger = True
    print(f'Tu pedido es: {ORDER}')
pizza_order()