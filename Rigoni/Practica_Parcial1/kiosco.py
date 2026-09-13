productos =[]
precios = []
cantidades = []

while True:
    menu = input("Selecciona una opción:\n1. Carga inicial de productos\n2. Carga de ventas del día\n3. Mostrar lista de precios y ventas del día\n4. Consulta de un producto\n5. Reporte de productos sin ventas\n6. Agregar producto nuevo\n7. Registrar venta\n8. Cerrar caja(Finalizar día)\n9. Salir\nOpción seleccionada: ")
    match menu:
        case "1":
            if len(productos) == 0:
                cantidad_productos = input("Ingrese la cantidad de procutos a cargar: ")
                cantidad_productos = cantidad_productos.replace(" ","")
                while not cantidad_productos.isdigit() or int(cantidad_productos) <= 0:
                    print("Error, debes ingresar un número entero positivo")
                    cantidad_productos = input("Ingrese la cantidad de procutos a cargar: ")
                    cantidad_productos = cantidad_productos.replace(" ","")
                cantidad_productos = int(cantidad_productos)
                for i in range(cantidad_productos):
                    nombre = input(f"Ingrese el nombre del producto {i+1}: ")
                    nombre = nombre.replace(" ", "")
                    while not nombre.isalpha() or nombre == "":
                        print("Error, el nombre ingresado no puede contener números ni estar vacío")
                        nombre = input(f"Ingrese el nombre del producto {i+1}: ")
                        nombre = nombre.replace(" ", "")
                    productos.append(nombre.lower())
                    precio_unidad = input(f"Ingrese el precio del producto {i+1}: ")
                    precio_unidad = precio_unidad.replace(" ", "")
                    while not precio_unidad.isdigit() or int(precio_unidad) <= 0:
                        print("Error, debes ingresar un número entero positivo")
                        precio_unidad = input(f"Ingrese el precio del producto {i+1}: ")
                        precio_unidad = precio_unidad.replace(" ","")
                    precio_unidad = int(precio_unidad)
                    precios.append(precio_unidad)
                    cantidades.append(0)
                print("CARGA REALIZADA CON ÉXITO")
                print("=" * 30)
            else:
                print("Error, esta opción solo se puede usar 1 vez y ya fue usada")
        case "2":
            if len(productos) == 0:
                print("Error, debes realizar la carga de productos inicial primero(opción 1)")
            else:
                for i in range(len(productos)):
                    unidades_vendidas = input(f"Ingrese las unidades vendidas de {productos[i]}: ")
                    unidades_vendidas = unidades_vendidas.replace(" ", "")
                    while not unidades_vendidas.isdigit() or int(unidades_vendidas) < 0:
                        print("Error, debes ingresar un número entero positivo o cero")
                        unidades_vendidas = input(f"Ingrese las unidades vendidas de {productos[i]}: ")
                        unidades_vendidas = unidades_vendidas.replace(" ", "")
                    cantidades[i] += int(unidades_vendidas)
                print("CARGA DE VENTAS REALIZADA CON ÉXITO")
                print("=" * 30)
        case "3":
            for i in range(len(productos)):
                print(f"{productos[i]} | ${precios[i]} | {cantidades[i]} unidades vendidas | recaudación total: ${precios[i] * cantidades[i]}")
            print("=" * 30)
        case "4":
            buscado = input("Ingrese el nombre del producto para mostrar sus datos: ")
            buscado = buscado.replace(" ", "")
            if buscado.lower() in productos:
                for i in range(len(productos)):
                    if buscado == productos[i]:
                        print(f"{productos[i]} | ${precios[i]} | {cantidades[i]} unidades vendidas | recaudación total: ${precios[i] * cantidades[i]}")
            else:
                print(f"El producto {buscado} no se encuentra en el kiosco")
            print("=" * 30)
        case "5":
            print("Listado de productos con 0 ventas:")
            for i in range(len(productos)):
                if cantidades[i] == 0:
                    if i + 1 == len(productos):
                        print(f"{productos[i]}")
                    else:
                        print(f"{productos[i]}", end = ", ")
            print("=" * 30)
        case "6":
            producto_agregado = input("Ingresa el producto que quieres añadir al kiosco: ")
            producto_agregado = producto_agregado.replace(" ", "")
            if producto_agregado == "":
                print("El nombre del producto a agregar no puede estar vacío")
            elif not producto_agregado.isalpha():
                print("El nombre del producto no puede contener números")
            elif producto_agregado.lower() in productos:
                print("El producto ya se encuentra en el kiosco")
            else:
                productos.append(producto_agregado.lower())
                precio_agregado = input("Ingresa el precio del rpoducto a agregtar: ")
                precio_agregado = precio_agregado.replace(" ", "")
                if int(precio_agregado) <= 0:
                    print("El precio del producto debe ser mayor a 0")
                elif precio_agregado == "":
                    print("Lo ingresado no puede estar vacío")
                elif not precio_agregado.isdigit():
                    print("Debes ingrear un número entero positivo")
                else:
                    precios.append(int(precio_agregado))
                    cantidades.append(0)
                    print("PRODUCTO AÑADIDO CON ÉXITO")
                    print("=" * 30)
        case "7":
            buscado = input("Ingrese el nombre del producto para sumar unidades vendidas: ")
            buscado = buscado.replace(" ", "").lower()
            while not buscado.isalpha() or buscado == "":
                print("Error, el producto a buscar no puede contener números ni estar vacío")
                buscado = input("Ingrese el nombre del producto para sumar unidades vendidas: ")
                buscado = buscado.replace(" ", "").lower()
            if buscado in productos:
                i = productos.index(buscado)
                cantidad_sumada = input(f"Ingresa la cantidad de unidades de {buscado} que se vendieron ahora: ")
                cantidad_sumada = cantidad_sumada.replace(" ", "")
                while not cantidad_sumada.isdigit() or cantidad_sumada == "":
                    print("Error, la cantida a sumar debe ser un número entero positivo")
                    cantidad_sumada = input(f"Ingresa la cantidad de unidades de {buscado} que se vendieron ahora: ")
                    cantidad_sumada = cantidad_sumada.replace(" ", "")
                cantidad_sumada = int(cantidad_sumada)
                cantidades[i] += cantidad_sumada
                print("CANTIDAD SUMADA CON ÉXITO")
                print("=" * 30)
            else:
                print("El producto buscado no se encuentra en el kiosco")
                print("=" * 30)
        case "8":
            recaudacion_total = 0
            for i in range(len(productos)):
                recaudacion_total += (cantidades[i] * precios[i])
            mas_vendido = cantidades.index(max(cantidades))
            print(f"Reacaudación dle día: ${recaudacion_total}")
            print(f"El produto más vendido del día fue: {productos[mas_vendido]}")
            for i in range(len(cantidades)):
                cantidades[i] = 0
        case "9":
            print("Has seleccionado salir")
            break
        case _:
            print("Error, debes seleccionar un número entre 1 y 9")