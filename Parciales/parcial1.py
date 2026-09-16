herramientas = []
c_stock = []

while True:
    menu = input("Selecciones la opción a realizar:\n1. Carga inicial de herraminetas\n2. Carga de existencias\n3. Visualización de inventario\n4. Consulta de stock\n5. Reporte de agotados\n6. Alta de nuevo producto\n7. Actualización de stock(venta o ingreso)\n8. Salir\nOpción seleccionada: ")
    match menu:
        case "1":
            if len(herramientas) == 0:
                cantidad_ingresdos = input("Ingrese la cantidad de herramientas que desea cargar: ")
                cantidad_ingresdos = cantidad_ingresdos.replace(" ", "")
                while not cantidad_ingresdos.isdigit() or int(cantidad_ingresdos) <= 0:
                    print("Error, debes ingresar un número entero mayor que 0 para la cantidad")
                    cantidad_ingresdos = input("Ingrese la cantidad de herramientas que desea cargar: ")
                    cantidad_ingresdos = cantidad_ingresdos.replace(" ", "")
                cantidad_ingresdos = int(cantidad_ingresdos)
                for i in range(cantidad_ingresdos):
                    h_ingrersada = input(f"Ingresa el nombre de la herramineta {i+1}: ")
                    h_ingrersada = h_ingrersada.strip().capitalize()
                    while not h_ingrersada.isalpha() or h_ingrersada == "":
                        print("Error, el nombre de la herramineta no puede estar vacío ni contener números")
                        h_ingrersada = input(f"Ingresa el nombre de la herramineta {i+1}: ")
                        h_ingrersada = h_ingrersada.strip().capitalize()
                    herramientas.append(h_ingrersada)
                print("Carga realizada con éxito")
                print("=" * 30)
            else:
                print("La opción 1 solo es una opción inicial y ya ha sido realizada")
                print("=" * 30)
        case "2":
            if len(herramientas) == 0:
                print("Error, debes realizar la opción 1 antes de poder hacer esta opción")
                print("=" * 30)
            elif len(c_stock) == 0:
                for i in range(len(herramientas)):
                    cantidad = input(f"Ingrese la cantidad en stock de {herramientas[i]}: ")
                    cantidad = cantidad.replace(" ", "")
                    while not cantidad.isdigit() or int(cantidad) <= 0:
                        print("Error, debes ingresar un número entero mayor que 0 para la cantidad")
                        cantidad = input(f"Ingrese la cantidad en stock de {herramientas[i]}: ")
                        cantidad = cantidad.replace(" ", "")
                    cantidad = int(cantidad)
                    c_stock.append(cantidad)
                print("Cantidades añadidas con éxito")
                print("=" * 30)
            else:
                print("Error, esta opción solo se puede realizar 1 vez, y ya ha sido realizada")
                print("=" * 30)
        case "3":
            if len(herramientas) == 0:
                print("Error, todavía no ha realizado la carga inicial de herraminetas")
                print("=" * 30)
            else:
                if len(c_stock) == 0:
                    print("Todavía no has hecho la carga de cantidades iniciales")
                    print("=" * 30)
                else:
                    print("INVENTARIO COMPLETO:")
                    for i in range(len(herramientas)):
                        print(f"Heeramienta: {herramientas[i]} | Cantidad en stock: {c_stock[i]}")
                    print("=" * 30)
        case "4":
            if len(herramientas) == 0:
                print("Error, todavía no ha realizado la carga inicial de herraminetas")
                print("=" * 30)
            else:
                if len(c_stock) == 0:
                    print("Todavía no has hecho la carga de cantidades iniciales")
                    print("=" * 30)
                else:
                    buscado = input("Ingresa el nobre de la herramienta a buscar: ")
                    buscado = buscado.strip().capitalize()
                    while not buscado.isalpha() or buscado == "":
                        print("Error, el nombre no puede contener números ni estar vacío")
                        buscado = input("Ingresa el nobre de la herramienta a buscar: ")
                        buscado = buscado.strip().capitalize()
                    if buscado in herramientas:
                        indice = herramientas.index(buscado)
                        print(f"La heeramineta si se encuentra en la ferretería. Unidades disponibles: {c_stock[indice]}")
                        print("=" * 30)
                    else:
                        print(f"La herramienta {buscado} no se encuentra en la ferretería")
                        print("=" * 30)
        case "5":
            if len(herramientas) == 0:
                print("Error, todavía no ha realizado la carga inicial de herraminetas")
                print("=" * 30)
            else:
                if len(c_stock) == 0:
                    print("Todavía no has hecho la carga de cantidades iniciales")
                    print("=" * 30)
                else:
                    if 0 in c_stock:
                        print("Listado de herramientas agotadas:")
                        print("|", end = " ")
                        for i in range(len(herramientas)):
                            if c_stock[i] == 0:
                                print(herramientas[i], end = " | ")
                        print("")
                        print("=" * 30)
                    else:
                        print("No hay ninguna herramienta agotada")
                        print("=" * 30)
        case "6":
            if len(herramientas) == 0:
                print("Error, todavía no ha realizado la carga inicial de herraminetas")
                print("=" * 30)
            else:
                if len(c_stock) == 0:
                    print("Todavía no has hecho la carga de cantidades iniciales")
                    print("=" * 30)
                else:
                    agregado = input("Ingrese el nombre de la herramineta a agregar: ")
                    agregado = agregado.strip().capitalize()
                    while not agregado.isalpha() or agregado == "":
                        print("Error, el nombre de la herramienta a agregar no puede estar vacío ni contener números")
                        agregado = input("Ingrese el nombre de la herramineta a agregar: ")
                        agregado = agregado.strip().capitalize()
                    if agregado in herramientas:
                        print("La herramineta ya se encuentra cargada en la ferretería")
                        print("=" * 30)
                    else:
                        c_agregado = input(f"Ingrese la cantidad inicial de la herramienta {agregado}: ")
                        c_agregado.replace(" ", "")
                        while not c_agregado.isdigit() or int(c_agregado) <= 0:
                            print("Error, la cantidad debe ser un número entero mayor que 0")
                            c_agregado = input(f"Ingrese la cantidad inicial de la herramienta {agregado}: ")
                            c_agregado.replace(" ", "")
                        c_agregado = int(c_agregado)
                        herramientas.append(agregado)
                        c_stock.append(c_agregado)
                        print("Alta de la herramineta realizado con éxito")
                        print("=" * 30)
        case "7":
            if len(herramientas) == 0:
                print("Error, todavía no ha realizado la carga inicial de herraminetas")
                print("=" * 30)
            else:
                if len(c_stock) == 0:
                    print("Todavía no has hecho la carga de cantidades iniciales")
                    print("=" * 30)
                else:
                    buscado = input("Ingresa el nobre de la herramienta a buscar: ")
                    buscado = buscado.strip().capitalize()
                    while not buscado.isalpha() or buscado == "":
                        print("Error, el nombre no puede contener números ni estar vacío")
                        buscado = input("Ingresa el nobre de la herramienta a buscar: ")
                        buscado = buscado.strip().capitalize()
                    if buscado in herramientas:
                        indice = herramientas.index(buscado)
                        while True:
                            v_o_i = input(f"¿Qué acción quiere realizar con la herramineta {buscado}?:\n1. Vender\n2. Reponer\nOpción seleccionada: ")
                            match v_o_i:
                                case "1":
                                    cantidad_vendidas = input("Ingrese la cantidad de unidades que quieres vender: ")
                                    cantidad_vendidas = cantidad_vendidas.replace(" ", "")
                                    while not cantidad_vendidas.isdigit() or int(cantidad_vendidas) <= 0:
                                        print("Error, la cantidad debe ser un número entero mayor que 0")
                                        cantidad_vendidas = input("Ingrese la cantidad de unidades que quieres vender: ")
                                        cantidad_vendidas = cantidad_vendidas.replace(" ", "")
                                    cantidad_vendidas = int(cantidad_vendidas)
                                    if c_stock[indice] >= cantidad_vendidas:
                                        c_stock[indice] -= cantidad_vendidas
                                        print(f"Se vendiron correctamente {cantidad_vendidas} unidades de {buscado}")
                                        print("=" * 30)
                                    else:
                                        print(f"No hay stock suficiente de la herramineta {buscado}")
                                        print("=" * 30)
                                    break
                                case "2":
                                    cantidad_ingreso = input(f"Ingrese la cantidad de unidades de {buscado} que quieres ingresar: ")
                                    cantidad_ingreso = cantidad_ingreso.replace(" ", "")
                                    while not cantidad_ingreso.isdigit() or int(cantidad_ingreso) <= 0:
                                        print("Error, la cantidad debe ser un número entero mayor que 0")
                                        cantidad_ingreso = input(f"Ingrese la cantidad de unidades de {buscado} que quieres ingresar: ")
                                        cantidad_ingreso = cantidad_ingreso.replace(" ", "")
                                    cantidad_ingreso = int(cantidad_ingreso)
                                    c_stock[indice] += cantidad_ingreso
                                    print(f"Ingreso de {cantidad_ingreso} unidades de {buscado} realizado con éxito")
                                    print("=" * 30)
                                    break
                                case _:
                                    print("Error, solo puedes seleccionar 1 para vender o 2 para reponer")
                    else:
                        print("La herramienta no se encuentra en la ferretería")
                        print("=" * 30)
        case "8":
            print("Has seleccionado salir, gracias por usar el sistema de control de inventario")
            break
        case _:
            print("Error, debes seleccionar una opción entre 1 y 8")
            print("=" * 30)