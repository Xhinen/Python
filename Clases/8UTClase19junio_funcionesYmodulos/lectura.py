""" 
Funciones para leer difrentes tipos de datos con control de errores

leer_entero()
-> hola
-> ValueError
"""

def leer_entero(mensaje):
    """ 
    Esto deberia hacer un input, intentar castearlo a int, y devolver valor entero
    Si al intentar castear la entrada no es un número, capturar excepción y elevarla
    """
    try:
        entero = int(input(mensaje))
    except:
        raise ValueError("")

    return entero

def leer_string(mensaje):
    return input(mensaje)

def leer_string_en_lista(mensaje):
    return input().split(" ")
    