# Ejercicio 5 - Invertir una lista
# Escribe un programa que pida al usuario una lista de 
# números enteros separados por espacios y la invierta. 
# El programa debe imprimir la lista invertida.

""" lista = input("Introduce numeros separados por espacios: ").split()
lista.reverse()
print(lista) """

lista = input("Introduce numeros separados por espacios: ").split()
lista_reversa =[]

for i in range(len(lista)):
    lista_reversa.append(lista.pop())

print(lista_reversa)
