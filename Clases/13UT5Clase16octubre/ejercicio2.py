""" Ejercicio 2 - Leer un archivo y contar líneas y palabras
Escribe un programa que abra un archivo de texto, lea su contenido y cuente el número de líneas y palabras que contiene.
El programa debe definir una función que realice esta tarea y luego imprima el resultado. """

import os

def count_lines_and_words(path):
    if not os.path.exists(path):
        raise FileNotFoundError("El archivo no existe")

    with open(path, 'r') as file:
        lines = file.readlines()
        if len(lines) == 0:
            raise ValueError("El archivo esta vacío")

        words = 0
        for line in lines:
            words += len(line.split())
        return len(lines), words

try:
    lines, words = count_lines_and_words("ejemplo.txt")
    print(f"El número de lineas del archivo ejemplo.txt es {lines} y el de palabras es {words}")
except Exception as e:
    print(e)