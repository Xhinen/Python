# Censor de palabras prohibidas

# 1. Crear lista de palabras prohibidas
prohibidas = ["malo", "tonto", "feo"]  # Puedes ampliar esta lista

# 2. Solicitar frase al usuario
frase = input("Introduce una frase: ")

# 3. Reemplazar palabras prohibidas por ***
palabras = frase.split()
frase_censurada = []

for palabra in palabras:
    if palabra.lower().strip(".,!?") in prohibidas:
        frase_censurada.append("***")
    else:
        frase_censurada.append(palabra)

# 4. Mostrar resultado
print("\n--- Frase censurada ---")
print(" ".join(frase_censurada))
