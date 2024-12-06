with open("input.txt") as fin:
    lineas = fin.read().strip().split("\n")

n = len(lineas)
m = len(lineas[0])

cuadricula = []
for dx in range(-1, 2):
    for dy in range(-1, 2):
        if dx != 0 or dy != 0:
            cuadricula.append((dx, dy))

# cuadricula = [(-1, -1), (-1, 0), (-1, 1),
#       (0, -1),           (0, 1),
#       (1, -1), (1, 0), (1, 1)]

def tener_xmas(i, j, d):
    dx, dy = d
    for k, x in enumerate("XMAS"):
        ii = i + k * dx
        jj = j + k * dy
        if not (0 <= ii < n and 0 <= jj < m):
            return False
        if lineas[ii][jj] != x:
            return False
    return True


total = 0
for i in range(n):
    for j in range(m):
        for d in cuadricula:
            total += tener_xmas(i, j, d)

print(total)