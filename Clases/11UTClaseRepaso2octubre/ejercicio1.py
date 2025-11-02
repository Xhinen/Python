# Ejericio 9 Hackathon de Repaso en Python
lista_peliculas = list()

opcion = input("Introduce una película (Introduce fin para acabar):\n")
while opcion != "fin":
    lista_peliculas.append(opcion)
    opcion = input("Introduce otra película (fin para acabar):\n")

print(f"Número total de peliculas: {len(lista_peliculas)}")
print(f"La primera película es: {lista_peliculas[0]}")
print(f"La última película es: {lista_peliculas[-1]}")
print(f"Número total de peliculas sin repetir: {set(lista_peliculas)}")