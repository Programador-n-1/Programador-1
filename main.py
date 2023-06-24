from Normativa import *
from Usuario import Usuario


def admin_menu():
    print("¡Bienvenido administrador!")
    print("1. Crear Normativa")
    print("2. Actualizar Normativa")
    print("3. Eliminar Normativa")
    print("4. Leer Normativas")
    print("0. Salir")

def random_user_menu():
    print("¡Bienvenido usuario!")
    print("1. Leer Normativas")
    print("0. Salir")

def login():
    print("¡Hola! Ingrese una opción:")
    print("1. Ingresar como admin")
    print("2. Ingresar como usuario")
    opcion = input("Ingrese su opción: ")
    if opcion == "1" or opcion == "2":
        userName(opcion)
    else:
        print("Opción inválida. Por favor, seleccione 1 o 2.")
        login()

def userName(opcion): 
    if opcion == "1":
        usuario = input("Ingrese su nombre de usuario: ")
        user = Usuario(usuario, "")
        if user.check_user_exists(usuario) and user.check_user_permission(usuario) == "todos":
            usuario = Usuario(usuario, "")
            print("Has iniciado sesión como admin")
            menu("todos")
        else: 
            print("Usuario inexistente. Por favor, ingrese un usuario válido.")
            userName(opcion)
    elif opcion == "2":
        usuario = input("Ingrese su nombre de usuario: ")
        user = Usuario(usuario, "")
        if user.check_user_exists(usuario) and user.check_user_permission(usuario) == "lectura":
            usuario = Usuario(usuario, "")
            print("Has iniciado sesión como usuario")
            menu("lectura")
        else:
            print("Usuario inexistente. Por favor, ingrese un usuario válido.")
            userName(opcion)


def run_program():
   login()

def menu(permisos):
    if permisos == "todos":
        while True:
            admin_menu()
            option = input("Opción: ")

            if option == "0":
                break
            elif option == "1":
                create_normativa()
            elif option == "2":
                update_normativa()
            elif option == "3":
                delete_normativa()
            elif option == "4":
                read_normativas()
            else:
                print("Opción inválida. Intente nuevamente.")
    else:
        while True:
            random_user_menu()
            option = input("Opción: ")

            if option == "0":
                break
            elif option == "1":
                read_normativas()
            else:
                print("Opción inválida. Intente nuevamente.")

    print("¡Hasta luego!")


run_program()