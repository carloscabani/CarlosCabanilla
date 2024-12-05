import re

def parte1(expresion_regular):
    
    with open("input.txt", 'r') as file:
        lineas = file.read()

    ies = re.findall(expresion_regular, lineas)

    total = sum(int(x) * int(y) for x, y in ies)

    print("Primera parte: ", total)


def parte2():

    total = 0

    with open("input.txt", 'r') as file:
        lineas = file.read()

    instrucciones = re.finditer(r'mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)', lineas)

    m_habilitada = True
    #mul(2,3)
    for i in instrucciones:

        if i.group(0).startswith('mul'): #mul
            a = int(i.group(1)) #2
            b = int(i.group(2)) #3
            if m_habilitada:
                total += a * b
        
        elif i.group(0) == 'do()':
            m_habilitada = True

        elif i.group(0) == "don't()":
            m_habilitada = False

    print("Parte 2: ", total)




def main():

    expresion_regular_mul = r'mul\((\d+),(\d+)\)'
    parte1(expresion_regular_mul)

    parte2()

if __name__ == "__main__":
    main()
    