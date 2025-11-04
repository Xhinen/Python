# Importamos los módulos necesarios
import os
from datetime import datetime


# Creamos una función para mostrar el menú principal y la ruta de trabajo actual.

def mostrar_menu():

    print("\n=======================================")
    print("<------ GESTOR DE ARCHIVOS v1.0 ------>")
    print("=======================================")
    try:
        print(f"Ruta Actual: {os.getcwd()}")
    except Exception as e:
        print(f"No se pudo obtener la ruta actual: {e}")

    print("1. Listar contenido del directorio actual")
    print("2. Crear un nuevo directorio")
    print("3. Crear un archivo de texto")
    print("4. Escribir texto en un archivo existente (añadir)")
    print("5. Eliminar un archivo o directorio")
    print("6. Mostrar información del archivo/directorio")
    print("7. Salir")

# Añado las diferentes funciones para que el bucle principal del programa no me de error y así poder comprobar que funiona.

def listar_contenido():

    pass

def crear_directorio():

    pass

def crear_archivo():

    pass

def escribir_en_archivo():

    pass

def eliminar_elemento():

    pass

def mostrar_informacion():

    pass

def main():
    
    # Bucle while del programa principal, lo he cogido del ejercicio1.py del tema UT4 Funciones y Módulos (12 de junio)
    
    opcion = 0
    while opcion != 7:
        mostrar_menu()

        try:
            opcion_str = input("Escoge una opción (1-7): ")
            # Evitar error si el input está vacío
            if not opcion_str:
                continue
            opcion = int(opcion_str)
        except ValueError:
            # Requisito: Gestionar error de entrada no numérica
            print("❌ Error: Debes introducir un número válido.")
            continue

        if opcion == 1:
            listar_contenido()
        elif opcion == 2:
            crear_directorio()
        elif opcion == 3:
            crear_archivo()
        elif opcion == 4:
            escribir_en_archivo()
        elif opcion == 5:
            eliminar_elemento()
        elif opcion == 6:
            mostrar_informacion()
        elif opcion == 7:
            print("\nSaliendo del gestor de archivos. ¡Hasta luego Lucas!")
        else:
            # Requisito: Gestionar error de opción no válida
            print("❌ Opción no válida. Por favor, introduce un número del 1 al 7.")

if __name__ == '__main__':
    main()