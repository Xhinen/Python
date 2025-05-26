# Ejercicio 9
# Escribe un programa que pida el precio de un producto y, 
# si supera los 100€, aplique un descuento del 10%. Muestra el precio final.

precio = float(input("Indica el precio del producto: "))
descuento = precio * 0.10
if precio > 100:
    print("El resultado es:", precio - descuento)
elif precio <= 100:
    print("El precio no incluye descuento")
else:
    print("Introduce un numero idiota")