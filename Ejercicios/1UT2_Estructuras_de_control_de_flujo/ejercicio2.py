# Ejercicio 2
# Escribe un programa que pida al usuario un número entero y determine si es positivo, negativo o cero.
# El programa debe imprimir un mensaje indicando el resultado.

numero2 = int(input("Introduce un número entero: "))
if numero2 > 0:
    print("El número {numero2} es positivo.")
elif numero2 < 0:
    print("El número {numero2} es negativo.")
else:
    print("El número es 0.")