# ejemplos de diccionarios con condicionales
precio_frutas = {
    "manzana" : 1.5,
    "banana" : 0.8,
    "naranja" : 1.2,
    "uva" : 2.3,
    "mango" : 2.5
}

# Solicitar una fruta al usuario
fruta = input("¿Que fruta deseas  comprar? (manzana, banana, naranja, uva, mango): ").lower()

# Verificar si la fruta esta en el diccionario
if fruta in precio_frutas:
    print(f"El precio de {fruta} es ${precio_frutas[fruta]:.2f}")
    
    if precio_frutas[fruta] > 2.0:
        print("¡Esta fruta es un poco cara!")
    else:
        print("¡Buen precio!")
else:
    print(f"Lo siento, no tenemos {fruta} en nuestro inventario")