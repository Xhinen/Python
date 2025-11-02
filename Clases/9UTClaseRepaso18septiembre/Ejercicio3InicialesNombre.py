# Iniciales de un nombre

# Pedir el nombre completo al usuario
nombre_completo = input("Introduce tu nombre completo: ")

# Dividir el nombre en palabras (se eliminan espacios extra automáticamente)
palabras = nombre_completo.split()

# Extraer la primera letra de cada palabra y ponerla en mayúsculas
iniciales = "".join([p[0].upper() for p in palabras])

# Mostrar el resultado
print(f"Tus iniciales son: {iniciales}")
