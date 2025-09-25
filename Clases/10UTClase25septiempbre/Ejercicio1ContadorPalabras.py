# Análisis de frase: palabras inicial y final

# Pedir la frase al usuario
frase = input("Introduce una frase completa: ")

# Dividir en palabras (elimina espacios extra)
palabras = frase.strip().split()

# Contar palabras
num_palabras = len(palabras)

# Identificar primera y última palabra
if palabras:  # evitar error si está vacío
    primera = palabras[0]
    ultima = palabras[-1]
else:
    primera = ""
    ultima = ""

# Mostrar resultados
print("\n--- Análisis de la frase ---")
print(f"Número total de palabras: {num_palabras}")
print(f"Primera palabra: {primera}")
print(f"Última palabra: {ultima}")