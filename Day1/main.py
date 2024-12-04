def parte1():
    
    lineas = []
    
    with open("input.txt") as file:
        lineas = file.readlines()

    lista1 = []
    lista2 = []

    for i in range(len(lineas)): 
        lista1.append(int(lineas[i].split(' ')[0])) 
        lista2.append(int(lineas[i].split(' ')[-1]))

    lista1.sort()
    lista2.sort()

    total= 0

    for i in range(len(lista1)):
        total += abs(lista1[i] - lista2[i])

    print(total)


def parte2():

    lineas = []
    
    with open("input.txt") as file:
        lineas = file.readlines()
    
    lista1 = []
    lista2 = []

    for i in range(len(lineas)):
        lista1.append(int(lineas[i].split(' ')[0]))
        lista2.append(int(lineas[i].split(' ')[-1]))

    total = 0

    for i in range(len(lista1)):
        repeticiones = lista2.count(lista1[i])
        total += lista1[i]*repeticiones


    print(total)



parte1()
parte2() 