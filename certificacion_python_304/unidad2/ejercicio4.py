mapa=[
    [".",".",",","."],
    [".",".","x","."],
    [".",".",",","."],
    [".",".",".","."]
]
filas=len(mapa)
columnas=len(mapa)
for i in range(filas):
    for j in range(columnas):
        if mapa[i][j]=="x":
            print(f"mapa encotrado en la posicion[{i}][{j}]")