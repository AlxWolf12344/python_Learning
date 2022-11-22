"""
while = mientras (tal condicion sea o no sea)
"""


### def sum_to_50():
   ## total = 0
   ## while total <= 50:
    ## number = int(input("ingrese un numero: "))
    ## total = total + number
  ##   print(f"total is: {total}")

## sum_to_50()

"""def registro_cuenta():
    usuario1 = input("Create a username: ")
    password1 = input("Create a password: ")
    print("lets start!, please introduce your username and your password")
    usuario2 = input("Username: ")
    user_trigger = False
    password_trigger = False
    while not user_trigger:
        if usuario2 == usuario1:
            user_trigger = True
            print("Username is correct!, now the password")
            password2 = input("Password: ")
            while not password_trigger == False:
                if password2 == password1:
                    password_trigger = True
                    print("Great youre now loggin Please enjoy!")
                else:
                    password_trigger = False
                    print("Password is incorrect, please try again...")
        elif not user_trigger:
            print("Username is incorrect please try again...")
        return


registro_cuenta()"""

def registro_de_cuenta():
    print("vamos a crear tu cuenta!")
    usuario1 = input("Crea tu nombre de usuario: ")
    pasword1 = input("Crea tu contraseña: ")
    usuario_trigger = False
    msg2 = 'la contraseña es incorrecta'
    print("vamos a iniciar tu sesión!")
    sesion1 = input("Ingresa tu usuario: ")
    if sesion1 == usuario1:
        usuario_trigger = True
    while not usuario_trigger:
        msg1 = input("El usuario es incorrecto quiere intentarlo nuevamente? 'y' para Si y 'n' para No: ")
        if msg1 == 'y':
            sesion1 = input("Ingresa tu nombre de usuario: ")
            sesion1 == usuario1
            usuario_trigger = True
        elif msg1 != 'y''n':
            print(f"{msg1.upper()} No es valido, intente denuevo")
            usuario_trigger = False
        else:
            msg1 == 'n'
            print("T E R M I N A N D O  E L  P R O G R A M A")
            print("x" * 40)
            usuario_trigger = True
            return {usuario1}
    password2 = input("Ingresa tu contraseña: ")
    password_trigger = False
    while not password_trigger:
        print(msg2)
        if password2 == pasword1:
            password_trigger = True
            print("has iniciado sesion correctamente, disfruta de tu estancia!...")
        else:
            print("Tu contraseña es incorrecta, porfavor intenta nuevamente")
        return password2


registro_de_cuenta()