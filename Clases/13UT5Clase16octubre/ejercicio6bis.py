import os

def search_lines(path, word):
    if len(word) == 0:
        raise ValueError("La palabra no puede ser vacía")
    
    if not os.path.exists(path):
        raise FileNotFoundError(f"El archivo {path} no existe")
    
    with open(path, "r") as file:
        for num, line in enumerate(file, start=1):
            if word in line:
                print(f"Línea{num}: {line}")


path = input("Que archivo quieres imprimir\n")
word = input("Que palabra quieres buscar\n")

try:
    search_lines(path, word)
except Exception as e:
    print(e)