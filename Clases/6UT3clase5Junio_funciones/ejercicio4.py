# Ejercicio 4 - Verificar si un número es primo
# Escribe un programa que pida al usuario un número entero y verifique si es primo. 
# El programa debe definir una función que reciba el número, realice la verificación 
# y luego imprima si el número es primo o no.
import math

def es_primo(numero):
    # Un número es primo si solo es divisible entre 1 y si mismo.
    for i in range(2, numero):
        if numero % i == 0:
            return False
        return True