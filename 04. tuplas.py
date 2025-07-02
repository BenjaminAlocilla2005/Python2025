# CREANDO E INSTANCIANDO UNA TUPLA
estudiantes = ("Samir", "Matias", "Hector", "Pia", "Carlos")

# IMPRIMIENDO UNA TUPLA
print(estudiantes)

# ELIMINANDO EL ÚLTIMO ELEMNTO DE LA TUPLA (NO SE PUEDE -> INMUTABLE)
"""estudiantes.pop()
print(estudiantes)"""
"""estudiantes = ("Constanza")
print(estudiantes)"""
print(estudiantes.count("Samir"))

# MÉTODO INDEX EN TUPLAS (INDICA LA POSICIÓN DE ELEMENTO)
print(estudiantes.index("Carlos"))

# METODO SORTED EN TUPLAS (ORDENA ELEMENTOS Y LO PASA A LISTA)
print(sorted(estudiantes))

numeros = (1,2,3,4,5,6)
print(max(numeros))
print(min(numeros))
print(sum(numeros))