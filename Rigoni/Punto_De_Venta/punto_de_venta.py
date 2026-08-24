print("Bienvenido al fast food")
total = 0
while True:
    opcion = input("Ingrese una opción:\n1. Agregar Hamburguesa ($4500) \n2. Agregar Papas Fritas ($2000) \n3. Agregar Bebida ($1500) \n4. Pagar el pedido (Cierra el ticket) \n5. Cancelar pedido y salir\nOpción seleccionada: ")
    match opcion:
        case "1":
            total += 4500
            print(f"Hambrguesa agregada, total actual: ${total}")
        case "2":
            total += 2000
            print(f"Papitas agregadas con éxito, total actual: ${total}")
        case "3":
            total += 1500
            print(f"Bebida agregada con éxito, total actual: ${total}")
        case "4":
            pago = input(f"El total a pagar es de ${total}, ingrese con cuanto efecito va a pagar: ")
            while not pago.isdigit() or pago == "":
                print("Debes ingresar un número entero mayor o igual que 0")
                pago = input(f"El total a pagar es de ${total}, ingrese con cuanto efecito va a pagar: ")
                pago = pago.replace(" ", "")
            pago = int(pago)
            while pago < total:
                agregado = input(f"El pago es menor que el total, de más dinero:")
                while not agregado.isdigit() or agregado == "":
                    print("Debes ingresar un número entero mayor o igual que 0")
                    agregado = input(f"El pago es menor que el total, de más dinero:")
                    agregado = agregado.replace(" ", "")
                agregado = int(agregado)
                pago += agregado
            vuelto = pago - total
            print(f"Pago realizado con éxito, se le devovlvió al usuario ${vuelto}")
            print("-" * 40)
            print("Pasa el nuevo cliente")
            total = 0
        case "5":
            print("Gracias por usar el fast food")
            break
        case _:
            print("Opción invpalida, selecciona un npumero entre 1 y 5")