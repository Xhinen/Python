# Calculadora de descuentos

# Pedir datos al usuario
precio_original = float(input("Introduce el precio original del producto: "))
descuento = float(input("Introduce el porcentaje de descuento: "))

# Calcular el precio final
precio_final = precio_original * (1 - descuento / 100)

# Mostrar el resultado con dos decimales
print(f"El precio final con descuento es: {precio_final:.2f} €")
