import json
import os
#Creamos unas preguntas de ejemplo para nuestro cuestionario y así poder probar el programa mas adelante
#Para ellos creamos una función con las preguntas
""" def preguntas_cuestionario():
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
    return preguntas """

# NOTA IMPORTANTE: TUVE QUE TIRAR UN POCO DE PARA RESOLVER EL PROBLEMA DE IMPORTAR EL ARCHIVO JSON, YA QUE POR DEFECTO
# PYTHON USA LA RUTA DEL PROYECTO COMO LA BASE Y POR LO QUE EL CODIGO DE ABAJO NO FUNCIONABA SI LA RUTA NO ERA ABSOLUTA.
""" def preguntas_cuestionario():
    with open("preguntas.json", "r") as archivo: 
        return json.load(archivo) """

# Importamos a través de una funciona las preguntamos que hemos creado en el archivo json.
def preguntas_cuestionario():
    directorio_script = os.path.dirname(os.path.abspath(__file__)) # Obtener la ruta del directorio donde está este script
    ruta_completa = os.path.join(directorio_script, "preguntas.json") # Construir la ruta completa al archivo JSON
    
    with open(ruta_completa, "r") as archivo:
        return json.load(archivo)

# Vamos a crear una función para mostrar las preguntas y su respectivas respuestas.
def mostrar_pregunta(preguntas):
    print(preguntas["pregunta"])
    for opciones in preguntas["opciones"]: #Con el for recorremos las respuestas y las imprimimos en pantalla
        print(opciones)

# Ahora creamos una función para la obtener la respuesta del usuario y evaluarla.
def respuesta_pregunta():
    #Creamos un bucle while ya que necesitas un bucle infinito hasta que se ingrese una respuesta válida.
    while True:
        respuesta = input("Elige una respuesta: ").upper() #Se pide la respuesta y la pasamos a mayúsculas con el método upper.
        if respuesta in ["A", "B", "C", "D"]: # Usamos un condiconal if para comprobar que la respuesta este dentro de las válidas.
            return respuesta # Y si es válida la devolvemos.
        print("Respuesta no válida!, introduce una respuesta válida(A, B, C o D)") # Si no es válida mostramos el mensaje de error y como es un bucle while volverá a preguntar por una respuesta correcta.

# Funcion para ver si la respuesta del usuario es correcta.
def comprobar_respuesta(resp, correcta):
    return resp == correcta # Comparamos la respuesta del usuario con la respuesta correcta.

# Función para mostrar los resultados.
def mostrar_resultados(aciertos, total):
    porcentaje = (aciertos / total) * 100 # Calculamos el porcentaje de aciertos.
    print(f"\nResultados:") 
    print(f"Preguntas: {total}") # Imprimimos el número de preguntas.
    print(f"Aciertos: {aciertos}") # Imprimimos el número de aciertos. 
    print(f"Porcentaje: {porcentaje:.1f}") # Imprimimos el porcentaje de aciertos sin decimales.

    # Ahora mostramos un mensaje basandonos en el porcentaje.
    if porcentaje >= 80: 
        print("Seguro que has hecho trampa...")
    elif porcentaje >= 60:
        print("No esta mal...")
    else:
        print(f"Tu porcentaje de aciertos ha sido del {porcentaje:.1f}\nMenudo parguela, analfabeto!")

# Creamos la función del programa principal
def main():
    preguntas = preguntas_cuestionario() # Cargamos las preguntas del archivo json que hemos importado antes.

    while True: # Creamos un bucle while para que se ejecute de nuevo en el caso de que el usuario introduzca una opción no válida.
        # Creamos el menú de la aplicación.
        print("\n=== MENÚ ===")
        print("1 - Empezar el cuestionario")
        print("2 - Salir")

        opcion = input("Elige una opción: ") # Le pedimos al usuario que elija una opción.

        # Con la opción uno iniciamos el cuestionario.
        if opcion == "1":
            nombre = input("Dime tu nombre: ")
            aciertos = 0 # Inicializamos el contador de aciertos a 0.

            # Recorremos todas las preguntas del archivo json.
            for x in preguntas:
                mostrar_pregunta(x) # Mostramos la pregunta.
                respuesta_usuario = respuesta_pregunta() # Obtenemos la respuesta
                if comprobar_respuesta(respuesta_usuario, x["respuesta_correcta"]): # Evaluamos que la respuesta sea correcta.
                    print("Respuesta correcta!!") # Imprimimos un mensaje en el caso de que sea correcta.
                    aciertos += 1 # Aumentamos el indicador de aciertos.
                else:
                    print("Incorrecto pringao") # Mensaje en el caso de que la respuesta sea incorrecta.

            mostrar_resultados(aciertos, len(preguntas)) # Mostramos los resultados del cuestionario.

        # Usamos elif para la opción 2 del programas para salir de este.
        elif opcion == "2":
            print("Ta luegooo.")
            break

        # Por ultimo, un mensaje en el caso de que introduzca una opción que no esté en el menú.
        else:
            print("Opción no válida, pulsa 1 para empezar el cuestionario o 2 para salir del programa.")

# Creamos el punto de entrada del programa.
if __name__ == "__main__":
    main() # Ejecutamos la función principal de programa.