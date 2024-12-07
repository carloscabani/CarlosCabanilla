orden_paginas = []
actualizaciones = []
total = 0
lineas = []

with open("input.txt", "r") as file:
    for linea in file:
        linea = linea.strip()
        if linea:
            lineas.append(linea)


for linea in lineas:
    if "|" in linea:
        orden_paginas.append(tuple(map(int, linea.split("|"))))
    else:
        actualizaciones.append(list(map(int, linea.split(","))))

def actualizacion_valida(actualizacion, reglas):
    for x, y in reglas:
        if x in actualizacion and y in actualizacion:
            if actualizacion.index(x) > actualizacion.index(y):
                return False
    return True

for actualizacion in actualizaciones:
    if actualizacion_valida(actualizacion, orden_paginas):
        medio = len(actualizacion) // 2
        total += actualizacion[medio]

print(total)
