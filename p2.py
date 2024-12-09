from collections import defaultdict
from itertools import combinations

with open("input.txt") as file:
    cuadricula = file.read().strip().split("\n")

n = len(cuadricula)

def en_limite(x, y):
    return 0 <= x < n and 0 <= y < n

def get_antinodos(a, b):
    ax, ay = a
    bx, by = b
    
    dx, dy = bx - ax, by - ay

    i = 0
    while True:
        if en_limite(ax - dx * i, ay - dy * i):
            yield (ax - dx * i, ay - dy * i)
        else:
            break
        i += 1
    
    i = 0
    while True:
        if en_limite(bx + dx * i, by + dy * i):
            yield (bx + dx * i, by + dy * i)
        else:
            break
        i += 1


antinodos = set()

ubicaciones = defaultdict(list)
for i in range(n):
    for j in range(n):
        if cuadricula[i][j] != ".":
            ubicaciones[cuadricula[i][j]].append((i, j))


for freq in ubicaciones:
    ubi = ubicaciones[freq]
    for a, b in combinations(ubi, r=2):
        for antinodo in get_antinodos(a, b):
            antinodos.add(antinodo)


for i in range(n):
    for j in range(n):
        if (i, j) in antinodos:
            print("#", end="")
        else:
            print(cuadricula[i][j], end="")
    print()


print(len(antinodos))