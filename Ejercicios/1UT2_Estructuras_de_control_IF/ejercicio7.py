# Ejercicio 7
# Escribe un programa que pida dos números y un operador (+, -, *, /) 
# y muestre el resultado de la operación.

numero1 = int(input("Introduce un número: "))
numero2 = int(input("Introduce otro número: "))
operador = input("Introduce el operador +, -, *, /: ")
if operador == "+":
    resultado = numero1 + numero2
elif operador == "-":
    resultado = numero1 - numero2
elif operador == "*":
    resultado = numero1 * numero2
elif operador == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "No se puede dividir por 0."
else:
    print("Introduce operadores o numeros correctos, vuelve a intentarlo")

print(f"Resultado: {resultado}")