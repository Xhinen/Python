""" Ejercicio 3 - Escribir en un archivo
Escribe un programa que pida al usuario una lista de nombres y los guarde en un archivo de texto, cada nombre en una línea diferente.
El programa debe definir una función que reciba la lista de nombres y el nombre del archivo, y luego escriba los nombres en el archivo. """

def escribir_nombres_en_archivo(nombres, archivo):
    if len(nombres) == 0:
        raise ValueError("No se ha proporcionado ningún nombre")
    
    with open(archivo, "a") as file:
        for name in nombres:
            file.write(f"{name}\n")


nombres = input("Introduce una lista de nombres separados por espacio\n").split()
escribir_nombres_en_archivo(nombres, "nombres.txt")