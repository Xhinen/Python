# Ejercicio 2 - Contar elementos de una lista
# Escribe un programa que pida al usuario una lista de palabras separadas por comas y cuente cuántas palabras hay en la lista. 
# El programa debe imprimir el resultado.

print("la logintud de la lista es: ", len(input("Introduce una lista de palabras separadas por coma: ").split(",")))

#Sin usar len

lista_palabra = input("Introduce una lista de palabras separadas por coma: ").split(",")
resultado = 0

for palabra in lista_palabra:
    resultado += 1

print("La longitud de la lista es: ", resultado)