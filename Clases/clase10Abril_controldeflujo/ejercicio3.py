# Ejercicio 3 - Pacman

# nombre_usuario - snake_case --> Python
# nombreUsuario - camelCase --> Java

pos_pacman = int(input("Cual es la posición de pacman? "))
pos_fantasma = int(input("Cual es la posición de fantasma? "))

if pos_pacman == pos_fantasma:
    # Caramelo -> Pacman come fantasma
    # Invisible -> Pacman escapa
    # Normal -> Pacman atrapado
    estado_pacman = input("Como está pacman? ")
    if estado_pacman == "caramelo":
        print("Pacman se ha comido al fantasma")
    elif estado_pacman == "invisible":
        print("Pacman ha escapado")
    else:
        print("Pacman ha sido atrapado")
else:
    print("Pacman ha escapado")
