# Ejercicio 1
# Escribe un programa que pida al usuario un número entero y determine si es par o impar.
# El programa debe imprimir un mensaje indicando el resultado.

""" numero = int(input("Introduce un número entero: "))
if numero % 2 == 0:
    print("El número es par.")

else:
    print("El número es impar.") """


# Ejercicio 2
# Escribe un programa que pida al usuario un número entero y determine si es positivo, negativo o cero.
# El programa debe imprimir un mensaje indicando el resultado.

""" numero2 = int(input("Introduce un número entero: "))
if numero2 > 0:
    print("El número {numero2} es positivo.")
elif numero2 < 0:
    print("El número {numero2} es negativo.")
else:
    print("El número es 0.") """

# Ejercicio 3
# Escribe un programa que pida al usuario un número entero y determine si es divisible por 3 y 5.
# El programa debe imprimir un mensaje indicando el resultado.

""" numero3 = int(input("Introduce un número entero: "))
if numero3 % 3 == 0 and numero3 % 5 == 0:
    print(f"El número {numero3} es divisible de 3 y 5.")
else:
    print(f"El número {numero3} no es divisible de 3 y 5.") """

# Ejercicio 4
# Escribe un programa que pida una nota (0-10) y muestre:

# "Suspenso" si es menor de 5
# "Aprobado" si es entre 5 y 6
# "Notable" si es entre 7 y 8
# "Sobresaliente" si es 9 o 10

""" numero4 = float(input("Introduce una nota (0-10): "))
if numero4 >= 5 and numero4 < 7:
    print("Aprobado.")
elif numero4 >= 7 and numero4 < 9:
    print("Notable.")
elif numero4 >= 9:
    print("Sobresaliente.")
else:
    print("Suspenso") """

# Ejercicio 5
# Escribe un programa que pida el nombre de un día de la semana y 
# muestre si es "laborable" o "fin de semana".

""" dia = input("Introduce el día de la semana: ")
dia = dia.capitalize()
if dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]:
    print("Es laborable")
elif dia in ["Sábado", "Domingo"]:
    print("Es fin de semana")
else:
    print("Día incorrecto") """

# Ejercicio 6
# Escribe un programa que pida un año y muestra si es bisiesto. 
# Un año es bisiesto si es divisible por 4, pero no por 100, o si es divisible por 400.

""" year = int(input("Introduce un año: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto") """

# Ejercicio 7
# Escribe un programa que pida dos números y un operador (+, -, *, /) 
# y muestre el resultado de la operación.

""" numero1 = int(input("Introduce un número: "))
numero2 = int(input("Introduce otro número: "))
operador = input("Introduce el operador +, -, *, /: ")
if operador == "+":
    resultado = numero1 + numero2
elif operador == "-":
    resultado = numero1 - numero2
elif operador == "*":
    resultado = numero1 * numero2
elif operador == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "No se puede dividir por 0."
else:
    print("Introduce operadores o numeros correctos, vuelve a intentarlo")

print(f"Resultado: {resultado}") """

# Ejercicio 8
# Escribe un programa que pida el nombre de un mes y 
# muestre cuántos días tiene (puedes simplificar febrero a 28 días siempre).

""" mes = input("Introduce un mes: ").lower()
if mes in ["enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre"]:
    print(f"{mes} tiene 31 días.")
elif mes in ["abril", "junio", "septiembre", "noviembre"]:
    print(f"{mes} tiene 30 días.")
elif mes in ["febrero"]:
    print(f"{mes} tiene 28 días.")
else:
    print("Introduce un mes correcto palurdo.") """

# Ejercicio 9
# Escribe un programa que pida el precio de un producto y, 
# si supera los 100€, aplique un descuento del 10%. Muestra el precio final.

""" precio = float(input("Indica el precio del producto: "))
descuento = precio * 0.10
if precio > 100:
    print("El resultado es:", precio - descuento)
elif precio <= 100:
    print("El precio no incluye descuento")
else:
    print("Introduce un numero idiota") """

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