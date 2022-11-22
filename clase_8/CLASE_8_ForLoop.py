NAMES = [
    "Jose",
    "Maria",
    "Juan",
    "Miguel",
    "jonathan",
    "Julio"
]
PETS = [
    "Cat",
    "Dog",
    "Parrot"
]
NUMBERS = (1, 2, 3)

##def list_names (names: list):
##    for name in names:
##        print(name)


def find_names (names):
    for name in names:
        if name == "Jose":
            print(f"{name} sí esta!!")
        else:
            print("No es Jose")
find_names(NAMES)

def check_if_name_in_list(name, names):
     if name in names:
         print(f"{name} Sí esta")
     else:
         print(f"{name} No esta")
check_if_name_in_list("Jose", NAMES)
print("x" * 20)
find_names(NAMES)
