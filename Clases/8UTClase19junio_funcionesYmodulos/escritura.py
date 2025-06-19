"""
Quiero crear una función imprimir que:
1- reciba el mensaje a imprimir
2- opcionalmente reciba un color para que imprima el mensaje de ese color
"""

def imprimir(mensaje, color=None):
    if color != None:
        mensaje = color + mensaje + Style.RESET_ALL
    
    print(mensaje)


def imprimir_con_marco(mensaje, color=None):
    """ 
    --------
    | Hola |
    -------- 
    """
    mensaje = f"| {mensaje} |"
    barra = "-"*len(mensaje)
    imprimir(barra + "\n" + mensaje+ "\n" + barra + Style.RESET_ALL)
    pass