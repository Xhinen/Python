# Ejercicio 3
# Escribe un programa que pida al usuario un número entero y determine si es divisible por 3 y 5.
# El programa debe imprimir un mensaje indicando el resultado.

numero3 = int(input("Introduce un número entero: "))
if numero3 % 3 == 0 and numero3 % 5 == 0:
    print(f"El número {numero3} es divisible de 3 y 5.")
else:
    print(f"El número {numero3} no es divisible de 3 y 5.")