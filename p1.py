
from collections import defaultdict
from itertools import combinations

with open("input.txt") as file:
    cuadricula = file.read().strip().split("\n")

print(cuadricula)

n = len(cuadricula)

def en_limite(x, y):
    return 0 <= x < n and 0 <= y < n

def get_antinodos(a, b):
    ax, ay = a
    bx, by = b
    
    cx, cy = ax - (bx - ax), ay - (by - ay)
    dx, dy = bx + (bx - ax), by + (by - ay)

    if en_limite(cx, cy):
        yield (cx, cy)
    if en_limite(dx, dy):
        yield (dx, dy)


antinodos = set()

ubicaciones = defaultdict(list)
for i in range(n):
    for j in range(n):
        if cuadricula[i][j] != ".":
            ubicaciones[cuadricula[i][j]].append((i, j))


for freq in ubicaciones:
    locs = ubicaciones[freq]
    for a, b in combinations(locs, r=2):
        for antinode in get_antinodos(a, b):
            antinodos.add(antinode)


print(len(antinodos))
