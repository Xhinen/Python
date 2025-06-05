# Ejercicio 4 - Verificar si un número es primo
# Escribe un programa que pida al usuario un número entero y verifique si es primo. 
# El programa debe definir una función que reciba el número, realice la verificación 
# y luego imprima si el número es primo o no.
import math


def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, math.sqrt(numero)+1):
        if numero % i == 0:
            return False
        return True

def cuantos_primos(numero):
    # Un número es primo si solo es divisible entre 1 y si mismo.
    resultado = 0

    for i in range(2, numero+1):
        if es_primo(i):
            resultado += 1

    return resultado
    
numero = int(input())
print(cuantos_primos(numero))