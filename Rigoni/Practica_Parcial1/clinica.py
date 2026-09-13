especialidades = []
cupos = []

while True:
    opcion = input("Selecciona que acción quieres realizar:\n1. Ingresar lista de especialidades\n2. Ingresar lista de cupos disponibles por especialidad\n3. Mostrar agenda\n4. Consultar cupos de una especialidad\n5. Listar especialidades sin cupo\n6. Agregar especialidad\n7. Actualizar cupos (reservar / cancelar)\n8. Salir\nOpción seleccionada: ")

    match opcion:
        case "1":
            if len(especialidades) == 0:
                e_ingresada = input("Ingresa la especialidad que quieres agregar a la lista de especialidades: ").replace(" ", "").lower()
                while not e_ingresada.isalpha() or e_ingresada == "":
                    print("Error, lo ingresado no puede estar vacío ni contener números")
                    e_ingresada = input("Ingresa la especialidad que quieres agregar a la lista de especialidades: ").replace(" ", "").lower()
                especialidades.append(e_ingresada)
                print("Especialidad ingresadas con éxito")
                while True:
                    continuar_ingresando = input("Quieres continuar ingresando especialidades a la lista:\n1. SI\n2. NO\nOpción seleccionada: ")
                    match continuar_ingresando:
                        case "1":
                            e_ingresada = input("Ingresa la especialidad que quieres agregar a la lista de especialidades: ").replace(" ", "").lower()
                            while not e_ingresada.isalpha() or e_ingresada == "":
                                print("Error, lo ingresado no puede estar vacío ni contener números")
                                e_ingresada = input("Ingresa la especialidad que quieres agregar a la lista de especialidades: ").replace(" ", "").lower()
                            especialidades.append(e_ingresada)
                            print("Especialidad ingresada con éxito")
                        case "2":
                            print("Has seleccionado volver al menú principal")
                            break
                        case _:
                            print("Debes seleccionar una opción entre 1 o 2")
            else:
                print("Esta es una opcón inicial, solo la puedes realizar 1 vez, para ingresar más especialidades selecciona la opción 6")
        case "2":
            if len(especialidades) > 0:
                if len(cupos) == 0:
                    for i in range(len(especialidades)):
                        cupo_ingresado = input(f"Ingresa la cantidad de cupos disponibles para {especialidades[i]}: ").replace(" ", "")
                        while not cupo_ingresado.isdigit() or cupo_ingresado == "":
                            print("Error, debes ingresar unn número entero para la cantidad de cupos")
                            cupo_ingresado = input(f"Ingresa la cantidad de cupos disponibles para {especialidades[i]}: ").replace(" ", "")
                        cupo_ingresado = int(cupo_ingresado)
                        cupos.append(cupo_ingresado)
                        print("Cantidad de cupos agregada con éxito")
                    lista_comprobar = cupos.copy()
                else:
                    print("Esta es una opción inicial y solo se puede realizar 1 vez. Para Ingresar los cupos de una nueva especialidad selecciona la opción 6, y para actualiar los cupos de una especialidad ya existente selecciona la opción 7")
            else:
                print("Todavía no has ingresado ninguna especialidad.")
        case "3":
            if len(especialidades) > 0:
                if len(cupos) > 0:
                    print("*" * 10,"Agenda","*" * 10)
                    for i in range(len(especialidades)):
                        print(f"Especialidad: {especialidades[i]}, Cantidad de cupos: {cupos[i]}")
                else:
                    print("Todavía no has ingresado la cantidad de cupos de las especialidades")
            else:
                print("Todavía no has ingresado ninguna especialidad")
        case "4":
            if len(especialidades) > 0:
                if len(cupos) > 0:
                    e_buscada = input("Ingrese la especialidad de la cual quiere saber la cantidad de cupos: ").lower()
                    while not e_buscada.isalpha() or e_buscada == "":
                        print("Error, la especialidad ingresada no puede tener números ni estar vacía")
                        e_buscada = input("Ingrese la especialidad de la cual quiere saber la cantidad de cupos: ").lower()
                    if e_buscada in especialidades:
                        indice = especialidades.index(e_buscada)
                        print(f"La cantidad de cupos de {e_buscada} son: {cupos[indice]}")
                    else:
                        print("La especialidad ha sido mal ingresada o no se encuentra en la lista de especialidades")
                else:
                    print("Todavía no has ingresado los cupos de las especialidades")
            else:
                print("Todavia no has ingresado las especialidades de la clinica")
        case "5":
            print("*" * 10,"Especialidades con 0 cupos disponibles", "*" * 10)
            if len(especialidades) > 0:
                if len(cupos) > 0:
                    for i in range(len(cupos)):
                        if cupos[i] == 0:
                            if i + 1 == len(cupos):
                                print(f"{especialidades[i]}")
                            else:
                                print(f"{especialidades[i]}", end = ", ")
                else:
                    print("Todavía no has ingresado los cupos de las especialidades")
            else:
                print("Todavia no has ingresado las especialidades de la clinica")
        case "6":
            if len(especialidades) > 0:
                if len(cupos) > 0:
                    e_ingresada = input("Ingresa la especialidad que quieres agregar a la lista de especialidades: ").replace(" ", "").lower()
                    while not e_ingresada.isalpha() or e_ingresada == "":
                        print("Error, lo ingresado no puede estar vacío ni contener números")
                        e_ingresada = input("Ingresa la especialidad que quieres agregar a la lista de especialidades: ").replace(" ", "").lower()
                    especialidades.append(e_ingresada)
                    print("Especialidad ingresadas con éxito")
                    cupo_ingresado = input(f"Ingresa la cantidad de cupos disponibles para {e_ingresada}: ").replace(" ", "")
                    while not cupo_ingresado.isdigit() or cupo_ingresado == "":
                        print("Error, debes ingresar unn número entero para la cantidad de cupos")
                        cupo_ingresado = input(f"Ingresa la cantidad de cupos disponibles para {e_ingresada}: ").replace(" ", "")
                    cupo_ingresado = int(cupo_ingresado)
                    cupos.append(cupo_ingresado)
                    lista_comprobar.append(cupo_ingresado)
                    print("Cantidad de cupos agregada con éxito")
                else:
                    print("Todavía no cargaste los cupos de las especialidades iniciales")
            else:
                print("Todavía no has hecho la carga inicial de especialidades")
        case "7":
            if len(especialidades) > 0:
                if len(cupos) > 0:
                    e_actualizar = input("Ingrese la especialidad que quieres reservar o cancelar un turno: ").lower()
                    while not e_actualizar.isalpha() or e_actualizar == "":
                        print("Error, la especialidad ingresada no puede tener números ni estar vacía")
                        e_actualizar = input("Ingrese la especialidad que quieres reservar o cancelar un turno: ").lower()
                    if e_actualizar in especialidades:
                        indice = especialidades.index(e_actualizar)
                        while True:
                            opcion = input(f"Ingresa que quieres hacer con {especialidades[indice]}:\n1. Reservar turno\n2. Cancelar truno\nOpción seleccionada: ")
                            match opcion:
                                case "1":
                                    if cupos[indice] == 0:
                                        print("No se puede reservar un turno ya que no hay ninguno disponible")
                                        break
                                    else:
                                        cupos[indice] -= 1
                                        print("Turno agendado con éxito")
                                        break
                                case "2":
                                    if cupos[indice] == lista_comprobar[indice]:
                                        print("No hay turnos reservados para esta especialidad")
                                        break
                                    else:
                                        cupos[indice] += 1
                                        print("Turno cancelado con éxito")
                                        break
                                case _:
                                    print("Error, debes seleccionar una opción entre 1 o 2")
                    else:
                        print("La especialidad está mal ingresada o no se encuentra en la lista de especialidades")
                else:
                    print("Todavía no has ingresado los cupos de las especialidades iniciales")
            else:
                print("Todavía no has hecho la carga inicial de especialidades")
        case "8":
            print("Has seleccionado salir")
            break
        case _:
            print("Error, opción inválida, selecciona un npumero entre 1 y 8")