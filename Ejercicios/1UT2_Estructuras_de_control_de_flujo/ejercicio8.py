# Ejercicio 8
# Escribe un programa que pida el nombre de un mes y 
# muestre cuántos días tiene (puedes simplificar febrero a 28 días siempre).

mes = input("Introduce un mes: ").lower()
if mes in ["enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre"]:
    print(f"{mes} tiene 31 días.")
elif mes in ["abril", "junio", "septiembre", "noviembre"]:
    print(f"{mes} tiene 30 días.")
elif mes in ["febrero"]:
    print(f"{mes} tiene 28 días.")
else:
    print("Introduce un mes correcto palurdo.")