tabla = [
    ["nombre","edad","calificacion"],
    ["emily",16,8.9],
    ["carlos yair",16,10],
    ["carlos yair",16,10],
    ["leo",15,9.9],
    ["america",16,9.8],
    ["luis",16,6.7],
    ["sdanna",16,6.7],
    ["carlos",16,10],
    ["brian",16,6.8],
    ["kimberly",16,10]
]
filas=len(tabla)
columnas=len(tabla)
nombre=len(tabla[0])
for i in range(filas):
    for j in range(columnas):
        if tabla[i][j] == nombre:
           print(f"tabla encontrada en la posision[{i}][{j}]")
       