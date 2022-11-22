
def inicio_de_sesion():
    print("Bienvenido, Vamos a crear tu usuario y tu contraseña")
    usuario = input("Crea tu nombre de usuario: ")
    password = input("Crea tu contraseña: ")
    print("Perfecto, vamos a iniciar sesion")
    registro = input("Ingresa tu usuario: ")
    password2 =input("Ingresa tu contraseña: ")
    if usuario != registro or password != password2:
        while usuario != registro or password != password2:
            print("La contraseña o el usuario son incorrectas, porfavor intenta nuevamente...")
            registro = input("Ingresa tu usuario: ")
            password2 = input("Ingresa tu contraseña: ")
    print("Sesion iniciada correctamente disfruta de tu estancia!")

inicio_de_sesion()