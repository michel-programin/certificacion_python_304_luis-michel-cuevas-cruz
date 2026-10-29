persona={
    "nombre":"luis",
    "edad":16,
    "profesion":"programador",
    "estudiante":False
}
print(persona)
#accediando a un valor en especifico
print(persona["nombre"])
print(persona.get("profecion"))
persona["edad"]=18
print(persona["edad"])
persona["ciudad"]="san nicolas de los cerrosss tu"
print(persona)