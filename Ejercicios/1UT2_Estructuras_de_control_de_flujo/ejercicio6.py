# Ejercicio 6
# Escribe un programa que pida un año y muestra si es bisiesto. 
# Un año es bisiesto si es divisible por 4, pero no por 100, o si es divisible por 400.

year = int(input("Introduce un año: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")