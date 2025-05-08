# Parte 1: Booleanos y Operaciones con Números
# Ejercicio 1: Evaluación de Expresiones Booleanas
# 📌 Objetivo: Evaluar expresiones numéricas que devuelvan valores booleanos.
# Crea variables con expresiones matemáticas y convierte los resultados en booleanos.
# Muestra el valor booleano de cada una.
expresion1 = 10>5
expresion2 = 7+3 == 10
expresion3 = 20<15
expresion4 = 4*2 == 9

print(expresion1, expresion2, expresion3, expresion4)

# Ejercicio 2: Operaciones Matemáticas con Booleanos
# 📌 Objetivo: Descubrir cómo Python trata los valores True y False en operaciones matemáticas.
# Suma True + True y False + True.
# Multiplica True * 10 y False * 50.
# Muestra los resultados y explica qué ocurre.
print(True+True)
print(False+True)
print(False+False)
print(True*10)
print(False*50)

# Ejercicio 3: Conversión entre Tipos Básicos
# 📌 Objetivo: Convertir entre tipos de datos (números, cadenas y booleanos).
# Convierte un número en cadena y muéstralo.
# Convierte una cadena numérica en un entero.
# Convierte un booleano en un número.
# convierto un número en cadena

numero = 123
cadena = str(numero)
print(cadena)  # "123"
# convierto una cadena numérica en entero
cadena_numerica = "456"
numero_convertido = int(cadena_numerica)
print(numero_convertido)  # 456
# convierto un booleano en número
print(int(True))  # 1
print(int(False))  # 0

# Ejercicio 4: Propiedades de las Cadenas
# 📌 Objetivo: Manipular cadenas y explorar sus propiedades.
# Crea una cadena con tu nombre.
# Muestra el primer y último carácter.
# Muestra la longitud de la cadena.
# Convierte la cadena a mayúsculas y minúsculas.
nombre = "Mario"
print(nombre[0])
print(nombre[-1])
# print(nombre[5]) Dará error ya que el nombre no tiene 6 caracteres (recuerda que empezamos por 0)
print(nombre[4])
print(nombre[-2])
print(nombre[-3])
print(nombre[-4])

#El resto de ejercicios de booleanos para casa


#EJERCICIOS DICCIONARIOS

# ✅ Ejercicio 1: Crear un diccionario simple
# Enunciado: Crea un diccionario que almacene información de una persona: nombre, edad y si está registrado (booleano).
persona = {
    "nombre" : "Alberto",
    "edad" : 32,
    "registradoEnElCenso" : True
}
print(persona)

# ✅ Ejercicio 2: Acceder a un valor por su clave
# Enunciado: Imprime el valor de la clave "edad" del diccionario persona(del ejecicio anterior).
print(persona["edad"])

# ✅ Ejercicio 3: Añadir una nueva clave-valor
# Enunciado: Añade al diccionario persona la clave "ciudad" con valor "Burgos".
persona["Ciudad"]  = "Granada"
print(persona)

# ✅ Ejercicio 4: Cambiar el valor de una clave
# Enunciado: Cambia la edad de la persona a 31.
persona["edad"] = 39
print(persona["edad"])

# ✅ Ejercicio 5: Eliminar una clave del diccionario
# Enunciado: Elimina la clave "ciudad" del diccionario persona.
del persona["Ciudad"]
print(persona)

# ✅ Ejercicio 6: Comprobar si una clave existe (con booleano)
# Enunciado: Crea una variable booleana que indique si existe la clave "nombre" en el diccionario persona.
existe_nombre = "nombre" in persona
print(existe_nombre)

# ✅ Ejercicio 7: Comparar dos valores booleanos
# Enunciado: Compara si la persona está registrada y tiene más de 18 años. Guarda el resultado en una variable booleana.
es_mayor_y_registrado = persona["edad"]>18 and persona["registradoEnElCenso"]
print(es_mayor_y_registrado)

# ✅ Ejercicio 8: Usar NOT con un valor booleano
# Enunciado: Invierte el valor de "registrado" y muestra el resultado.
no_registrado = not persona["registradoEnElCenso"]
print(no_registrado)

# ✅ Ejercicio 9: Crear un conjunto a partir de una lista con duplicados
# Enunciado: Elimina duplicados de esta lista: [1, 2, 2, 3, 3, 3] usando un conjunto.
numeros = [2, 2, 3, 4, 5, 3, 4, 5, 2, 1]
conjunto = set(numeros) #con set ordenamos y eliminamos los números repetidos
print(conjunto)

# ✅ Ejercicio 10: Comparar si dos colecciones tienen los mismos elementos únicos
# Enunciado: Compara si las listas [1, 2, 2, 3] y [3, 1, 2] tienen los mismos elementos únicos.
lista1 = set([1, 2, 3, 4])
lista2 = set([5, 4, 3, 2, 1])
mismos_elementos = lista1 == lista2
print(mismos_elementos)