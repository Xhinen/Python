# Analizador de texto

# Pedir frase al usuario
frase = input("Introduce una frase: ")

# 1. Conteo de caracteres (incluyendo espacios y signos)
total_caracteres = len(frase)

# 2. Número de palabras
palabras = frase.split()
num_palabras = len(palabras)

# 3. Palabra más larga
if palabras:  # evitar error si la frase está vacía
    palabra_mas_larga = max(palabras, key=len)
else:
    palabra_mas_larga = ""

# Mostrar resultados
print("\n--- Análisis del texto ---")
print(f"Total de caracteres: {total_caracteres}")
print(f"Número de palabras: {num_palabras}")
print(f"Palabra más larga: {palabra_mas_larga}")
