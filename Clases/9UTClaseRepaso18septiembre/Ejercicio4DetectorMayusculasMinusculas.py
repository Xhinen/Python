# Detector de mayúsculas y minúsculas

# Pedir la cadena de texto al usuario
texto = input("Introduce una cadena de texto: ")

# Contadores
mayusculas = sum(1 for c in texto if c.isupper())
minusculas = sum(1 for c in texto if c.islower())
""" digitos = sum(1 for c in texto if c.isdigit())
espacios = sum(1 for c in texto if c.isspace())
otros = len(texto) - (mayusculas + minusculas + digitos + espacios) """

# Mostrar estadísticas
print("\n--- Estadísticas del texto ---")
print(f"Total de caracteres: {len(texto)}")
print(f"Letras mayúsculas: {mayusculas}")
print(f"Letras minúsculas: {minusculas}")
""" print(f"Dígitos: {digitos}")
print(f"Espacios: {espacios}")
print(f"Otros caracteres: {otros}") """
