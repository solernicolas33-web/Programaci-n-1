### EJERCICIO 1 ###
"""
edad = int(input("Ingrese la edad del usuario: "))
if edad >= 18:
    print("El usuario es mayor de edad")"""

### EJERCICIO 2 ###
"""
nota = int(input("Ingrese la nota del usuario: "))
if nota >= 6:
    print("El usuario está aproobado")
else:
    print("El usuario desaprobó")"""

### EJERCICIO 3 ###
"""
numero = int(input("Ingrese un número par: "))
if numero % 2 == 0:
    print("Has ingresado un número par")
else:
    print("Por favor, ingresa un numero par")"""

### EJERCICIO 4 ###
"""
edad = int(input("Ingrese la edad del usuario: "))
if edad >= 0:
    if edad < 12:
        print("Eres un niño/a")
    elif 12 <= edad < 18:
        print("Eres un adolescente")
    elif 18 <= edad < 30:
        print("Eres un adulto/a joven")
    else:
        print("Eres un adulto mayor")
else:
    print("Has ingresado un número negativo, no puede ser una edad")"""

### EJERCICIO 5 ###
"""
contraseña = input("Ingrese una contraseña de entre 8 y 14 caracters: ")

if 8 <= len(contraseña) <= 14:
    print("Has ingresado una contraseña válida")
else:
    print("ERROR, la contraseña debe tener entre 8 y 14 caracteres")"""

### EJERCICIO 6 ###
"""
energia = int(input("Ingrese la cantidad de energia gastada al mes en kWh: "))
if energia < 150:
    print("Consumo bajo")
elif 150 <= energia <= 300:
    print("Consumo medio")
elif energia > 300:
    print("Consumo alto")
    
if energia > 500:
    print("Considere medidas de ahorro energético")"""

### EJERCICIO 7 ###
"""
texto = input("Ingrese una frase: ")

if texto[-1] in "aeiouAEIOU":
    print(f"{texto}!")
else:
    print(texto)"""

### EJERCICIO 8 ###
"""
nombre = input("Ingrese el nombre del usuario: ")

opcion = input("Selecicona una opción:\n1. Mostrar nombre en MAYÚSCULAS\n2. Mostrar nombre en minúsculas\n3. Mostrar nombre con la primer letra en mayúscula\nOpción elegida: ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Has seleccionado una opción inválida, debe ser 1, 2 o 3")"""

### EJERCICIO 9 ###
"""
magnitud = float(input("Ingrese l amagnitud del terremoto en escala Richter: "))

if magnitud < 3:
    print("Muy leve(imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve(ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado(sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte(puede causar daños en estructuras débiles). ")
elif 6 <= magnitud < 7:
    print("Muy Fuerte(puede causar daños significativos)")
elif magnitud >= 7:
    print("Extremo(puede causar graves daños a gran escala)")
"""

### EJERCICIO 10 ###
"""
hemisferio = input("En que hemisferio está el usuario(s/n): ")

if hemisferio == "s" or hemisferio == "n":    
    mes = int(input("Ingrese el mes en el que se encuentra(1-12): "))
    dia = int(input("Ingrese el día en el que se encuentra(1-31): "))
    fecha = (mes * 100) + dia
    if (1 <= mes <= 12) and (1 <= dia <= 31):
        if fecha >= 1221 or fecha <= 320:
            if hemisferio == "s":
                print("Verano")
            else:
                print("Invierno")
        elif fecha >= 321 and fecha <= 620:
            if hemisferio == "s":
                print("Otoño")
            else:
                print("Primavera")
        elif fecha >= 621 and fecha <= 920:
            if hemisferio == "s":
                print("Invierno")
            else:
                print("Verano")
        elif fecha >= 921 and fecha <= 1220:
            if hemisferio == "s":
                print("Primavera")
            else:
                print("Otoño")
    else:
        print("Introdujiste una fecha inválida")
else:
    print("ERROR, El hemisferio debe ser s o n")"""