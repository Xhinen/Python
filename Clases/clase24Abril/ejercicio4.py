# Ejercicio 4 - Factorial¶
# Escribe un programa que pida al usuario un número entero positivo y calcule su factorial. El programa debe imprimir el resultado. 
# El factorial de un número n se define como el producto de todos los números enteros desde 1 hasta n.

numero = int(input("Introduce un número entero positivo: "))
factorial = 0
for i in range(1, numero+1):
    factorial *= i #factorial = factorial * i

print(f"El factorial de {numero} es {factorial}")