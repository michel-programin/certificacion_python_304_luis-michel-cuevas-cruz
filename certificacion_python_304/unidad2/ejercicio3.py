abecedario=[
    ["a","b","c","d"],
    ["e","f","g","h"],
    ["i","j","k","l"],
    ["m","n","ñ","o"],
    ["m","n","Ñ"]
]
for i in range(0,4):
    for j in range(0,4):
        print(f"[{i}] [{j}] = {abecedario[i][j]}")