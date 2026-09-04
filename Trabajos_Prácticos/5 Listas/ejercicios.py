### Ejercicio 1 ###
"""
notas = [10,9,8,4.5,9.7,8.3,1,4.5,2.8,3.1]
suma = 0
for i in range(len(notas)):
    suma += notas[i]
promedio = suma / len(notas)
print("Notas de los alumnos:" , end=" ")
for i in range(len(notas)):
    if i == 9:
        print(notas[i])
    else:
        print(notas[i], end= ", ")
print(f"Promedio de todos los alumnos: {promedio:.2f}")
nota_alta = 0
nota_baja = notas[i]
for i in range (len(notas)):
    if notas[i] > nota_alta:
        nota_alta = notas[i]
    if notas[i] < nota_baja:
        nota_baja = notas[i]
print(f"La nota más alta es: {nota_alta}")
print(f"La nota más baja es: {nota_baja}")"""

### Ejercicio 2 ###
"""
print("Debes cargar 5 productos al carrito")
carrito = []
for i in range(1,6):
    producto = input(f"Ingresa el nombre del producto {i} para cargar al carrito: ")
    carrito.append(producto)
print(f"El carrito ordenado alfabéticamente queda así:", end = " ")
for i in range(len(carrito)):
    if i == len(carrito) - 1:
        print(sorted(carrito)[i])
    else:
        print(sorted(carrito)[i], end = ", ")
print("-" * 40)
print("Debes elimninar un rpoducto del carrito")
eliminado = input("Ingresa el producto que deseas eliminar: ")
if eliminado in carrito:
    carrito.remove(eliminado)
    print(f"El producto {eliminado} se quitó del carrito correctamente")
    print(f"La lista actualizada quedó así:", end = " ")
    for i in range(len(carrito)):
        if i == len(carrito) - 1:
            print(sorted(carrito)[i])
        else:
            print(sorted(carrito)[i], end = ", ")
else:
    print("El producto no se encuentra en el carrito")"""

### Ejercicio 3 ###
"""
import random
numeros = []
for i in range(15):
    añadido = random.randint(1,100)
    numeros.append(añadido)
pares = []
impares = []
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])
    else:
        impares.append(numeros[i])
print(f"La lista con los números pares tiene {len(pares)} números")
print(f"La lista de números ipares tiene {len(impares)} números")"""

### Ejercicio 4 ###
"""
datos = [1,3,5,3,7,1,9,5,3]
sin_repetidos = []
for i in range(len(datos)):
    if datos[i] not in sin_repetidos:
        sin_repetidos.append(datos[i])
print(f"La lista sin números repetidos es:", end = " ")
for i in range(len(sin_repetidos)):
    if i == len(sin_repetidos) - 1:
        print(sin_repetidos[i])
    else:
        print(sin_repetidos[i], end= ", ")"""

### Ejercicio 5 ###
"""
alumnos = ["Nico", "Bruno", "Ramiro", "Tomy", "Marcos", "Seba", "Gero", "Fabri"]
opcion = input("¿Qué quieres?:\n1. Añadir nuevo alumno\n2. Eliminar alumno existente\nOpción seleccionada: ")
match opcion:
    case "1":
        nuevo = input("Ingresa el nombre del alumno a añadir a la lista: ")
        alumnos.append(nuevo)
        print(f"Alumno añadido con éxito\nLista actualizada:", end= " ")
        for i in range(len(alumnos)):
            if i == len(alumnos) - 1:
                print(alumnos[i])
            else:
                print(alumnos[i], end = ", ")
    case "2":
        eliminado = input("Ingresa el producto que deseas eliminar: ")
        if eliminado in alumnos:
            alumnos.remove(eliminado)
            print(f"El alumno {eliminado} se quitó del la lista de alumnos correctamente")
            print(f"La lista actualizada quedó así: ", end = "")
        for i in range(len(alumnos)):
            if i == len(alumnos) - 1:
                print(alumnos[i])
            else:
                print(alumnos[i], end = ", ")
        else:
            print("El alumno ingresado no existe")
    case _:
        print("Opción inválida, debes seleccionar 1 o 2")"""

### Ejercicio 6 ###
"""
numeros = [1,2,3,4,5,6,7]
ultimo_numero = numeros[-1]
numeros.remove(numeros[-1])
numeros.insert(0, ultimo_numero)
print(f"La lista actualizada queda así:", end = " ")
for i in range(len(numeros)):
    if i == len(numeros) - 1:
        print(numeros[i])
    else:
        print(numeros[i], end = ", ")"""

### Ejercicio 7 ###
"""
temperaturas = [
    [10,20],
    [13,16],
    [13,19],
    [7,12],
    [19,31],
    [6,14],
    [15,23]
]
suma_min = 0
suma_max = 0
diferencia = 0
for i in range(len(temperaturas)):
    suma_min += temperaturas[i][0]
    suma_max += temperaturas[i][1]
    if temperaturas[i][1] - temperaturas[i][0] > diferencia:
        diferencia = temperaturas[i][1] - temperaturas[i][0]
        dia = i
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
promedio_min = suma_min / len(temperaturas)
promedio_max = suma_max / len(temperaturas)

print(f"El promedio de las temperaturas mínimas es: {promedio_min:.2f}")
print(f"El promedio de las temperaturas máximas es: {promedio_max:.2f}")
print(f"El día que mayor AT hubo fue el {dias[dia]}, fue de {diferencia} grados")"""

### Ejercicio 8 ###
"""
notas = [
    [5,8,7.8],
    [10,4.9,8],
    [9.2,6.5,7.3],
    [7,8,9],
    [9.8,7,3.1]
]
for i in range(len(notas)):
    suma = 0
    for j in range(len(notas[i])):
        suma += notas[i][j]
    promedio = suma / len(notas[i])
    print(f"El promedio del estudiante {i+1} es: {promedio:.2f}")
for j in range(len(notas[i])):
    suma_materia = 0
    for i in range(len(notas)):
        suma_materia += notas[i][j]
    promedio_materia = suma_materia / len(notas)
    print(f"El promedio de la materia {j+1} es: {promedio_materia:.2f}")"""

### Ejercicio 9 ###
"""
tateti = [
    [" - "," - "," -"],
    [" - "," - "," -"],
    [" - "," - "," -"]
]
turno = True
cantidad_turnos = 0
while True:
    print(f"Estado actual del tateti:")
    for i in range(len(tateti)):
        print(f"{tateti[i]}")
    if cantidad_turnos >= 9:
        break    
    if turno:
        print("Turno del jugador de X")
        fila = int(input("Ingresa la fila: "))
        columna = int(input("Ingresa la columna: "))
        tateti[fila][columna] = " X "
        turno = False
        cantidad_turnos += 1
    else:
        print("Turno del jugador de O")
        fila = int(input("Ingresa la fila: "))
        columna = int(input("Ingresa la columna: "))
        tateti[fila][columna] = " O "
        turno = True
        cantidad_turnos += 1"""

### Ejercicio 10 ###
"""
productos = [[15,7,2,6],
            [19,10,1,3],
            [17,6,4,9],
            [13,4,0,6],
            [11,8,7,11],
            [9,5,7,13],
            [10,5,1,8]]
v1 = 0
v2 = 0
v3 = 0
v4 = 0

ventas_dia = 0
dia_mas_ventas = 0
for i in range(len(productos)):
    v1 += productos[i][0]
    v2 += productos[i][1]
    v3 += productos[i][2]
    v4 += productos[i][3]
    if sum(productos[i]) > ventas_dia:
        ventas_dia = sum(productos[i])
        dia_mas_ventas = i + 1

ventas_productos = [v1,v2,v3,v4]
cantidad_producto = 0
for i in range(len(ventas_productos)):
    if ventas_productos[i] > cantidad_producto:
        cantidad_producto = ventas_productos[i]
        producto_mas_vendido = i + 1


print(f"Del producto 1 se vendieron {v1} unidades")
print(f"Del producto 2 se vendieron {v2} unidades")
print(f"Del producto 3 se vendieron {v3} unidades")
print(f"Del producto 4 se vendieron {v4} unidades")
print(f"El día con más ventas fue el día {dia_mas_ventas}")
print(f"El producto más vendido fue el producto {producto_mas_vendido}")"""

### Ejercicio 11 ###
"""
alumnos = ["Ana","Carlos","Elena","David","Lucía","Mateo","Sofía","Alejandro","Valentina","Lucas"
]
buscado = input("Ingrese el nombre que quiere buscar en la lista de alumnos(Se distinguen mayúsculas de minúsculas): ")
if buscado in alumnos:
    print(f"El alumno si está en la lista, está en la posición {alumnos.index(buscado) + 1}")
else:
    print("El alumno no se encuentra en la lista")"""

### Ejercicio 12 ###
"""
numeros = []
for i in range(1,9):
    ingresado = int(input(f"Ingrese el número {i}(Debe ser si o si un número): "))
    numeros.append(ingresado)
print(f"Lista original: ", end = "")
for i in range(len(numeros)):
    if i == len(numeros) - 1:
        print(numeros[i])
    else:
        print(numeros[i], end = ", ")
print(f"Lista ordenada de menor a mayor:", end = " ")
for i in range(len(numeros)):
    if i == len(numeros) - 1:
        print(sorted(numeros)[i])
    else:
        print(sorted(numeros)[i], end = ", ")
print(f"Lista ordenada de mayor a menor:", end = " ")
for i in range(len(numeros)):
    if i == len(numeros) - 1:
        print(sorted(numeros, reverse= True)[i])
    else:
        print(sorted(numeros, reverse= True)[i], end = ", ")"""

### Ejercicio 13 ###
"""
puntajes = [450, 1200, 875, 990, 300, 1500, 640]

puntaje_mas_bajo = puntajes[0]
puntaje_mas_alto = 0
for i in range(len(puntajes)):
    if puntajes[i] > puntaje_mas_alto:
        puntaje_mas_alto = puntajes[i]
    if puntajes[i] < puntaje_mas_bajo:
        puntaje_mas_bajo = puntajes[i]
print(f"El puntaje más bajo del ranking es de: {puntaje_mas_bajo} puntos")
print(f"El puntaje más alto del ranking es de: {puntaje_mas_alto} puntos")

print(f"El ranking de mayor a menor queda así:", end = " ")
for i in range(len(puntajes)):
    if i == len(puntajes) - 1:
        print(sorted(puntajes, reverse= True)[i])
    else:
        print(sorted(puntajes, reverse= True)[i], end = ", ")

print(f"La puntuación de 990 puntos ocupa el puesto {sorted(puntajes, reverse= True).index(990) + 1} del ranking")"""