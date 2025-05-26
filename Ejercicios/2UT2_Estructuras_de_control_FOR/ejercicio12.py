# Ejercicio 12
# Escribe un programa que pida al usuario dos números enteros e imprima la secuencia de números entre ellos (incluidos) en orden ascendente. 
# Si el primer número es mayor que el segundo, imprime la secuencia en orden descendente. 
# Debes imprimir la secuencia de números en una sola línea, separados por espacios.

numero = int(input("Introduce un número: "))
numero2 = int(input("Introduce otro número: "))

if numero > numero2:
    for i in range(numero, numero2-1, -1):
        print(i)
else:
    for i in range(numero, numero2+1):
        print(i)