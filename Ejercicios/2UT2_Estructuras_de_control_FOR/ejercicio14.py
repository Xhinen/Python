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