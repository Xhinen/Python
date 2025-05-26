# Ejercicio 10
# Escribe un programa que pida día, mes y año. Comprueba si la fecha introducida es válida.
# Recuerda que, en los años bisiestos, febrero tiene 29 días.
# Puedes usar el algoritmo del ejercicio 6 para determinar si un año es bisiesto.

""" dia = int(input("Introduce un día: "))
mes = int(input("Introduce un mes(en numero): "))
year = int(input("Introduce un año: "))
# validamos el mes
if mes < 1 or mes > 12:
    # comprobamos que el año sea bisiesto
    bisiesto = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    # ahora validamos los día según el mes
    if dia < 1:
        print("El día introducido no es correcto.")
    elif mes == 2 and bisiesto and dia > 29:
        print("Febrero no tiene mas de 29 días.")
    elif mes == 2 and not bisiesto and dia > 28:
        print("Febrero no tienes mas de 28 días.")
    elif mes in (4, 6, 9, 11) and dia > 30:
        print("abril, junio, septiembre y noviembre no tienen mas de 30 días.")
    elif mes in (1, 3, 5, 7, 8, 10, 12) and dia > 31:
        print("enero, marzo, mayo, julio, agosto, octubre y diciembre no tienen mas de 31 días.")
else:
    print(f"La fecha {dia}/{mes}/{year} es correcta.") """

""" dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes (1-12): "))
año = int(input("Introduce el año: "))
bisiesto = (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

if mes < 1 or mes > 12:
    print("Mes no válido.")
elif dia < 1 or (mes == 2 and bisiesto and dia > 29) or (mes == 2 and not bisiesto and dia > 28) or (mes in [4, 6, 9, 11] and dia > 30) or (mes in [1, 3, 5, 7, 8, 10, 12] and dia > 31):
    print("Fecha no válida.")
else:
    print(f"La fecha {dia}/{mes}/{año} es válida.") """

dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes (1-12): "))
año = int(input("Introduce el año: "))

if mes < 1 or mes > 12:
    print("Mes no válido.")
elif dia < 1 or (mes == 2 and ((año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)) and dia > 29) or (mes == 2 and not ((año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)) and dia > 28) or (mes in [4, 6, 9, 11] and dia > 30) or (mes in [1, 3, 5, 7, 8, 10, 12] and dia > 31):
    print("Fecha no válida.")
else:
    print(f"La fecha {dia}/{mes}/{año} es válida.")