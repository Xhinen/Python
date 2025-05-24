mi_lista = [1, 2, 3, 4, 5]

print(f"Elemento popeado: {mi_lista.pop}" )

# LIFO - Last In First Out

print("Lista popeada: ", mi_lista)

mi_lista.append(6)

print("Lista con nuevo elemento: ", mi_lista)

mi_lista.insert(0, 6)

print("Lista con nuevo elemento: ", mi_lista)

mi_lista.remove(3) #Si hay dos valores iguales siempre borrará el primero

print("Lista con nuevo elemento: ", mi_lista)

print("Lista ordenada: ", mi_lista.sort())