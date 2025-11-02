# Clasificador de edades

# Pedir la edad al usuario
edad = int(input("Introduce tu edad: "))

# Clasificación según rangos
if edad < 0:
    print("La edad no puede ser negativa.")
elif 0 <= edad <= 12:
    print("Eres un niño.")
elif 13 <= edad <= 17:
    print("Eres un adolescente.")
elif 18 <= edad <= 64:
    print("Eres un adulto.")
else:  # edad >= 65
    print("Eres un senior.")
