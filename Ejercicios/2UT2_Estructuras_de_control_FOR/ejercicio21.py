# Ejercicio 21
# Escribe un programa que pida introducir un número entero positivo que corresponde al número de casos a tratar.
# Seguidamente solicite un número entero positivo que corresponde a una serie de números que el usuario va a introducir.
# Después debes recibir ese total de números e imprimirlos en la misma linea de la terminal, 
# separados por un espacio y habiéndoles sumado 1 a cada uno de ellos.

""" num_casos = int(input("Introduce el número de casos a tratar: "))

for _ in range(num_casos):
    serie_num = int(input("Números que vas a introducir: "))
    for _ in range(serie_num):
        numeros = int(input())
        print(int(numeros) + 1, end=" ")
    print() """

casos = int(input("Introduce el número de casos: "))
for _ in range(casos):
    numeros = int(input("Cuántos números vas a introducir? "))
    for _ in range(numeros):
        numero = int(input())
        print(int(numero) + 1, end=" ")
    print()