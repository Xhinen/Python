# Ejercicio 2 - Coloreando la Terminal con colorama

import os


def listar_archivo(ruta):
    return os.listdir(ruta)

def existe_archivo(archivo):
    return os.path.exists(archivo)

def crear_archivo(nombre):
    return open(nombre, "x")

def crear_directorio(nombre):
    try:
        os.mkdir(nombre)
    except FileExistsError:
        raise FileExistsError
        
    return 

def color_segun_extension(archivo):
    # Los archivos sin extensión y los directorios
    if os.path.isdir(archivo):
        return "white"
    elif len(archivo.split(".")) == 1:
        return "green"
    elif archivo.split(".")[-1] == "txt":
        return "blue"
    elif archivo.split(".")[-1] in ["jpg", "png"]:
        return "yellow"
    return "white"

def main():
    opcion = -1
    while opcion != 5:
        print("### MENÚ ###")
        print("1. Listar archivos")
        print("2. Verificar existencia archivo")
        print("3. Crear archivos")
        print("4. Crear directorio")
        print("5. Salir")

        opcion = int(input("Escoge una opción:\n"))

        if opcion == 1:
            ruta = input("Introduce la ruta que quieres consultar:\n")
            try:
                archivos = listar_archivo(ruta)
                for archivo in archivos:
                    """ 
                     Funcion para coger el formato del archivo
                    """
                    print(f"Archivo")
            except FileNotFoundError:
                print(f"La ruta {ruta} no existe")
            except:
                print("Error al consultar la ruta, intenta de nuevo")
        elif opcion == 2:
            archivo = input("Qué archivo quieres comprobar?\n")
            if existe_archivo(archivo):
                print("Archivo existe, el pueblo resiste\n")
            else:
                print("El archivo no existe")
        elif opcion == 3:
            nombre = input("Introduce el nombre del archivo\n")
            if existe_archivo(nombre):
                print("Este archivo ya existe")
            else:
                archivo = crear_archivo(nombre)
                print(f"Archivo {archivo.name} creado con éxito")
        elif opcion == 4:
            nombre = input("Queé nombre quieres ponerle al directorio\n")
            try:
                crear_directorio(nombre)
                print(f"Directorio {nombre} creado con éxito")
            except FileExistsError:
                print(f"El directorio {nombre} ya existe")
        elif opcion > 5:
            print("Opción no válida")

if __name__ == '__main__':
    main()