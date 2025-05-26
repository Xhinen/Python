# Ejercicio 16
# Escribe un programa que pida al usuario un número entero positivo e imprima la lista de divisores de ese número. 
# Un divisor de un número n es un número entero que divide a n sin dejar residuo. 
# El programa debe imprimir todos los divisores del número introducido.

numero = int(input("Introduce un número entero positivo: "))

for i in range(1, numero + 1):
    if numero % i == 0:
        print(f"{i} es divisor de {numero}")


#Solucion profesor
""" numero = int(input("Introduce un número entero positivo: "))

print(f"Los divisores de {numero} son: ", end=" ")
for i in range(1, numero + 1):
    if numero % i == 0:
        print(i, end=" ")
print() """