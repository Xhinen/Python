# Eliminador de duplicados

# Pedir palabras al usuario (separadas por comas)
entrada = input("Introduce palabras separadas por comas: ")

# Dividir por comas y limpiar espacios
palabras = [p.strip() for p in entrada.split(",") if p.strip()]

# Eliminar duplicados con set y volver a lista
sin_duplicados = list(set(palabras))

# Ordenar alfabéticamente
sin_duplicados.sort()

# Mostrar resultado
print("\n--- Lista procesada ---")
print(sin_duplicados)
