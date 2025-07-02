# crear un inventariode productos a pagar
# 1. Pide al usuario el nombre del producto y cuántos quiere agregar.
# 2. Si el usuario existe, suma la cantidad.
# 3. Si no existe, agrégalo con esa cantidad.
# 4. Mostrar el inventario final al final del programa

# Creación de diccionario
inventario = {
    "manzana" : 3,
    "pepino" : 5,
    "bebida" :2,
    "jugo" : 8
}

print("Bienvenido usuario a nuestra tienda, ingrese la opcion que desea ejecutar \n ( 1: 'mostrar productos disponibles' 2: 'agregar producto' 3: 'mostrar productos a comprar (mi carro)')")

opcion = str(input("ingresa tu opcion: (1 | 2 | 3 | salir)\n >"))

while True:
    if opcion == "1": # listo
        print("Mostrando productos disponibles: ")
        print("Procesando... \n")
        for i in inventario:
            cantidad = inventario.get(i)
            print(f"{i} | cantidad: {cantidad}")
    elif opcion == "2":
        print("Porfavor ingresa el producto que deseas agregar al inventario: \n > ")
        nombre = str(input("> "))
        print("Ahora ingrese la cantidad del producto: ")
        cantidad = int(input("> "))
        inventario_nuevo = {nombre:cantidad}
        inventario.update(inventario_nuevo)
        print(f"Su inventario actualizado: {inventario}")
        print(inventario)


    elif opcion == "3":
        pass
    elif opcion == "salir":
        pass
    else:
        pass
