# Ejercicio 6 - Dias de la semana
# Escribe un programa que reciba números enteros positivos hasta la introducción de un 0. Por cada número, 
# suponiendo que el 1 representa el lunes, el 2 el martes, etc., 
# imprime el nombre del día correspondiente.

lista_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# 2//7 = 0
# 2%7 = 2

while True:
    numero = int(input("Ingrese un número (0 para salir): "))
    if numero == 0:
        print("Programa terminado")
        break
    print(lista_dias[(numero%7)-1])