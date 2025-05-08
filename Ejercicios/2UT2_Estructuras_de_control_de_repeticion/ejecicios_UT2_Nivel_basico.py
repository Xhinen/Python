# Ejercicio 11
# Escribe un programa que pida al usuario dos números enteros e imprima la secuencia de números entre ellos (incluidos) en orden ascendente. 
# El primer número siempre será menor que el segundo.

""" numero = int(input("Introduce un número: "))
numero2 = int(input("Introduce otro número: "))

for i in range (numero, numero2+1):
    print(i, end=" ") #añadimos end=" " para imprimir los números en la misma línea con un espacio. """


# Ejercicio 12
# Escribe un programa que pida al usuario dos números enteros e imprima la secuencia de números entre ellos (incluidos) en orden ascendente. 
# Si el primer número es mayor que el segundo, imprime la secuencia en orden descendente. 
# Debes imprimir la secuencia de números en una sola línea, separados por espacios.

""" numero = int(input("Introduce un número: "))
numero2 = int(input("Introduce otro número: "))

if numero > numero2:
    for i in range(numero, numero2-1, -1):
        print(i)
else:
    for i in range(numero, numero2+1):
        print(i) """

# Ejercicio 13 ESTE EJERCICIO SE RESOLVIÓ EN CLASE
# Escribe un programa que pida al usuario un número entero positivo e imprima la tabla de multiplicar de ese número (del 1 al 10).

""" numero = int(input("Introduce un número entero positivo: "))

for i in range(1, 11, 1):
    print(f"{numero} x {i} =", numero*i)
    #print(f"{numero} x {i} = {numero*i}") #otra forma de imprimirlo """

# Ejercicio 14
# Escribe un programa que pida al usuario un número entero positivo e imprima la suma de los números pares por un lado
# y la suma de los números impares por otro. El programa debe imprimir ambos resultados.

numero = int(input("Introduce un número entero positivo: "))
suma_pares = 0
suma_impare = 0

for i in range(1, numero+1):
    if i%2 == 0:
        suma_pares +=i
    else:
        suma_impare +=i

print(f"Suma de los números pares: {suma_pares}")
print(f"Suma de los números impares: {suma_impare}")