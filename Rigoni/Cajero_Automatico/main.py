saldo = 50000
print("Bienvenido al cajero automático")

while True:
    opcion = input("Que acción quiere realizar:\n1. Consultar saldo\n2. Ingresar dinero\n3. Retirar dinero\n4. Salir\nOpción seleccionada: ")
    match opcion:
        case "1":
            print(f"El saldo actual es de: ${saldo}")
        case "2":
            ingreso = input("Ingrese la cantidad que quiere depositar en la cuenta: ")
            ingreso = ingreso.replace(" ", "")
            while not ingreso.isdigit() or ingreso == "":
                print("Debes ingresar un número entero mayor o igual que 0")
                ingreso = input("Ingrese la cantidad que quiere depositar en la cuenta: ")
                ingreso = ingreso.replace(" ", "")
            ingreso = int(ingreso)
            saldo += ingreso
        case "3":
            retiro = input("Ingrese la cantidad que quiere retirar: ")
            retiro = retiro.replace(" ", "")
            while not retiro.isdigit() or retiro == "":
                print("Debes ingresar un número entero mayor o igual que 0")
                retiro = input("Ingrese la cantidad que quiere retirar: ")
                retiro = retiro.replace(" ", "")
            retiro = int(retiro)
            if retiro <= saldo:
                saldo -= retiro
            else:
                print("El saldo actual es insuficiente")
        case "4":
            print("Gracias por usar el cajero")
            break
        case _:
            print("Opción inválida, selecciona un número entre 1 y 4")
