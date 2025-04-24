# Ejercicio 13¶ (este es de los de nivel básico pero lo hemos resuelto en clase)
# Escribe un programa que pida al usuario un número entero positivo e imprima la tabla de multiplicar de ese número (del 1 al 10).

numero = int(input("Introduce un número entero positivo: "))

for i in range (1, 11):
    print(f"{numero} x {i} = {numero*i}")