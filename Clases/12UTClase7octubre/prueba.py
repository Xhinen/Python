notas_alumnos = {
    "Kenneth": [6.5, 8, 3],
    "Jorge": [0, 10, 5],
    "Jose el chater": [7, 6, 10],
    "Heber": [10, 10, 10],
    "Victor": [7, 8, 9],
    "Ander": [8, 8, 8]
}

def main():
    print("Escoge una opción:")
    print("1- Consultar media alumno")
    print("2- Añadir nota alumno")
    print("3- Añadir alumno")
    print("4- Eliminar nota alumno")
    print("5- Eliminar alumno")
    print("6- Salir")

def main():
    print("Bienvenidos al gestor de notas!")
    imprimir_menu()

    opcion = input()

    while opcion != 6:
        match opcion:
            case 1:
                alumno = input("Que media quieres consultar?\n")
                consultar_media(alumno)