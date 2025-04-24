# Ejercicio 6 - Triángulo de asteriscos
# Escribe un programa que pida al usuario un número entero positivo y dibuje un triángulo de asteriscos con la altura especificada. 
# Por ejemplo, si el usuario ingresa 5, el triángulo debe verse así:

altura = int(input("Introduce la altura del triángulo: "))

for i in range(1,altura+1):
    print("*"*i)


""" altura = int(input("Introduce un número: "))

if altura > 0:
    
    for i in range(1, altura + 1):
        print("*" * i)
else:
    print("Por favor, introduce un número entero positivo.") """