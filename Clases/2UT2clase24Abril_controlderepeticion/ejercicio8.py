#hacer un cuadrado con una "X" dentro (esto es una fumada)
dimension = int(input("Introduce un numero entero impar q..."))

for i in range( dimension+1):
    for j in range(dimension+1):
        if i == 0 or i == dimension or j == 0 or j == dimension:
            print("*", end="")
        else:
            if i == j or i + j == dimension:
                print("*", end="")
            else:
                print(" ", end="")
    print()