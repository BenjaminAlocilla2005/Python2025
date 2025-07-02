estudiante = {
    "nombre" : "María Lopez",
    "edad" : 22,
    "carrera" : "Ingenieria informatica",
    "promedio" : 8.5,
    "materías_aprobadas" : ["Programacion", "Matematicas", "Base de datos"]
}

# Preguntar una clave
print(estudiante["nombre"])
print(estudiante.get("edad", "no existe"))
print(estudiante.get("casa", "no existe"))

# Modificacion de valores
estudiante["edad"] = 23
estudiante["universidad"] = "Ulagos"
print(estudiante)

# Obtener todas las claves
print(estudiante.keys())

# Obtener todos los valores
print(estudiante.values())

print(estudiante.items())

for clave in estudiante:
    print(f"{clave}: {estudiante[clave]}")

for clave, valor in estudiante.items():
    print(f"{clave} -> {valor}")