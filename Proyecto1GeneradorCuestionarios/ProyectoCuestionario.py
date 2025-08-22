#Creamos unas preguntas de ejemplo para nuestro cuestionario y así poder probar el programa mas adelante
#Para ellos creamos una función con las preguntas
def preguntas_cuestionario():
    preguntas = [
        {
            "pregunta": "¿Cuál es la capital de España?",
            "opciones": ["A. Madrid", "B. Roma", "C. Londres", "D. Amsterdan"],
            "respuesta_correcta": "A"
        },
        {
            "pregunta": "¿Qué comando se usa en linux para moverse entre directorios?",
            "opciones": ["A. ls", "B. rm", "C. cd", "D. pwd"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Cuantos lados tiene un cubo?",
            "opciones": ["A. 12", "B. 9", "C. 4", "D. 6"],
            "respuesta_correcta": "D"
        }

    ]
    return preguntas


# Vamos a crear una función para mostrar las preguntas.
def mostrar_pregunta(preguntas):
    print(preguntas["pregunta"])
    for opciones in preguntas["opciones"]:
        print(opciones)

# Ahora creamos una función para la respuesta del usuario
def respuesta_usuario():
    while True:
        respuesta = input("Elige una respuesta: ").upper() #Añadimos el método upper por si el usuario introduce la respuesta en minúscula convertirla en mayúscula
        if respuesta in ["A", "B", "C", "D"]:
            return respuesta
        print("Respuesta no válida!, introduce una respuesta válida(A, B, C o D)")

# Funcion para corregir la respuesta del usuario
def comprobar_respuesta(resp, correcta):
    return resp == correcta

# Y ahora mostramos los resultados