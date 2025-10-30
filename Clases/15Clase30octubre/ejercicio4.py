import os

""" 
1º comprobar que existe el archivo
2º comprobar que sea un archivo
3º new_path = directorio/
5º comporobar que path y new_path no son iguales
6º mover el archivo a new_path
 """

def move_file(path, new_path):
    if not os.path.isfile(path):
        raise FileNotFoundError("No existe el archivo")
    if not os.path.isdir(new_path):
        path_without_file = os.path.abspath(new_path)
        if os.path.isdir(path_without_file):
            raise FileNotFoundError("No existe el directorio de destino")
    if path == new_path:

    pass

path = input("Introduce el archivo que quieres mover\n")
new_path = input("Introduce la ruta donde quieres moverlo\n")

try:
    print(move_file(path, new_path))
except Exception as e:
    print(e)