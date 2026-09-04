import random
lista_carton = random.sample(range(1,51), 25)

carton = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]
elemento_lista_carton = 0
for fila in range(0,5):
    for columna in range(0,5):
        carton[fila][columna] = lista_carton[elemento_lista_carton]
        elemento_lista_carton += 1
        print(carton[fila][columna], end= " ")
    print("")

sorteados = [0]
cantidad_sorteados = 0
bingo = True
while bingo:
    num_s = random.randint(1,50)
    if num_s in sorteados:
        continue
    else:
        sorteados.append(num_s)
        print(f"El número que tocó es el {num_s}")
        for i in range(0,5):
            for j in range(0,5):
                if carton[i][j] == num_s:
                    carton[i][j] = 0
        cantidad_sorteados += 1

    for fila in carton:
        cantidad_cero_fila = fila.count(0)
        if cantidad_cero_fila == 5:
            bingo = False
        for columna in range(len(fila)):
            columna_bingo = [fila[columna] for fila in carton]
            cantidad_cero_columna = columna_bingo.count(0)
            if cantidad_cero_columna == 5:
                bingo = False

    ceros_diago = 0
    for i in range(len(carton)):
        if carton[i][i] == 0:
            ceros_diago += 1
        if carton[1][3] == 0 and carton[3][1] == 0 and carton[0][4] == 0 and carton[4][0] == 0 and carton[2][2] == 0:
            bingo = False

print("¡BINGO!")
print(f"La cantidad de numeros sorteados fueron: {cantidad_sorteados}")

for i in range(len(carton)):
    for j in range(len(carton[0])):
        print(carton[i][j], end = " ")
    print("")