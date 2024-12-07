from collections import defaultdict

with open("input.txt") as file:
    c_reglas, updates = file.read().strip().split("\n\n")
    reglas = []
    for line in c_reglas.split("\n"):
        a, b = line.split("|")
        reglas.append((int(a), int(b)))
    updates = [list(map(int, line.split(","))) for line in updates.split("\n")]


def seguir_reglas(update):
    dic = {}
    for i, num in enumerate(update):
        dic[num] = i
    
    for a, b in reglas:
        if a in dic and b in dic and not dic[a] < dic[b]:
            return False, 0
        
    return True, update[len(update) // 2]

def ordenar(update):
    r = []
    for a, b in reglas:
        if not (a in update and b in update):
            continue
        r.append((a, b))

    indeg = defaultdict(int)
    for a, b in r:
        indeg[b] += 1
    
    lista_ordenada = []
    while len(lista_ordenada) < len(update):
        for x in update:
            if x in lista_ordenada:
                continue
            if indeg[x] <= 0:
                lista_ordenada.append(x)
                for a, b in r:
                    if a == x:
                        indeg[b] -= 1
    
    return lista_ordenada


total = 0

for update in updates:
    if seguir_reglas(update)[0]:
        continue

    act_ordenada = ordenar(update)
    total += act_ordenada[len(act_ordenada) // 2]

print(total)