import random
from statistics import mode

# 1. Simulación de 10 tiradas de un dado de 6 caras
tiradas = [random.randint(1, 6) for i in range(10)]

# 2. Almacenar resultados en lista (ya hecho arriba)

# 3. Mostrar tiradas
print("--- Resultados de las tiradas ---")
print(tiradas)

# 4. Calcular la moda (número más frecuente)
try:
    mas_frecuente = mode(tiradas)
    print(f"\nLa moda es: {mas_frecuente}")
except:
    print("\nNo hay una única moda (varios números con la misma frecuencia).")


#solucion clase

dados = ()
repeticiones = list[0]*6

for i in range(10):
    tirada = random.randint(1, 6)
    tiradas.append(tirada)
    repeticiones[tirada-1] += 1

reps = -1
moda = 0
for i in range (6):
    if repeticiones[i] > reps:
        moda = i
        reps = repeticiones[i]


print(f"Las tiradas han sido {dados}")
print(f"El primer más repetido es {moda+1}")