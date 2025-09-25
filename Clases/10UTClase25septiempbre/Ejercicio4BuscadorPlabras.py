# Buscador de palabras

# Pedir al usuario un texto largo
texto = input("Introduce un texto: ")

# Pedir la palabra a buscar
palabra = input("Introduce la palabra que quieres localizar: ")

# --- Búsqueda sensible a mayúsculas/minúsculas ---
conteo_sensible = texto.split().count(palabra)

# --- Búsqueda insensible a mayúsculas/minúsculas ---
conteo_insensible = texto.lower().split().count(palabra.lower())

# Mostrar resultados
print("\n--- Resultados de la búsqueda ---")
print(f"Sensible a mayúsculas/minúsculas: '{palabra}' aparece {conteo_sensible} veces")
print(f"No sensible a mayúsculas/minúsculas: '{palabra}' aparece {conteo_insensible} veces")


