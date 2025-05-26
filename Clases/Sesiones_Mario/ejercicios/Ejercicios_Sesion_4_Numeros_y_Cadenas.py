import math
# Ejercicio 6: Operaciones combinadas entre números y cadenas
# Define dos variables numéricas enteras y dos cadenas. Realiza cálculos matemáticos diversos y 
# genera una cadena formateada que explique cada operación (sumas, restas, multiplicaciones, módulo) claramente utilizando métodos de cadenas.
num1 = 12
num2 = 18
cadena1 = "La operación de "
cadena2 = " da como resultado: "
suma = cadena1 + "sumar " + str(num1) + " + " + str(num2) + cadena2 + str(num1 + num2)
resta = cadena1 + "restar "  + str(num1) + " - " + str(num2) + cadena2 + str(num1 - num2)
multiplicacion = cadena1 + "multiplicar " + str(num1) + " x " + str(num2) + cadena2 + str(num1 * num2)
division = cadena1 + "dividir " + str(num1) + " / " + str(num2) + cadena2 + str(num1 / num2)
print(suma)
print(resta)
print(multiplicacion)
print(division)


# Ejercicio 7: Cálculo del área y perímetro
# Define variables numéricas que representen dimensiones (largo, ancho, radio, altura). 
# Calcula el área y perímetro de distintas figuras geométricas (rectángulo, círculo, triángulo rectángulo) y 
# presenta todos los resultados claramente en una sola cadena formateada usando conversiones explícitas.
base = 10
altura = 15
radio = 4
area_rectangulo = "\nEl área de un rectángulo se calcula multiplicando su base que es " + str(base) + " y su altura que es " + str(altura) + ", lo que da como resultado: " + str(base * altura)
area_circulo = "\nEl área de un círculo se calcula multiplicando su radio que es " + str(radio) + " al cuadrado por la constante " + str('\u03c0') + ", lo que da como resultado: " + str((radio * radio) * math.pi)
area_triangulo_rectangulo = "\nEl área de un triángulo rectángulo se calcula dividiendo la multiplicación de sus catetos " + str(base) + " y " + str(altura) + " dividido entre 2, lo que da como resultado: " + str((base * altura)/2)
print(area_rectangulo)
print(area_circulo)
print(area_triangulo_rectangulo)


# Ejercicio 8: Análisis de texto complejo
# Define una cadena extensa que represente un párrafo completo. Utilizando únicamente métodos de cadenas y 
# funciones integradas (len, upper, split), obtén el número total de caracteres, palabras y 
# el resultado de transformar el texto completamente a mayúsculas, presentándolo claramente en una cadena nueva.
cadena_extensa = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu mi ut felis elementum vestibulum eget eu elit. Maecenas sed nulla a ante dictum euismod."
num_caracteres = len(cadena_extensa)
num_palabras = (cadena_extensa.split())
mayuscula = cadena_extensa.upper()
print(f"\nEl número total de caracteres es: {num_caracteres}")
print(f"\nEl número total de palabras es: {len(num_palabras)}")
print(f"\nMostramos la cadena en mayúsculas: {mayuscula}")


# Ejercicio 9: Fórmula cuadrática
# Dados tres números que representan los coeficientes (a, b, c) de una ecuación cuadrática, 
# resuelve la fórmula cuadrática para obtener las raíces reales o complejas. 
# Imprime claramente en una cadena formateada los coeficientes y las raíces encontradas.
a = 1
b = -1
c = -12
raiz = (b**2 - 4 * a * c)**0.5
positiva = (-b + raiz)/(2 * a)
negativa = (-b - raiz)/(2 * a)
resultado = f"Los coeficientes que tenemos para la operación son {a}, {b}, {c} que dan como resultado {positiva} y {negativa}"
print(resultado)


# Ejercicio 10: Manejo y transformación de datos personales
# Crea variables para representar datos personales (nombre, edad, peso, altura). 
# Calcula el índice de masa corporal (IMC) sin usar bucles, 
# y presenta un resumen detallado y formateado de todos estos datos personales, incluyendo el IMC con dos decimales.
nombre = "Juan"
edad = 42
peso = 85
altura = 1.80
imc = peso / (altura**2)
print(f"Nombre del paciente: {nombre}, altura {altura} y peso {peso} por tanto su índice de masa corporal es: {imc:.2f}")