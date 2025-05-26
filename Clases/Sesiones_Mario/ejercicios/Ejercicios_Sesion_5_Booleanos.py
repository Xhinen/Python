# Ejercicio 5: Operaciones con Cadenas y Números
# 📌 Objetivo: Realizar operaciones matemáticas con cadenas y números.
# Concatenar cadenas con números usando str().
# Multiplicar una cadena para repetirla varias veces.

numero = input("Introduce tu edad: ")
cadena = f"\nTengo {numero} años "
multi_cadena = cadena * 5
print(cadena)
print(multi_cadena)

# Ejercicio 6: Operaciones con Caracteres y Códigos ASCII
# 📌 Objetivo: Explorar caracteres y su representación en ASCII.
# Obtén el código ASCII de la letra 'A'.
# Convierte un número en su carácter ASCII correspondiente.

ascii_letra = input("Introduce una letra: ")
convertir_letra = ord(ascii_letra)
print(convertir_letra)
ascii_num = input("Introduce un número del 0 al 9: ")
convertir_num = ord(ascii_num)
print(convertir_num)

# Ejercicio 7: Evaluación de Expresiones Lógicas
# 📌 Objetivo: Trabajar con operadores lógicos (and, or, not).
# Evalúa expresiones lógicas combinando números y operadores lógicos.
# Muestra los resultados.

expresion_1 = 3 > 2 and 5 < 10
expresion_2 = 3 > 7 or 15 < 10
expresion_3 = not(3 > 2 and 5 < 10)
print(expresion_1)
print(expresion_2)
print(expresion_3)

# Ejercicios para casa
# Ejercicio 1: Comparación de números y booleanos
# 📌 Objetivo: Usar comparaciones con números y analizar los resultados booleanos.
# Crea tres variables numéricas con valores diferentes.
# Compara los valores entre sí (>, <, >=, <=, ==, !=).
# Almacena los resultados en nuevas variables booleanas y muéstralos.

expresion1 = "9 >= 5"
expresion2 = "17 < 10"
expresion3 = "27 > 25"
expresion4 = "18 == 18"
expresion5 = "15 != 15"
print(f"\n - La expresión {expresion1} es {eval(expresion1)}\n"
      f" - La expresión {expresion2} es {eval(expresion2)}\n"
      f" - La expresión {expresion3} es {eval(expresion3)}\n"
      f" - La expresión {expresion4} es {eval(expresion4)}\n"
      f" - La expresión {expresion5} es {eval(expresion5)}\n")

# Ejercicio 2: Propiedades y manipulación de cadenas
# 📌 Objetivo: Trabajar con cadenas y métodos integrados de Python.
# Crea una cadena con una frase corta.
# Muestra cuántos caracteres tiene la cadena.
# Convierte toda la cadena a mayúsculas y minúsculas.
# Cuenta cuántas veces aparece una letra específica en la cadena.

cadena = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu mi ut felis elementum vestibulum eget eu elit."
num_caracteres = len(cadena)
mayusculas = cadena.upper()
minusculas = cadena.lower()
letra = input("Introduce una letra: ")
contador = cadena.count(letra)
print(f"\nEl número total de caracteres es: {num_caracteres}"
      f"\nMostramos la cadena en mayúsculas: {mayusculas}"
      f"\nMostramos la cadena en minúsculas: {minusculas}"
      f"\nLa letra aparece letra {letra} aparece {contador} veces")


# Ejercicio 3: Operaciones matemáticas con números y booleanos
# 📌 Objetivo: Realizar cálculos numéricos usando valores booleanos.
# Define dos variables booleanas (verdadero, falso) con los valores True y False.
# Realiza operaciones matemáticas con estos valores (+, *, -).
# Muestra los resultados y analiza qué sucede.

verdadero = True
falso = False
print("Suma entre números y booleanos: ", verdadero + 2, falso + 2)
print("Resta entre números y booleanos: ", verdadero - 3, falso - 3)
print("Multiplicación entre números y booleanos: ", verdadero * 4, falso * 4)

# Ejercicio 4: Extracción de caracteres en una cadena
# 📌 Objetivo: Extraer partes de una cadena utilizando índices y slicing.
# Define una cadena con una palabra o nombre.
# Extrae y muestra los tres primeros caracteres.
# Extrae y muestra los tres últimos caracteres.
# Extrae los caracteres en posiciones impares de la cadena.

cadena = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus et"
print(cadena[:3])
print(cadena[-2:])
print(cadena[1::2])

# Ejercicio 5: Conversión de tipos y evaluación booleana
# 📌 Objetivo: Convertir entre tipos básicos y analizar valores booleanos.
# Convierte un número en una cadena y muestra el tipo de dato.
# Convierte una cadena numérica en un número entero y muestra el tipo.
# Convierte diferentes valores ("", "Texto", 0, 1, -1, None) a booleanos y muestra los resultados.

numero = 546
numero_cadena = str(numero)
print("El tipo de dato es", type(numero_cadena))
numero2_cadena = "325"
numero2 = int(numero2_cadena)
print("El tipo de dato es", type(numero2))
valor1 = bool("")
valor2 = bool("Texto")
valor3 = bool(0)
valor4 = bool(1)
valor5 = bool(-1)
valor6 = bool(None)
print(valor1)
print(valor2)
print(valor3)
print(valor4)
print(valor5)
print(valor6)