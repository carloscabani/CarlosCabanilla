from itertools import product

with open("input.txt") as file:
    lineas = file.read().strip().split("\n")

total = 0

for i, linea in enumerate(lineas):
    separacion = linea.split()
    valor = int(separacion[0][:-1])
    numeros = list(map(int, separacion[1:]))

    def prueba(combinaciones):
        total = numeros[0]
        for i in range(1, len(numeros)):
            if combinaciones[i-1] == "+":
                total += numeros[i]

            elif combinaciones[i-1] == "|":
                total = int(f"{total}{numeros[i]}")
                
            else:
                total *= numeros[i]

        return total

    long_cadena = len(numeros)-1

    for combinaciones in product("*+|", repeat=long_cadena):
        if prueba(combinaciones) == valor:
            total += valor
            break


print(total)