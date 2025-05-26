# Ejercicio 17
# Escribe un programa que reciba un número entero positivo y una letra.
# El programa debe imprimir la letra tantas veces como el número introducido.

num_positivo = int(input("Introduce un número positivo: "))
letra = str(input("introduce una letra: "))

for i in range (num_positivo):
    print(f"{letra}")

print()