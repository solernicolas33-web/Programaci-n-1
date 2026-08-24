### EJERCICIO 1 ###
"""
nombre = input("Ingrese el nombre del cliente: ")
nombre = nombre.replace(" ", "")
while not nombre.isalpha() or nombre == "":
    print("El nombre no puede contener números ni estar vacío")
    nombre = input("Ingrese el nombre del cliente: ")
    nombre = nombre.replace(" ", "")

cantidad = input("Ingrese la cantidad de productos a vender: ")
while not cantidad.isdigit() or cantidad == "0":
    print("La cantidad ingresada debe ser un número entero mayor a 0")
    cantidad = input("Ingrese la cantidad de productos a vender: ")

cantidad = int(cantidad)

productos = []
total_sin_descuentos = 0
total_con_descuentos = 0

for i in range(cantidad):
    producto = []
    print(f"Producto {i+1}:")
    precio = input(f"Ingrese el precio del producto {i+1}: ")
    while not precio.isdigit() or precio == "0":
        print("El precio debe ser un número entero mayor que 0")
        precio = input(f"Ingrese el precio del producto {i+1}: ")

    precio = int(precio)

    descuento = input(f"¿El producto {i+1} tiene descuento?(S/N): ")
    descuento = descuento.replace(" ", "").upper()
    while not descuento in "SN" or descuento == "":
        print("Ingrese S o N si el producto tiene o no descuento")
        descuento = input(f"¿El producto {i+1} tiene descuento?(S/N): ")
        descuento = descuento.replace(" ", "").upper()

    producto.append(i+1)
    producto.append(precio)
    producto.append(descuento)
    productos.append(producto)

    total_sin_descuentos += precio
    if descuento == "S":
        total_con_descuentos += precio * .9
    else:
        total_con_descuentos += precio

ahorro = total_sin_descuentos - total_con_descuentos
promedio = total_sin_descuentos / cantidad

print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cantidad}")
for i in range(cantidad):
    print(f"Producto {i+1} | Precio = {productos[i][1]} | Descuanto(s/n): {productos[i][2]}")
print(f"Total sin descuentos: {total_sin_descuentos}")
print(f"Total con descuento: {total_con_descuentos}")
print(f"Ahorro total: {ahorro}")
print(f"Pormedio por producto: {promedio:.2f}")"""


### EJERCICIO 2 ###
"""
usuario_correcto = "alumno"
clave_correcta = "python123"
acceso = False

contador = 0
while contador < 3:
    print(f"Intento {contador+1}")
    ingreso_u = input("Ingrese el nombre de usuario: ")
    if ingreso_u == usuario_correcto:
        ingreso_clave = input("Ingrese la clave: ")
        if ingreso_clave == clave_correcta:
            print("Aceso permitido")
            contador = 3
            acceso = True
        else:
            print("Contraseña incorrecta")
    else:
        print("Nombre de usuario incorrecto")
    contador += 1

if acceso == False:
    print("Cuenta bloqueada")

if acceso == True:
    while True:
        opcion = input("Selecciona una opcón del menú:\n1. Ver estado de inscripción\n2. Cambiar clave\n3. Ver mensaje motivacional\n4. Salir\nOpción seleccionada: ")
        match opcion:
            case "1":
                print("Estado de incripción: INSCRIPTO")
            case "2":
                nueva_clave = input("Ingrese la nueva clave: ")
                while len(nueva_clave) < 6:
                    print("La nueva clave debe tener mínimo 6 caracteres")
                    nueva_clave = input("Ingrese la nueva clave: ")
                confirmación_nueva_clave = input("Confirme la nueva clave: ")
                while confirmación_nueva_clave != nueva_clave:
                    print("La nueva clave y la confirmación no coinciden, intentalo de nuevo")
                    confirmación_nueva_clave = input("Confirme la nueva clave: ")
                clave_correcta = confirmación_nueva_clave
                print("Clave cambiada con éxito")
            case "3":
                print("¡Estás aprendiendo mucho, sigue así!")
            case "4":
                print("Has selccionad salir")
                break
            case _:
                if opcion.isdigit():
                    print("Opción fuera de rango")
                else:
                    print("Ingrese un número válido")"""

### EJERCICIO 3 ###
"""
nombre = input("Ingrese el nombre del operador: ")
nombre = nombre.replace(" ", "")
while not nombre.isalpha() or nombre == "":
    print("El nombre no puede contener números ni estar vacío")
    nombre = input("Ingrese el nombre del operador: ")
    nombre = nombre.replace(" ", "")

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""
while True:
    opcion = input("Selecciona una opción del menú:\n1. Reservar turno\n2. Cancelar turno(por nombre)\n3. Ver agenda del día\n4. Ver resumen general\n5. Cerrar sistema\nOpción seleccionada: ")
    match opcion:
        case "1":
            while True:
                dia = input("Selecciona un día para pedir el turno: 1. Lunes, 2. Martes.\nDía seleccionado: ")
                match dia:
                    case "1":
                        turno_nuevo = input("Ingrese el nombre del paciente que quiere agendar un turno el lunes: ")
                        turno_nuevo = turno_nuevo.replace(" ", "")
                        while not turno_nuevo.isalpha() or turno_nuevo == "":
                            turno_nuevo = input("Ingrese el nombre del paciente que quiere agendar un turno el lunes: ")
                            turno_nuevo = turno_nuevo.replace(" ", "")
                        if turno_nuevo != lunes1 and turno_nuevo != lunes2 and turno_nuevo != lunes3 and turno_nuevo != lunes4:
                            if lunes1 == "":
                                lunes1 = turno_nuevo
                                print("Turno agendado con éxito")
                            elif lunes2 == "":
                                lunes2 = turno_nuevo
                                print("Turno agendado con éxito")
                            elif lunes3 == "":
                                lunes3 = turno_nuevo
                                print("Turno agendado con éxito")
                            elif lunes4 == "":
                                lunes4 = turno_nuevo
                                print("Turno agendado con éxito")
                            else:
                                print("Todos los turnos del día lunes están agendados")
                        else:
                            print(f"El paciente {turno_nuevo} ya tiene un turno agendado el día lunes")
                        break
                    case "2":
                        turno_nuevo = input("Ingrese el nombre del paciente que quiere agendar un turno el lunes: ")
                        turno_nuevo = turno_nuevo.replace(" ", "")
                        while not turno_nuevo.isalpha() or turno_nuevo == "":
                            turno_nuevo = input("Ingrese el nombre del paciente que quiere agendar un turno el lunes: ")
                            turno_nuevo = turno_nuevo.replace(" ", "")
                        if turno_nuevo != martes1 and turno_nuevo != martes2 and turno_nuevo != martes3:
                            if martes1 == "":
                                martes1 = turno_nuevo
                                print("Turno agendado con éxito")
                            elif martes2 == "":
                                martes2 = turno_nuevo
                                print("Turno agendado con éxito")
                            elif martes3 == "":
                                martes3 = turno_nuevo
                                print("Turno agendado con éxito")
                            else:
                                print("Todos los turnos del día martes están agendados")
                        else:
                            print(f"El paciente {turno_nuevo} ya tiene un turno agendado el día martes")
                        break
                    case _:
                        print("Opción inválida, seleccioa 1. Lunes o 2. Martes")

        case "2":
            while True:
                dia = input("Selecciona el día del turno a cancelar: 1. Lunes, 2. Martes.\nDía seleccionado: ")
                match dia:
                    case "1":
                        turno_cancelado = input("Ingresa el nombre del paciente que quiere cancelar su turno: ")
                        turno_cancelado = turno_cancelado.replace(" ", "")
                        while not turno_cancelado.isalpha() or turno_cancelado == "":
                            turno_cancelado = input("Ingresa el nombre del paciente que quiere cancelar su turno: ")
                            turno_cancelado = turno_cancelado.replace(" ", "")
                        if turno_cancelado == lunes1:
                            lunes1 = ""
                        elif turno_cancelado == lunes2:
                            lunes2 = ""
                        elif turno_cancelado == lunes3:
                            lunes3 = ""
                        elif turno_cancelado == lunes4:
                            lunes4 = ""
                        else:
                            print(f"El paciente {turno_cancelado} no tiene un turno agendado el lunes")
                        break
                    case "2":
                        turno_cancelado = input("Ingresa el nombre del paciente que quiere cancelar su turno: ")
                        turno_cancelado = turno_cancelado.replace(" ", "")
                        while not turno_cancelado.isalpha() or turno_cancelado == "":
                            turno_cancelado = input("Ingresa el nombre del paciente que quiere cancelar su turno: ")
                            turno_cancelado = turno_cancelado.replace(" ", "")
                        if turno_cancelado == martes1:
                            martes1 = ""
                        elif turno_cancelado == martes2:
                            martes2 = ""
                        elif turno_cancelado == martes3:
                            martes3 = ""
                        else:
                            print(f"El paciente {turno_cancelado} no tiene un turno agendado el martes")
                        break
                    case _:
                        print("Opción inválida, seleccioa 1. Lunes o 2. Martes")

        case "3":
            while True:
                dia = input("Ver agenda de: 1. Lunes, 2. Martes.\nDía seleccionado: ")
                match dia:
                    case "1":
                        print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
                        print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
                        print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
                        print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
                        break
                    case "2":
                        print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
                        print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
                        print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")
                        break
                    case _:
                        print("Opción inválida, selecciona 1. Lunes o 2. Martes")

        case "4":
            turnos_lunes = 0
            turnos_martes = 0
            if lunes1 != "":
                print(f"Turno 1 lunes: {lunes1}")
                turnos_lunes += 1
            else:
                print("Turno 1 lunes: DISPONIBLE")
            if lunes2 != "":
                print(f"Turno 2 lunes: {lunes2}")
                turnos_lunes += 1
            else:
                print("Turno 2 lunes: DISPONIBLE")
            if lunes3 != "":
                print(f"Turno 3 lunes: {lunes3}")
                turnos_lunes += 1
            else:
                print("Turno 3 lunes: DISPONIBLE")
            if lunes4 != "":
                print(f"Turno 4 lunes: {lunes4}")
                turnos_lunes += 1
            else:
                print("Turno 4 lunes: DISPONIBLE")

            if martes1 != "":
                print(f"Turno 1 martes: {martes1}")
                turnos_martes += 1
            else:
                print("Turno 1 martes: DISPONIBLE")
            if martes2 != "":
                print(f"Turno 2 martes: {martes2}")
                turnos_martes += 1
            else:
                print("Turno 2 martes: DISPONIBLE")
            if martes3 != "":
                print(f"Turno 3 martes: {martes3}")
                turnos_martes += 1
            else:
                print("Turno 3 martes: DISPONIBLE")

            if turnos_lunes > turnos_martes:
                print("El día lunes hay más turnos ocupados")
            elif turnos_martes > turnos_lunes:
                print("El día martes hay más turnos ocupados")
            else:
                print("Los dos días tienen la misma cantidad de turnos ocupados")

        case "5":
            print("Has seleccionad cerrar el sistema")
            break
        case _:
            print("Opción fuera de rango, selecciona una opción entre 1 y 5")"""

### EJERCICIO 4 ###
"""
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

agente = input("Ingrese el nombre del agente: ")
agente = agente.replace(" ", "")
while not agente.isalpha() or agente == "":
    print("El nombre dle agente no puede contener números ni estar vacío")
    agente = input("Ingrese el nombre del agente: ")
    agente = agente.replace(" ", "")

forzar_seguidas = 0

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    if alarma and tiempo <= 3:
        break
    print(f"Estado actual: Energía: {energia}, Tiempo: {tiempo}, Cerrdauras forzadas: {cerraduras_abiertas}, Alarma_ {'ACTIVADA' if alarma else 'DESAVTIVADA'}")
    print(f"Código parcial: {codigo_parcial}, Longitud: {len(codigo_parcial)}")

    opcion = input("Selecciona una opción del menú:\n1. Forzar cerradura (-20 energía, -2 tiempo)\n2. Hackear panel (-10 energía, -3 tiempo)\n3. Descansar (+15 energía, -1 tiempo)\nOpción sleccionada: ")
    match opcion:
        case "1":
            forzar_seguidas += 1
            energia -= 20
            tiempo -= 2
            if forzar_seguidas >= 3:
                print("Regla anti-spam, la cerradura se trabó por forzar 3 veces seguidas")
                print("La alarma se activó y no se abrió la cerradura")
                alarma = True
            else:
                if energia < 40:
                    print("Riesgo de alarma por energía baja")
                    numero = input("Ingresa un número entre 1 y 3: ")
                    while not numero.isdigit() and numero in "123":
                        print("Opción inválida, selecciiona un número entre 1 y 3")
                        numero = input("Ingresa un número entre 1 y 3: ")
                    if numero == "3":
                        print("La alarma se activó")
                        alarma = True
                if not alarma:
                    cerraduras_abiertas += 1
                    print(f"Swe frozó la cerradura con éxito, llevas {cerraduras_abiertas}/3 cerraduras abiertas")
                else:
                    print("La alarma está activada, nop se pudo forzar la cerradura")
        case "2":
            forzar_seguidas = 0
            energia -= 10
            tiempo -= 3

            print("Hackeando panel de seguridad")
            for i in range(4):
                print(f"Paso {i+1}/4 commpeto, letra añadida con éxito")
                codigo_parcial += "A"

            if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                print("Código completado, se abrió una cerradura")
                cerraduras_abiertas += 1
        case "3":
            forzar_seguidas = 0
            tiempo -= 1

            if not alarma:
                energia += 15
                print("Descansaste ocn éxito")
            else:
                energia += 5
                print("No pudiste descansar bien por la alarma")
            if energia > 100:
                energia = 100

            print(f"Energía actual: {energia}")
        case _:
            print("Opción inválida, selecciona una opción entre 1 y 3")

if cerraduras_abiertas >= 3:
    print("Victoria, lograste forzar todas las cerraduras y salir con éxito")
elif alarma and tiempo <= 3:
    print(f"Derrota, el sistema se bloqueó por falta de tiempo y la alarma activa")
elif energia <= 0:
    print(f"Derrota, tu energía llegó a 0 y te quedaste encerrado")
elif tiempo <= 0:
    print(f"Derrota, te quedaste sin tiempo")"""

### EJERCICIO 5 ###
"""
print("--- Bienvenido a la arena ---")
nombre = input("Ingrese el nombre del gladiador: ")
nombre = nombre.replace(" ", "")
while not nombre.isalpha() or nombre == "":
    print("ERROR: solo se permiten letras")
    nombre = input("Ingrese el nombre del gladiador: ")
    nombre = nombre.replace(" ", "")

print("=== Inicio del combate ===")
vida_gladiador = 100
vida_enemigo = 100
pociones = 3
daño_base = 15
daño_enemigo = 12
turno_gladiador = True

while vida_gladiador > 0 and vida_enemigo > 0:
    while turno_gladiador:
        print("TURNO DLE JUGADOR")
        print(f"Vida actual: {vida_gladiador}")
        print(f"Vida actual del enemigo: {vida_enemigo}")
        print(f"Pociones disponibles: {pociones}")
        opcion = input("Selecciona una opción:\n1. Ataque pesado\n2. Ráfaga veloz\n3. Curar\nOpción seleccionada: ")
        while not opcion.isdigit() or opcion not in ["1", "2", "3"]:
            print("ERROR, la opción elegida debe ser unn número entre 1 y 3")
            opcion = input("Selecciona una opción:\n1. Ataque pesado\n2. Ráfaga veloz\n3. Curar\nOpción seleccionada: ")

        if opcion == "1":
            daño_total = daño_base
            if vida_enemigo < 20:
                daño_total = daño_total * 1.5
                vida_enemigo -= daño_total
            else:
                vida_enemigo -= daño_total
            print(f"Atacaste al enemigo por {daño_total} puntos de daño")

        if opcion == "2":
            for i in range(3):
                vida_enemigo -= 5
                print("Golpe conectado por 5 de daño")

        if opcion == "3":
            if pociones > 0:
                vida_gladiador += 30
                pociones -= 1
                print("Usaste una pocíon y recuperaste 30HP")
            else:
                print("No te quedan pociones, perdiste eñ turno")

        turno_gladiador = False

    while not turno_gladiador:
        print("TURNO DEL ENEMIGO")
        vida_gladiador -= daño_enemigo
        print(f"El enemigo te atacó por {daño_enemigo} puntos de vida")
        turno_gladiador = True

if vida_gladiador > 0 and vida_enemigo <= 0:
    print(f"Felicidades gladiador {nombre}, has derrotado al enemigo")
elif vida_enemigo > 0 and vida_gladiador <= 0:
    print(f"El gladiador {nombre} a muerto por la espada del enemigo")"""