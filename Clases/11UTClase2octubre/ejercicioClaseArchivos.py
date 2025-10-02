""" Vamos a realizar un programa que lea el archivo sistema_log_extenso.txt e imprima por pantalla todos los mensajes del tipo ERROR """


log = open("Clases/11UTClase2octubre/sistema_log_extenso.txt", "r") #La ruta raiz que coge visualstudio es la carpeta del proyecto en este caso PYTHON

log_data = log.readlines()

for line in log_data:
    if "ERROR" in line:
        print(line, end="")