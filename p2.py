from tqdm import tqdm

with open("input.txt") as fin:
    cuadricula = [list(line) for line in fin.read().strip().split("\n")]

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

ii = i
jj = j

l_direcciones = [[-1, 0], [0, 1], [1, 0], [0, -1]]

dir = 0
c_visitas = set()
while True:
    
    c_visitas.add((i, j))

    sig_i = i + l_direcciones[dir][0]
    sig_j = j + l_direcciones[dir][1]

    if not (0 <= sig_i < n and 0 <= sig_j < n):
        break

    if cuadricula[sig_i][sig_j] == "#":
        dir = (dir + 1) % 4
    else:
        i, j = sig_i, sig_j


def encontrar_bucle(oi, oj):
    if cuadricula[oi][oj] == "#":
        return False
    
    cuadricula[oi][oj] = "#"
    i, j = ii, jj

    dir = 0
    c = set()
    while True:
        if (i, j, dir) in c:
            cuadricula[oi][oj] = "."
            return True
        c.add((i, j, dir))

        sig_i = i + l_direcciones[dir][0]
        sig_j = j + l_direcciones[dir][1]

        if not (0 <= sig_i < n and 0 <= sig_j < n):
            cuadricula[oi][oj] = "."
            return False

        if cuadricula[sig_i][sig_j] == "#":
            dir = (dir + 1) % 4
        else:
            i, j = sig_i, sig_j

total = 0
for oi, oj in tqdm(c_visitas):

    if oi == ii and oj == jj:
        continue
    bucle = encontrar_bucle(oi, oj)
    total += bucle

print(total)