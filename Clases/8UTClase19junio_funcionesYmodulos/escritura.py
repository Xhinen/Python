"""
Quiero crear una función imprimir que:
1- reciba el mensaje a imprimir
2- opcionalmente reciba un color para que imprima el mensaje de ese color
"""

def imprimir(mensaje, color=None):
    if color != None:
        mensaje = color + mensaje + Style.RESET_ALL
    
    print(mensaje)