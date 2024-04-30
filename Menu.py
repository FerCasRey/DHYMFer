def show_menu():
    print("\nBienvenido al lanzador de HYMFer.")
    print("Seleccione una opcion:".center(30, "-"))
    print("1. Ejecutar Pong")
    print("2. Ejecutar Space Invaders")
    print("3. Créditos y más")
    print("4. Cerrar")

def option1():
    print("Ejecutando Pong")
    # Add your code for Option 1 here

def option2():
    print("Ejecutando Space Invaders")
    # Add your code for Option 2 here

def option3():
    print("Créditos".center(30,"~"))
    print("".center(30,"-"))
    print("Pong - Mateo".center(30,"-"))
    print("Space Invaders - Yoel".center(30,"-"))
    print("Arte - Hugo".center(30, "-"))
    print("Menú - Fernando".center(30,"-"))
    print("Creado para el proyecto".center(30,"+"))
    print("final de TICs 23-24".center(30, "+"))
    print("¡Gracias por jugar!".center(30, "#"))
    # Add your code for Option 3 here

def main():
    while True:
        show_menu()
        choice = input("Su selección \n")

        if choice == "1":
            option1()
        elif choice == "2":
            option2()
        elif choice == "3":
            option3()
        elif choice == "4":
            print("Cerrando. Gracias por jugar.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
