# Ejercicio 4 - Múltiplo de 3 y 5

num_multiplo = int(input("Introduce un número entero: "))

if num_multiplo % 3 == 0:
    if num_multiplo % 5 == 0:
        print("Múltiplo de 3 y de 5.")
    else:
        print("Múltiplo de 3.")
elif num_multiplo % 5 == 0:
    print("Múltiplo de 5.")
else:
    print("No es múltiplo de 3 ni de 5.")