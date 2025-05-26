# Ejercicio 5
# Escribe un programa que pida el nombre de un día de la semana y 
# muestre si es "laborable" o "fin de semana".

dia = input("Introduce el día de la semana: ")
dia = dia.capitalize()
if dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]:
    print("Es laborable")
elif dia in ["Sábado", "Domingo"]:
    print("Es fin de semana")
else:
    print("Día incorrecto")