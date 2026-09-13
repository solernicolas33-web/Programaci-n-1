print("Bienvenido al Sistema de Gestión de Biblioteca")
print("*" * 30)
libros = []
copias = []
prestamos = []

while True:
    menu = input("Seleccione la acción que quiere realizar:\n1. Carga inicial de libros\n2. Mostrar inventario completo\n3. Consultar estado de un libro\n4. Registrar préstamo\n5. Registrar devolución\n6. Reportar libros agotados\n7. Agregar nuevo libro\n8. Mostrar estadisticas generales y finalizar jornada\n9. Salir\nOpción seleccionada: ")
    match menu:
        case "1":
            if len(libros) == 0:
                cantidad = input("Ingresa la cantidad de libros a cargar: ")
                cantidad = cantidad.replace(" ", "")
                while not cantidad.isdigit() or int(cantidad) <= 0:
                    print("Error, la cantidad debe ser un número entero mayor que 0")
                    cantidad = input("Ingresa la cantidad de libros a cargar: ")
                    cantidad = cantidad.replace(" ", "")
                cantidad = int(cantidad)
                for i in range(cantidad):
                    titulo = input(f"Ingresa el nombre del libro {i+1}: ")
                    titulo = titulo.replace(" ", "").lower()
                    while titulo == "":
                        print("Error, el titulo del nombre no puede estar vacío")
                        titulo = input(f"Ingresa el nombre del libro {i+1}: ")
                        titulo = titulo.replace(" ", "").lower()
                    libros.append(titulo)
                    copias_disponibles = input(f"Ingresa la cantidad de copias disponibles del libro '{titulo}': ")
                    copias_disponibles = copias_disponibles.replace(" ", "")
                    while not copias_disponibles.isdigit() or int(copias_disponibles) <= 0:
                        print("Error, la cantidad debe ser un número entero mayor que 0")
                        copias_disponibles = input(f"Ingresa la cantidad de copias disponibles del libro '{titulo}': ")
                        copias_disponibles = copias_disponibles.replace(" ", "")
                    copias_disponibles = int(copias_disponibles)
                    copias.append(copias_disponibles)
                    prestamos.append(0)
                    print("Libro cargado con Éxito")
                    print("*" * 30)
                print("=" * 30)
            else:
                print("Esta opción solo es una opción inicial y ya fue realizada")
                print("=" * 30)
        case "2":
            if len(libros) == 0:
                print("Error, todavía no hay libros cargados, realice la opción 1")
                print("=" * 30)
            else:
                print("Catálogo completo:")
                for i in range(len(libros)):
                    print(f"{libros[i]} | Copias disponibles: {copias[i]} | Veces prestado: {prestamos[i]}")
                    print("--" * 15)
                print("=" * 30)
        case "3":
            if len(libros) == 0:
                print("Error, todavía no hay libros cargados, realice la opción 1")
                print("=" * 30)
            else:
                buscado = input("Ingrese el libro del cual quiere ver los datos: ")
                buscado = buscado.replace(" ", "").lower()
                while buscado == "":
                    print("Error, no ingresaste el nombre de un libro")
                    buscado = input("Ingrese el libro del cual quiere ver los datos: ")
                    buscado = buscado.replace(" ", "").lower()
                if buscado in libros:
                    indice = libros.index(buscado)
                    print(f"Datos del libro {buscado}: Copias disponibles: {copias[indice]} | veces prestado: {prestamos[indice]}")
                    print("=" * 30)
                else:
                    print(f"El libro {buscado} no se encuentra en el stock de la biblioteca")
                    print("=" * 30)
        case "4":
            if len(libros) == 0:
                print("Error, todavía no hay libros cargados, realice la opción 1")
                print("=" * 30)
            else:
                buscado = input("Ingrese el libro que quiere pedir: ")
                buscado = buscado.replace(" ", "").lower()
                while buscado == "":
                    print("Error, no ingresaste el nombre de un libro")
                    buscado = input("Ingrese el libro que quiere prestar: ")
                    buscado = buscado.replace(" ", "").lower()
                if buscado in libros:
                    indice = libros.index(buscado)
                    if copias[indice] == 0:
                        print(f"No queda copias disponibles del libro {buscado}")
                        print("=" * 30)
                    else:
                        copias[indice] -= 1
                        prestamos[indice] += 1
                        print("Préstamo realizado con éxito")
                        print("=" * 30)
                else:
                    print(f"El libro {buscado} no se encuentra en el stock de la biblioteca")
                    print("=" * 30)
        case "5":
            if len(libros) == 0:
                print("Error, todavía no hay libros cargados, realice la opción 1")
                print("=" * 30)
            else:
                buscado = input("Ingrese el libro que quiere devolver: ")
                buscado = buscado.replace(" ", "").lower()
                while buscado == "":
                    print("Error, no ingresaste el nombre de un libro")
                    buscado = input("Ingrese el libro que quiere devolver: ")
                    buscado = buscado.replace(" ", "").lower()
                if buscado in libros:
                    indice = libros.index(buscado)
                    copias[indice] += 1
                    print("Libro devuelto con éxito")
                    print("=" * 30)
                else:
                    print(f"El libro {buscado} no se encuentra en el stock de la biblioteca")
                    print("=" * 30)
        case "6":
            cont_agotados = 0
            for i in range(len(libros)):
                if copias[i] == 0:
                    cont_agotados = 1
            if cont_agotados == 0:
                print("No hay ningún libro agotado")
                print("=" * 30)
            else:
                print("Listado de libros agotados:")
                print("|", end = " ")
                for i in range(len(libros)):
                    if copias[i] == 0:
                        print(f"{libros[i]}", end = " | ")
                print("")
                print("=" * 30)
        case "7":
            if len(libros) == 0:
                print("Error, todavía no ha realizado la carga inicial de libros, realice la opción 1")
                print("=" * 30)
            else:
                ingresado = input("Ingrese el titulo del libro que quiere añadir al stcok de la biblioteca: ")
                ingresado = ingresado.replace(" ", "").lower()
                while ingresado == "":
                    print("Error, no ingresaste nada")
                    ingresado = input("Ingrese el titulo del libro que quiere añadir al stcok de la biblioteca: ")
                    ingresado = ingresado.replace(" ", "").lower()
                if ingresado not in libros:
                    libros.append(ingresado)
                    cantidad_ingresado = input(f"Ingresa la cantidad de ejemplares del libro ingresaodo: ")
                    cantidad_ingresado = cantidad_ingresado.replace(" ", "")
                    while not cantidad_ingresado.isdigit() or cantidad_ingresado <= 0:
                        print("Error, la cantidad ingresada debe ser un número entero mayor que 0")
                        cantidad_ingresado = input(f"Ingresa la cantidad de ejemplares del libro ingresaodo: ")
                        cantidad_ingresado = cantidad_ingresado.replace(" ", "")
                    cantidad_ingresado = int(cantidad_ingresado)
                    copias.append(cantidad_ingresado)
                    prestamos.append(0)
                    print("Libro añadido con éxito")
                    print("=" * 30)
                else:
                    print("El libro ya se encuentra cargaod en la biblioteca")
                    print("=" * 30)
        case "8":
            totales = sum(copias)
            print(f"Cantidad de libros totales de la biblioteca: {totales}")
            indice = prestamos.index(max(prestamos))
            print(f"El libro más solicitado del día hasta ahora fue: {libros[indice]}")
            while True:
                continuar = input("¿Qué desea realizar?:\n1. Continuar con el día\n2. Finalizar día(reiniciar el contador de préstamos)\nOpción seleccionada: ")
                match continuar:
                    case "1":
                        print("Has seleccionado la opción '1. Continuar con el día'")
                        print("=" * 30)
                        break
                    case "2":
                        print("Has seleccionado la opción '2. Finalizar día'")
                        for i in range(len(prestamos)):
                            prestamos[i] = 0
                        print("Lista de préstamos diarios reiniciada con éxito")
                        print("=" * 30)
                        break
                    case _:
                        print("Error, debes seleccionar 1 o 2")
        case "9":
            print("Has seleccionado salir del programa")
            break
        case _:
            print("Error, debes seleccionar un número entre 1 y 9")