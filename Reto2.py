# Primero se pone el diccionario con el nombre inventario y poner 
inventario = dict(
    Manzana = (1000, 600, 790),
    Platano = (800, 800, 720),
    Cereza = (500, 640, 650)
)

print(inventario)


print(inventario["Platano"])


print(sorted(inventario["Platano"]))


tipos_frutas = [inventario]
print(tipos_frutas)

precios_platano = tipos_frutas
print(precios_platano)









