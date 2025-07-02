# CREANDO SETS
colores = {"Azul", "Rojo", "Azul", "Verde"}
colorcitos = {"Azul", "Naranja"}

# IMPRIMIENDO EL SET COLORES
print(colores)

# AGREGANDO UN NUEVO ELEMENTO AL SET
colores.add("Blanco")
print(colores)

# ELIMINANDO UN ELEMENTO DEL SET
colores.discard("Blanco")
print(colores)

# APLICANDO EL MÉTODO DIFFERENCE
diferencia = colores.difference(colorcitos)
print(diferencia)

colorines = (colores.intersection(colorcitos))
print(colorines)
