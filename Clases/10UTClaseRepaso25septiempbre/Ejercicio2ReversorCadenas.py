# Reversor de cadenas

# Pedir palabra al usuario
palabra = input("Introduce una palabra: ")

# 1. Palabra invertida
invertida = palabra[::-1]

# 2. Reemplazar vocales por *
vocales = "aeiouAEIOU"
con_censura = "".join("*" if c in vocales else c for c in palabra)

# Mostrar resultados
print("\n--- Resultado ---")
print(f"Palabra invertida: {invertida}")
print(f"Con vocales sustituidas: {con_censura}")


#solución clase

palabra = input("Introduce la palabra a invertir: ")

for i in range(len(palabra)-1, -1, -1):
    if palabra[i].lower() in ("a", "e", "i", "o", "u"):
        print("*", end="") #ponemos end="" para que no salte de linea
    else:
        print(palabra[i], end="")
print()