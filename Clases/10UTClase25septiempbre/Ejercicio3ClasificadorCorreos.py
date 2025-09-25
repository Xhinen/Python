# Clasificador de correos

# Entrada: pedir correos separados por comas
entrada = input("Introduce varias direcciones de correo separadas por comas: ")

# Procesamiento: limpiar espacios y guardar en lista
correos = [c.strip() for c in entrada.split(",") if c.strip()]

# Clasificación en dos listas
gmail = [c for c in correos if c.lower().endswith("@gmail.com")]
thepower = [c for c in correos if c.lower().endswith("@thepower.com")]
otros = [c for c in correos if not c.lower().endswith("@gmail.com")]

# Resultado final
print("\n--- Clasificación de correos ---")
print(f"Gmail: {gmail}")
print(f"thepower: {thepower}")
print(f"Otros: {otros}")


#solución clase

correos = input("Introduce varias direcciones de correo separadas por comas:\n").split(",")
correos_clas = {}

for correo in correos:
    #jordi.cidoncha@gmail.com
    correo_separado = correo.split("@")[1]
    extension = correo.split("@")[1].split(".")[0]
    if extension not in correos_clas.keys():
        correos_clas[extension] = list()
    
    correos_clas[extension].append(correo)

print(correos_clas)