nombre_alumno = input("Ingresa el nombre del alumno que quiere ver/usar el sistema de notas: ")
lista_notas = []

while True:
    opcion = input("--- Sistema de notas ---\n1. Cargar una nota\n2. Ver todas las notas cargadas\n3. Calcular promedio y condición final\n4. Ver nota más alta y más baja del alumno\n5. Salir\nOpción elegida: ")
    match opcion:
        case "1":
            if len(lista_notas) >= 6:
                print("El máximo de notas que se pueden cargar ya ha sido alcanzado(6).")
            else:
                nota = float(input(f"Ingresa una de las notas del estudiante {nombre_alumno}: "))
                if 0 <= nota <= 10:
                    print(f"Nota agregada a la lista de notas exitosamente")
                    lista_notas.append(nota)
                else:
                    print(f"Nota fuera de rango, el valor debe estar entre 0 y 10")

        case "2":
            if len(lista_notas) == 0:
                print("Todavía no hay notas cargadas")
            else:
                print(f"Notas de {nombre_alumno}:")
                for i in range(len(lista_notas)):
                    print(f"Nota {i+1}: {lista_notas[i]}")

        case "3":
            if len(lista_notas) == 0:
                print("Todavía no hay notas cargadas")
            else:
                suma_notas = 0
                for i in range(len(lista_notas)):
                    suma_notas += lista_notas[i]
                promedio = suma_notas / len(lista_notas)
                match promedio:
                    case p if p < 4:
                        print(f"El promedio del estudiante {nombre_alumno} es: {promedio}. Condición final: LIBRE")
                    case p if 4 <= p < 7:
                        print(f"El promedio del estudiante {nombre_alumno} es: {promedio}. Condición final: REGULAR, deberá rendir fianl")
                    case p if 7 <= p <= 10:
                        print(f"El promedio del estudiante {nombre_alumno} es: {promedio}. Condición final: PROMOCIANADO")

        case "4":
            if len(lista_notas) == 0:
                print("No hay notas cargadas actualmente")
            else:
                nota_mas_baja = min(lista_notas)
                nota_mas_alta = max(lista_notas)
                print(f"La nota más alta del alumno {nombre_alumno} = {nota_mas_alta}")
                print(f"La nota más baja del alumno {nombre_alumno} = {nota_mas_baja}")

        case "5":
            print("Has seleccionado salir del sistema de notas")
            break


        case _:
            print("Opción inválida, selecciona una opción entre 1 y 4")