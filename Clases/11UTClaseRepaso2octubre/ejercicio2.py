# Ejericio 10 Hackathon de Repaso en Python
inventario = {}

while True:
    try:
        opcion = int(input("Sistema de gestión:\n 1- Añadir producto\n 2- Vender producto\n 3- Visualizar inventario\n 4- Salir\n"))
    except:
        ValueError("Tienes que escoger ua opción de la 1 a la 4")

    match opcion:
        case 1:
            nombre = input("Nombre del producto:\n")
            cantidad = int(input("Cantidad de unidades:\n"))
            inventario[nombre] = inventario.get(nombre, 0) + cantidad
        case 2:
            nombre = input("Nombre del producto:\n")
            cantidad = int(input("Cantidad de unidades:\n"))
            stock = inventario.get(nombre)
            if stock < cantidad:
                print("no existe suficiente cantidad en el inventario")
            else:
                inventario[nombre] = stock - cantidad
        case 3:
            if not inventario:
                print("Inventario vacío")
            else:
                for producto, cantidad in sorted(inventario.items()):
                    print(f"{producto}: {cantidad} unidades")
        case 4:
            print("Bye bye hasta dentro de un rato")
            exit()