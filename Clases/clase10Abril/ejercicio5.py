# Ejercicio 5 - 

rol = input("Introduce tu rol: ").lower
academy = input("Introduce tu academia: ").lower

if rol == "alumno" and academy == "prometeo":
    print("Tienes acceso al Discord oficial y de alumnos.")
elif rol == "profesor" and academy == "prometeo":
    print("tienes acceso al Discord oficial.")
else:
    print("No tienes acceso.")
    