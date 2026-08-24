print("Bienvenodo a la calculadora de patentes")

patente = input("Ingresa l apatende que quieres calcular(formato LL NNN LL): ")
limpia = patente.replace(" ", "").upper()

letras = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25
}

letra1 = letras[limpia[0]]
letra2 = letras[limpia[1]]
letra3 = letras[limpia[5]]
letra4 = letras[limpia[6]]
num1 = int(limpia[2])
num2 = int(limpia[3])
num3 = int(limpia[4])

numero_total = num1 * 100 + num2 * 10 + num3

decimal = letra1
decimal = decimal * 26 + letra2
decimal = decimal * 1000 + numero_total
decimal = decimal * 26 + letra3
decimal = decimal * 26 + letra4

print(f"La pantente {limpia} es la patente N°{decimal+1}")

decimal_sumado = int(input(f"Ingresa el número que le quires sumar a la patente N°{decimal} y mostraré la patente correspondiente a ese número: "))

decimal_sumado += decimal
mostrar_decimal = decimal_sumado

letras_inverso = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
    8: "I",
    9: "J",
    10: "K",
    11: "L",
    12: "M",
    13: "N",
    14: "O",
    15: "P",
    16: "Q",
    17: "R",
    18: "S",
    19: "T",
    20: "U",
    21: "V",
    22: "W",
    23: "X",
    24: "Y",
    25: "Z"
}

nueva_letra4 = decimal_sumado % 26
decimal_sumado = decimal_sumado // 26

nueva_letra3 = decimal_sumado % 26
decimal_sumado = decimal_sumado // 26

numero = decimal_sumado % 1000
numero = str(numero)
if len(numero) == 1:
    numero = "00" + numero
elif len(numero) == 2:
    numero = "0" + numero
decimal_sumado = decimal_sumado // 1000

nueva_letra2 = decimal_sumado % 26
decimal_sumado = decimal_sumado // 26

nueva_letra1 = decimal_sumado % 26

letra1 = letras_inverso[nueva_letra1]
letra2 = letras_inverso[nueva_letra2]
letra3 = letras_inverso[nueva_letra3]
letra4 = letras_inverso[nueva_letra4]

patente_sumada = letra1 +letra2 + numero + letra3+ letra4

print(f"La patente {patente_sumada} es la que corresponde al número {mostrar_decimal+1}")