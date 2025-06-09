'''
4. Desarrollar un programa de gestión de inventario:
A. Ingresar el nombre de un producto y su precio unitario.
B. Ingresar la cantidad en stock.
C. Calcular el valor total de los productos ingresados y mostrarlo con 2 decimales.
D. Crear una variable booleana llamada umbral, que entregue un True si el valor_total >
100000 y False en caso contrario..
E. Imprimir el nombre del producto, la cantidad, el valor total y el estado umbral en un solo
print() formateado.
'''

producto = (input("Ingresa un producto: "))
precio_de_producto = (input("Ingresa el coste del producto: "))
stock = (input("Ingrese la cantida en stock: "))

valor_total = (precio_de_producto * stock)
print(round(valor_total))
umbral = valor_total > 100000
print(umbral)

