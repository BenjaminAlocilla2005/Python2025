# CREANDO DICCIONARIO (SE AGREGAN DIFERENTES TIPOS DE DATOS ESTRUCTURADOS)
paciente = {
    "nombre" : "Carlos",
    "apellido" : "Santana",
    "edad" : 50,
    "ciudad" : "Quellon",
    "consultas" : [14, 20, 40],
    "diagnostico" : ("resfrio")
}

# OTRA FORMA DE DECLARAR DICCIONARIOS
medico = dict(
    nombre = "Samir",
    apellido = "Arana",
    edad = 20,
    especialidad = "Neurologo"
)

#IMPRESION DE DICCIONARIOS
print(paciente)
print(medico)

# CONSULTANDO UN ELEMENTO A TRAVÉS DE LA CLAVE DEL DICCIONARIO
print(medico["nombre"])

# ELIMINANDO UNA CLAVE DEL DICCIONARIO (MÉTODO DEL)
del(paciente["nombre"])
print(paciente)

print(paciente.keys())
print(paciente.values())
print(paciente.items())