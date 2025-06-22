# Nombres de los Integrantes: Benjamin Alocilla y Ana Villegas

print("Bienvenido usuario, ingrese a continuación un párrafo para que este sea leído")

# primero agregamos una variable que sera el texto que ingresemos

parrafo = input("Ingrese su texto aqui: ")

# despues usamos if, len y raise el cual le ponemos un ValueError en caso de que el texto este vacio

if len(parrafo) == 0:
    raise ValueError("El texto no debe quedar vacio")
parrafo_nuevo = parrafo.split()
print(parrafo_nuevo)
print("")

# luego creamos otra variable para poner la palabra que queramos buscar
# y usamos for e if para que el contador funcione

palabra = input("Ahora indique una palabra a buscar: ")
contador_de_palabras = 0
for i in parrafo_nuevo:
    if palabra == i:
        contador_de_palabras = contador_de_palabras+1

# por ultimo usamos if y else para saber si el parrafo esta vacio o si tiene una palabra que se repite

if contador_de_palabras == 0:
    resultado = "El párrafo está vacío"
else:
    resultado = f"La palabra se repite: {contador_de_palabras} veces."

print(resultado)