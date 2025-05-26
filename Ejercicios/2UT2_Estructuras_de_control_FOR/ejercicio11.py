# Ejercicio 11
# Escribe un programa que pida al usuario dos números enteros e imprima la secuencia de números entre ellos (incluidos) en orden ascendente. 
# El primer número siempre será menor que el segundo.

numero = int(input("Introduce un número: "))
numero2 = int(input("Introduce otro número: "))

for i in range (numero, numero2+1):
    print(i, end=" ") #añadimos end=" " para imprimir los números en la misma línea con un espacio.