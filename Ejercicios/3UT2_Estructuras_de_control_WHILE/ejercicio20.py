# Ejercicio 20
# Escribe un programa que dado una serie de números introducidos por el usuario, 
# hasta que introduzca un -1, cuente cuántos de estos números son pares y cuántos son impares. 
# El programa debe imprimir el número de pares e impares introducidos, menos el -1.


pares = 0
impares = 0

while True:
    numero = int(input("Introduce un número, -1 para finalizar: "))
    if numero == -1:
        break
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"El número de pares es: {pares}")
print(f"El número de impares es: {impares}")