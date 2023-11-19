def contar_habitaciones(mapa):
    n = len(mapa)
    m = len(mapa[0])
    habitaciones = 0

    def dfs(i, j):
        if i < 0 or i >= n or j < 0 or j >= m or mapa[i][j] == '#':
            return
        mapa[i][j] = '#'  # Marcar el cuadro como visitado
        dfs(i + 1, j)    # Moverse hacia abajo
        dfs(i - 1, j)    # Moverse hacia arriba
        dfs(i, j + 1)    # Moverse hacia la derecha
        dfs(i, j - 1)    # Moverse hacia la izquierda

    for i in range(n):
        for j in range(m):
            if mapa[i][j] == '.':
                habitaciones += 1
                dfs(i, j)

    return habitaciones

# Mapa de ejemplo
mapa_ejemplo = [
    list("########"),
    list("#..#...#"),
    list("####.#.#"),
    list("#..#...#"),
    list("########")
]

# Contar el número de habitaciones
resultado = contar_habitaciones(mapa_ejemplo)
print(resultado)
