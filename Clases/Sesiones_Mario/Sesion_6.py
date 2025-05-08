#1. Crear una lista con los días de la semana y mostrar el primer y último día.
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print("Primer día de la semana: ", dias[0])
print("Último día de la semana: ", dias[-1])


#2. Modificar un elemento de una lista de frutas y agregar una fruta nueva al final.
frutas = ["Manzana", "Plátano", "Pera"]
frutas[0] = "Mango"
print(frutas)
#añado una fruta al final
frutas.append("Sandía")
print(frutas)


#3. Crear una lista vacía y llenarla con tres colores usando append().
colores = []
print(colores)#En este print no aparacerá nada
colores.append("Rojo")
colores.append("Amarillo")
colores.append("Rojo")
print(colores)#En este si


#4. Ordenar una lista de números desordenados y mostrarla al revés.
numeros = [6,2,4,0,1,12,4,6,8]
#Vamos a ordenarlos
numeros.sort()
print(numeros)
#Vamos a invertir el orden
numeros.reverse()
print(numeros)


#5. Eliminar un elemento de una lista y mostrar el resultado.
animales = ["Perro", "Pulpo", "Gato", "Rinoceronte"]
print(animales)
animales.remove("Gato")#Hay que escribirlo igual
print(animales)


#6. Contar cuántas veces aparece un número en una lista.
num = [4,6,7,8,2,3,4,5,6,7,8,9]
cantidad = num.count(2)#Indica el número de veces que se repite el número includi en count
print("El número de veces que se repite el número es: ", cantidad)


#7. Crear una tupla con tres elementos de distinto tipo y mostrar cada uno.
mi_tupla = (19, "Mario", True)
print("Número: ", mi_tupla[0])
print("String: ", mi_tupla[1])
print("Booleano: ", mi_tupla[2])

#8. Acceder al segundo elemento de una tupla anidada dentro de una lista.
datos = ["Nombre", (100,200), "Apellido"]
tupla_inter = datos[1]
print(tupla_inter)
print(tupla_inter[0])
print(tupla_inter[1])


#9. Desempaquetar una tupla en tres variables y mostrarlas con print().
persona = ("Sara", 32, "Madrid")
nombre, edad, ciudad = persona
print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad:", ciudad)


#10. Crear una lista con nombres de alumnos, cambiar el nombre del segundo y mostrar la lista completa.
lista_nombre = ["María", "Alberto", "Cristina", "Eleonora", "Dania"]
lista_nombre[1] = "Iraida"
print(lista_nombre)
