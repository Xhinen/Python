# Ejercicio 1 - Sumar elementos de una lista
# Escribe un programa que pida al usuario una lista de números enteros separados por comas y calcule la suma de todos los elementos de la lista.
# El programa debe imprimir el resultado.

lista_numeros = input("Escribe una lista de números separados por coma: ").split(",")
resultado = 0

# ['1', '2', '3', '4', '5', '6']
for i in range(len(lista_numeros)):
    resultado += int(lista_numeros[i])

print(f"Resultado: {resultado}")


#otra opcion, que recorre los valores

for numero in lista_numeros:
    resultado += int(numero)

print(f"Resultado: {resultado}")

#otra opción, curiosa

lista_numeros_formato_string = input("Escribe una lista de números separados por coma: ").split(",")
lista_numero = [int(num) for num in lista_numeros_formato_string]
resultado = 0

for numero in lista_numeros:
    resultado += numero

print(f"Resultado: {resultado}")