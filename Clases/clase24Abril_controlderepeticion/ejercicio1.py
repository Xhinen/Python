""" for i in range(5):
    print(i) """

""" for i in range(0,10,2): #dentro del rango se representa(en este orden) el inicio, el final(no incluido) y el número de saltos.
    print(i) """

""" for i in range(11):
    if i%2 == 1:
        continue
    print(i) """

""" for i in range(11):# [0,1,2,3,4,5,6,7,8,9,10]
    if i%2 == 1:
        break
    print(i) """

# Ejercicio 1 - Contador¶
# Escribe un programa que pida al usuario un número entero positivo e imprima los números desde el 0 hasta ese número (incluido). 
# El programa debe imprimir los números en cada iteración.

numero = int(input("Introduce un número positivo: "))
for i in range(0, numero+1):
    print(i)

