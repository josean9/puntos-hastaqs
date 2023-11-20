listademoves= []
def BuscarEntrada(mapa):
    
    columnas = len(mapa)
    filas = len(mapa[0])
    numero=0
    
    for i in range(columnas):
        for j in range(filas):
            if mapa[i][j] == "A":
                
                return BuscarSalida(mapa, i, j, filas, columnas, numero, None)
    return "NO"

def BuscarSalida(mapa, i, j, fil, col, contador, palabra):
    salida = False
    if palabra == "R":
        listademoves.append("R")
    elif palabra == "L":
        listademoves.append("L")
    elif palabra == "U":
        listademoves.append("U")
    elif palabra == "D":
        listademoves.append("D")
    while True:
        if i < 0 or i >= col or j < 0 or j >= fil or mapa[i][j] == '#':
            if listademoves:
                listademoves.pop()
            break
        if mapa[i][j] == "B":
            salida = True
            print("YES", "contador:", contador, "moves:", listademoves)
            

            
        

        mapa[i][j] = '#'
        
        BuscarSalida(mapa, i + 1, j, fil, col, contador+1, "D")
        BuscarSalida(mapa, i - 1, j, fil, col, contador+1,"U")
        BuscarSalida(mapa, i, j + 1, fil, col, contador+1,"R")
        BuscarSalida(mapa, i, j - 1, fil, col, contador+1,"L")
        break
    if salida == False:
        return "NO"
        
mapa2 = [
    list("########"),
    list("#.A#...#"),
    list("#.##.#B#"),
    list("#......#"),
    list("########")
]


BuscarEntrada(mapa2)
