def parte1(lineas):

    
    creciente = True
    decreciente = True

    for i in range(len(lineas)-1):
        diferencia = abs(lineas[i]-lineas[i+1])

        if diferencia < 1 or diferencia > 3:
            creciente = False
            decreciente = False
            break

        if lineas[i] >= lineas[i + 1]:
            creciente = False
            
            
        if lineas[i] <= lineas[i + 1]:
            decreciente = False
        
    return(creciente or decreciente)
        
            
    
   


def parte2():

    lineas = []

    with open("input.txt") as file:
        lineas = file.readlines()

    r_seguros = 0 

    for linea in lineas:
        reporte = list(map(int, linea.split()))
        
        if parte1(reporte):
            r_seguros += 1
        
        else:
            for i in range(len(reporte)):
                copia_reporte = reporte[:i] + reporte[i+1:]
                if parte1(copia_reporte):
                    r_seguros += 1
                    break

    print("Parte 2: ",r_seguros)



def main():
    parte2()

if __name__ == "__main__":
    main()