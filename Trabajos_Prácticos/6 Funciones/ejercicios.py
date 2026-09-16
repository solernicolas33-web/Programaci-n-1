### EJERCICIO 1 ###
"""
def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()
"""

### EJERCICIO 2 ###
"""
def saludar(nombre):
    print(f"Hola {nombre}, ¿Cómo estás?")
nombre = input("Ingresa el nombre de la persona que quieres que salude: ")
nombre = nombre.strip().capitalize()
while not nombre.replace(" ", "").isalpha() or nombre == "":
    print("El nombre no puede contener números ni estar vacío")
    nombre = input("Ingresa el nombre de la persona que quieres que salude: ")
    nombre = nombre.strip().capitalize()
saludar(nombre)
"""

### EJERCICIO 3 ###
"""
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Hola, soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
print("Ingresa tus datos personales")
nombre = input("Ingresa tu nombre: ")
nombre = nombre.strip().capitalize()
while not nombre.replace(" ", "").isalpha() or nombre == "":
    print("El nombre no puede contener números ni estar vacío")
    nombre = input("Ingresa tu nombre: ")
    nombre = nombre.strip().capitalize()
apellido = input("Ingresa tu apellido: ")
apellido = apellido.strip().capitalize()
while not apellido.replace(" ", "").isalpha() or apellido == "":
    print("El apellido no puede contener números ni estar vacío")
    apellido = input("Ingresa tu apellido: ")
    apellido = apellido.strip().capitalize()
edad = input("Ingresa tu edad: ")
edad = edad.replace(" ", "")
while not edad.isdigit():
    print("Error, la edad ingresada no es un número entero")
    edad = input("Ingresa tu edad: ")
    edad = edad.replace(" ", "")
residencia = input("Ingrese su residencia: ")
residencia = residencia.strip().capitalize()
while residencia == "":
    print("Erro, no ingresaste nada")
    residencia = input("Ingrese su residencia: ")
    residencia = residencia.strip().capitalize()
informacion_personal(nombre, apellido, edad, residencia)
"""

### EJERCICIO 4 ###
"""
import math

def calcular_area(radio):
    area = (radio ** 2) * math.pi
    return area

def calcular_perimetro(radio):
    perimetro = radio * 2 * math.pi
    return perimetro

radio = input("Ingrese el radio del círculo: ")
radio = radio.strip()
while not radio.replace(".", "").isdigit():
    print("Error, debes ingresar un número")
    radio = input("Ingrese el radio del círculo: ")
    radio = radio.strip()
radio = float(radio)

area = calcular_area(radio)
perimetro = calcular_perimetro(radio)

print(f"El area del círculos es {area:.2f}, y su perímetro es {perimetro:.2f}")
"""

### EJERCICIO 5 ###
"""
def segundos_a_horas(segundos):
    horas = (segundos / 60) / 60 
    return horas

segundos = input("Ingrese la catidad de segundos que quiere trsnsformar a horas: ")
segundos.strip()
while not segundos.isdigit():
    print("Error, los segundos ingresados deben ser un número entero")
    segundos = input("Ingrese la catidad de segundos que quiere trsnsformar a horas: ")
    segundos.strip()
segundos = int(segundos)

horas = segundos_a_horas(segundos)

print(f"{segundos} segundos equivale a {horas:.2f} hora/s")
"""

### EJERCICIO 6 ###
"""
def imprimir_tabla(num):
    for i in range(1,11):
        if i == 10:
            print(num * 10)
        else:
            print(num * i, end = ", ")

numero = input("Ingresa el número para mostrarte su tabla de multiplicación: ")
numero.strip()
while not numero.isdigit():
    print("Error, debes ingresar un número entero")
    numero = input("Ingresa el número para mostrarte su tabla de multiplicación: ")
    numero.strip()

numero = int(numero)

imprimir_tabla(numero)
"""

### EJERCICIO 7 ###
"""
def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    mult = a * b
    div = a / b
    return suma, resta, mult, div

num1 = input("Ingresa el primer número: ")
num1 = num1.strip()
while not num1.replace(".", "").isdigit():
    print("Error, no se ingresó un número")
    num1 = input("Ingresa el primer número: ")
    num1 = num1.strip()
num1 = float(num1)

num2 = input("Ingresa el segundo número: ")
num2 = num2.strip()
while not num2.replace(".", "").isdigit() or num2 == "0":
    if num2 == "0":
        print("Error, el segundo número no puede ser 0")
    else:
        print("Error, no se ingresó un número")
    num2 = input("Ingresa el segundo número: ")
    num2 = num2.strip()
num2 = float(num2)

tupla = operaciones_basicas(num1, num2)

print(f"{num1} + {num2} = {tupla[0]}")
print(f"{num1} - {num2} = {tupla[1]}")
print(f"{num1} * {num2} = {tupla[2]}")
print(f"{num1} / {num2} = {tupla[3]:.2f}")
"""

### EJERCICIO 8 ###
"""
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = input("Ingrese su peso en KiloGramo: ")
peso = peso.strip()
while not peso.replace(".", "").isdigit() or peso == "0":
    print("Error, el peso debe ser un número mayor a 0")
    peso = input("Ingrese su peso en KiloGramo: ")
    peso = peso.strip()
peso = float(peso)

altura = input("Ingrese su altura en Metros: ")
altura = altura.strip()
while not altura.replace(".", "") or altura == "0":
    print("Error, la altura debe ser un número mayor que 0")
    altura = input("Ingrese su altura en Metros: ")
    altura = altura.strip()
altura = float(altura)

imc = calcular_imc(peso, altura)
print(f"Tu IMC es de {imc:.2f}")
"""

### EJERCICIO 9 ###
"""
def celcius_a_fahrenheit(grados):
    fah = (grados * 9/5) + 32
    return fah

grados = input("Ingrese los grados celsius: ")
grados = grados.strip()
while not grados.replace(".", "").replace("-", "").isdigit():
    print("Error, no ingresaste un número")
    grados = input("Ingrese los grados celsius: ")
    grados = grados.strip()
grados = float(grados)

fahrenheit = celcius_a_fahrenheit(grados)

print(f"{grados}°C equivale a {fahrenheit}°F")
"""

### EJERCICIO 10 ###
"""
def calcular_promedio(a,b,c):
    promedio = (a+b+c) / 3
    return promedio

def pedir_num(cantidad):
    for i in range(cantidad):
        num = input(f"Ingresa el numero {i+1}: ")
        num = num.strip()
        while not num.replace(".", "").isdigit():
            print("Error, se debe ingresar un número mayor o igual que 0")
            num = input(f"Ingresa el numero {i+1}: ")
            num = num.strip()
        num = float(num)
        if i == 0:
            a = num
        elif i == 1:
            b = num
        else:
            c = num
    return a,b,c

numeros = pedir_num(3)
num1 = numeros[0]
num2 = numeros[1]
num3 = numeros[2]

promedio = calcular_promedio(num1,num2,num3)

print(f"El promedio de los 3 números ingresados es {promedio:.2f}")
"""