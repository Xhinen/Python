# Ejercicio 3 - Cuenta atrás¶
# Escribe un programa que pida al usuario un número entero positivo y realice una cuenta atrás desde ese número hasta 0.
# El programa debe imprimir cada número en la cuenta atrás.

numero = int(input("Introduce un número entero positivo: "))

for i in range(numero, -1, -1):
    print(i)