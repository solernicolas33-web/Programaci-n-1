print("Bienvenido al horno industrial, donde validamos que las temperaturas ingresadas sean válidas")

while True:
    opcion = input("¿Quiere ingresar una nueva temperatura o parar? (Colocar exactamente 'FIN' para parar): ")
    match opcion:
        case "FIN":
            print("Gracias por usar el horno industrial")
            break
        case _:
            temperatura = input("Ingrese la temperatura a validar(entre 100 y 500): ")
            puntos = 0
            for i in range(len(temperatura)):
                if temperatura[i] == ".":
                    puntos += 1
            temperatura_entero = temperatura.replace(" ","").replace(".", "")
            while not temperatura_entero.isdigit() or temperatura_entero == "" or puntos > 1:
                print("Ingresaste una temperatura inválida, debe ser un número entero o uno flotante con 1 solo punto")
                temperatura = input("Ingrese la temperatura a validar(entre 100 y 500): ")
                puntos = 0
                for i in range(len(temperatura)):
                    if temperatura[i] == ".":
                        puntos += 1
                temperatura_entero = temperatura.replace(" ","").replace(".", "")
            temperatura = float(temperatura)
            if 100 < temperatura < 500:
                print("Temperatura registrada con éxito, se encuentra dentro de rango")
            else:
                print("¡ADVERTENCIA! Temperatura fuera de rango")