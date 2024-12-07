
with open("input.txt") as file:
    cuadricula = file.read().strip().split("\n")

n = len(cuadricula)
m = len(cuadricula[0])

pos_inicial_guardia = False

for i in range(n):
    for j in range(m):
        if cuadricula[i][j] == "^":
            pos_inicial_guardia = True
            break

    if pos_inicial_guardia:
        break

direccion = 0
l_direcciones = [[-1, 0], [0, 1], [1, 0], [0, -1]]

c_visitas = set()

while True:
    c_visitas.add((i, j))

    siguiente_i = i + l_direcciones[direccion][0]
    siguiente_j = j + l_direcciones[direccion][1]

    if not (0 <= siguiente_i < n and 0 <= siguiente_j < n):
        break

    if cuadricula[siguiente_i][siguiente_j] == "#":
        direccion = (direccion + 1) % 4
    else:
        i, j = siguiente_i, siguiente_j

print(len(c_visitas))
