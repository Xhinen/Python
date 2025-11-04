"""
Ejercicio 1 - Gestor de Archivos con Python usando el módulo os
Desarrollar un programa en Python que permita gestionar archivos y directorios mediante un menú interactivo, utilizando las funciones principales del módulo os.

El programa debe incluir las siguientes funcionalidades:

1. Menú principal con las siguientes opciones:

Listar archivos del directorio actual
Verificar si un archivo existe
Crear un nuevo archivo
Crear un nuevo directorio
Salir

2. Implementación de cada opción:

Listar archivos: Mostrar todos los archivos y carpetas en el directorio actual.
Verificar existencia: Pedir al usuario un nombre de archivo y comprobar si existe.
Crear archivo: Solicitar un nombre y generar un archivo vacío.
Crear directorio: Pedir un nombre y crear una carpeta nueva.

3. Manejo de errores:

Evitar que el programa falle si el usuario ingresa datos incorrectos.
Mostrar mensajes claros (ej: "❌ El archivo no existe", "✅ Operación exitosa").

4. Bucle infinito:

El menú debe mostrarse continuamente hasta que el usuario elija "Salir".
"""

""" 
Función - os.listdr()
Descripción - Lista archivos en un directorio
Ejemplo de uso - os.listdir('.')

Función - os.path.exists()
Descripción - Verifica si un archivo/directorio existe
Ejemplo de uso - os.path.exists("archivo.txt")

Función - os.mkdir()
Descripción - Crea un nuevo directorio
Ejemplo de uso - os.mkdir("nueva_carpeta")

Función - open() (modo 'w')
Descripción - Crea/sobrescribe un archivo (no es de os, pero útil)
Ejemplo de uso - open("archivo.txt", "w").close()

"""

import os

def listar_archivo():
    return os.listdir(".")

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
            archivos = listar_archivo()
            for archivo in archivos:
                print(archivo)
        elif opcion == 2:
            archivo = input("Qué archivo quieres comprobar?\n")
            if existe_archivo(archivo):
                print("✅ Archivo existe, el pueblo resiste\n")
            else:
                print("❌ El archivo no existe")
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