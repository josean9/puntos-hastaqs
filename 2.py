
def BuscarEntrada(mapa):
    columnas = len(mapa)
    filas = len(mapa[0])
    numero=0
    for i in range(columnas):
        for j in range(filas):
            if mapa[i][j] == "A":
                return BuscarSalida(mapa, i, j, filas, columnas, numero)
    return "NO"

def BuscarSalida(mapa, i, j, fil, col, contador):
    
    while True:
        if i < 0 or i >= col or j < 0 or j >= fil or mapa[i][j] == '#':
            
            break
        if mapa[i][j] == "B":
            print("YES", "contador:", contador)
        mapa[i][j] = '#'
        
        BuscarSalida(mapa, i + 1, j, fil, col, contador+1)
        BuscarSalida(mapa, i - 1, j, fil, col, contador+1)
        BuscarSalida(mapa, i, j + 1, fil, col, contador+1)
        BuscarSalida(mapa, i, j - 1, fil, col, contador+1)
    
mapa2 = [
    list("########"),
    list("#.A#...#"),
    list("#.##.#B#"),
    list("#......#"),
    list("########")
]

BuscarEntrada(mapa2)