print("-- Bienvenido al Kioskito ---")
lista_ventas = []

while True:
    opcion = input("Opciones disponibles del kiosoc0:\n1. Registrar venta\n2. Ver listados de ventas del turno\n3. Ver total recaudado\n4. Cerrar caja y Salir\n5. Buscar venta individual\nOpción seleccionada: ")
    match opcion:
        case "1":
            nombre_producto = input("Ingrese el nombre del producto: ")
            precio_unitario = input("Ingrese el precio del producto(número entero positivo): ")
            cantidad_vendida = input("Ingrese la cantidad vnedida del producto(número entero positivo): ")
            nombre_producto = nombre_producto.strip().lower()
            if precio_unitario.isdigit():
                if cantidad_vendida.isdigit():
                    if int(cantidad_vendida) != 0 and int(precio_unitario) != 0:
                        subtotal = int(cantidad_vendida) * int(precio_unitario)
                        if subtotal > 10000:
                            subtotal = subtotal * 0.9
                        producto = [nombre_producto, int(precio_unitario), int(cantidad_vendida), subtotal]
                        lista_ventas.append(producto)
                        print("Porducto y subtotal guardado con exito")
                    else:
                        print("No se acepta 0 ni en la cantidad vendida ni en el precio unitario")
                else:
                    print("La cantidad vendida debe ser un número entero positivo")
            else:
                print("E precio por unidad debe ser un númeor entero positivo")
        case "2":
            if len(lista_ventas) == 0:
                print("TOdavía no hay ninguna venta")
            else:
                for i in range(len(lista_ventas)):
                        print(f"Venta número {i+1}: {lista_ventas[i][0]}, ${lista_ventas[i][1]}, cantidad vendida: {lista_ventas[i][2]}, subtotal: {lista_ventas[i][3]}")
        case "3":
            if len(lista_ventas) == 0:
                print("TOdavía no hay ninguna venta")
            else:
                acumulador = 0
                for i in range(len(lista_ventas)):
                    acumulador += lista_ventas[i][3]
                print(f"Subtotal de ventas actual: {acumulador}")
        case "4":
            if len(lista_ventas) == 0:
                print("TOdavía no hay ninguna venta")
                break
            else:
                acumulador = 0
                for i in range(len(lista_ventas)):
                    acumulador += lista_ventas[i][3]
                print(f"Subtotal de ventas final: {acumulador}")
                break
        case "5":
            cantidad = 0
            producto_buscado = input("Ingrese el nombre dle producto que quiere buscar: ").strip().lower()
            encontrado = False
            for i in range(len(lista_ventas)):
                if producto_buscado == lista_ventas[i][0]:
                    encontrado = True
                    cantidad += lista_ventas[i][2]
                    print("El producto si fue vendido")
            if encontrado:
                print(f"Del producto {producto_buscado} se vendieron {cantidad} unidadas en este turno")
            else:
                print("No se vendió ninguna unidad dle producot hoy")
        case _:
            print("Opción inválida, selecciona una opcion del 1 al 4")