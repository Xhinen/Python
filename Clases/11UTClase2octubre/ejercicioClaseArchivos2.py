""" Vamos a realizar un programa que lea el archivo sistema_log_extenso.txt e imprima por pantalla todos los mensajes del tipo ERROR """


log = open("Clases/11UTClase2octubre/sistema_log_extenso.txt", "r") #La ruta raiz que coge visualstudio es la carpeta del proyecto en este caso PYTHON
log_errores = open("errores.txt", "w")
log_data = log.readlines() # Lista con todas las líneas en String

for line in log_data:
    if "ERROR" in line:
        log_errores.write(line)