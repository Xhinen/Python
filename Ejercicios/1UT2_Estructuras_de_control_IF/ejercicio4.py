# Ejercicio 4
# Escribe un programa que pida una nota (0-10) y muestre:

# "Suspenso" si es menor de 5
# "Aprobado" si es entre 5 y 6
# "Notable" si es entre 7 y 8
# "Sobresaliente" si es 9 o 10

numero4 = float(input("Introduce una nota (0-10): "))
if numero4 >= 5 and numero4 < 7:
    print("Aprobado.")
elif numero4 >= 7 and numero4 < 9:
    print("Notable.")
elif numero4 >= 9:
    print("Sobresaliente.")
else:
    print("Suspenso")