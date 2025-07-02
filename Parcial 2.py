# A) Crea un diccionario cuyas claves deben ser los números de ingreso y los valores sean sub-diccionarios con las claves "Edad"
gatitos = {
    101 : {
        "Nombre" : "Luna",
        "Peso" : 1.2,
        "Edad" : 3,
        "Tamaño" : 30
    },

    102 : {
        "Nombre" : "Michi",
        "Peso" : 0.8,
        "Edad" : 2,
        "Tamaño" : 25
    },
    103 : {
        "Nombre" : "Pepito",
        "Peso" : 2.5,
        "Edad" : 5,
        "Tamaño" : 35
    }
}

print(gatitos)
print("")

# B) Recorrer el diccionario principal con un bucle y, en cada sub-diccionario, añadir la clave "Clasificación-Peso" dependiendo del valor del peso
try:
    "Clasificacion peso".__add__(gatitos[101])
    Clasificacion = gatitos[101]["Peso"]
    if Clasificacion < 1:
        gatitos[101]["Clasificacion peso"] = "Bajo Peso"
    elif 1 <= Clasificacion <= 4:
        gatitos[101]["Clasificacion peso"] = "Normal"
    else:
        gatitos[101]["Clasificacion peso"] = "Sobre Peso"
except:
    gatitos[101]["Clasificacion peso"] = "Desconocida"

try:
    "Clasificacion peso".__add__(gatitos[102])
    Clasificacion = gatitos[102]["Peso"]
    if Clasificacion < 1:
        gatitos[102]["Clasificacion peso"] = "Bajo Peso"
    elif 1 <= Clasificacion <= 4:
        gatitos[102]["Clasificacion peso"] = "Normal"
    else:
        gatitos[102]["Clasificacion peso"] = "Sobre Peso"
except:
    gatitos[102]["Clasificacion peso"] = "Desconocida"

try:
    "Clasificacion peso".__add__(gatitos[103])
    Clasificacion = gatitos[103]["Peso"]
    if Clasificacion < 1:
        gatitos[103]["Clasificacion peso"] = "Bajo Peso"
    elif 1 <= Clasificacion <= 4:
        gatitos[103]["Clasificacion peso"] = "Normal"
    else:
        gatitos[103]["Clasificacion peso"] = "Sobre Peso"
except:
    gatitos[103]["Clasificacion peso"] = "Desconocida"



# C) Crear otro bucle para agregar la clave "Categoría-Etaria" basada en la edad
try:
    "Categoría-Etaria".__add__(gatitos[101])
    Categoria = gatitos[101]["Edad"]
    if Categoria < 4:
        gatitos[101]["Categoría-Etaria"] = "Cachorro"
    elif 4 <= Categoria <= 12:
        gatitos[101]["Categoría-Etaria"] = "Joven"
    else:
        gatitos[101]["Categoría-Etaria"] = "Adulto"
except:
    gatitos[101]["Categoría-Etaria"] = "Desconocida"

try:
    "Categoría-Etaria".__add__(gatitos[102])
    Categoria = gatitos[102]["Edad"]
    if Categoria < 4:
        gatitos[102]["Categoría-Etaria"] = "Cachorro"
    elif 4 <= Categoria <= 12:
        gatitos[102]["Categoría-Etaria"] = "Joven"
    else:
        gatitos[102]["Categoría-Etaria"] = "Adulto"
except:
    gatitos[102]["Categoría-Etaria"] = "Desconocida"


try:
    "Categoría-Etaria".__add__(gatitos[103])
    Categoria = gatitos[103]["Edad"]
    if Categoria < 4:
        gatitos[103]["Categoría-Etaria"] = "Cachorro"
    elif 4 <= Categoria <= 12:
        gatitos[103]["Categoría-Etaria"] = "Joven"
    else:
        gatitos[103]["Categoría-Etaria"] = "Adulto"
except:
    gatitos[103]["Categoría-Etaria"] = "Desconocida"

# D) Crear una lista de tuplas, donde el primer elemento de la tupla es el “N° de Ingreso”, y el segundo valor es el “Peso"
lista_tuplas = list((101, gatitos[101]["Peso"], 102, gatitos[102]["Peso"], 103, gatitos[103]["Peso"]))
print(lista_tuplas)

# F) Pedir al usuario el número de ingreso de un gatito existente y el nuevo tamaño
print("Escoge el gatito al cual cambiarle el peso")
print("")
n_dict = input()
print("")

match n_dict:
    case "101":
        print(f"Has escogido a {gatitos[101]["Nombre"]} ¿Que peso deseas agregarle?")

match n_dict:
    case "102":
        print(f"Has escogido a {gatitos[102]["Nombre"]} ¿Que peso deseas agregarle?")

match n_dict:
    case "103":
        print(f"Has escogido a {gatitos[103]["Nombre"]} ¿Que peso deseas agregarle?")
match n_dict:
    case _:
        print("No puede quedar vacio")
print("")

# Crear una lista con todos los valores de "Peso"
Peso_de_Gatitos = [gatitos[101]["Peso"], gatitos[102]["Peso"], gatitos[103]["Peso"]]
print(Peso_de_Gatitos)
print("")

# Luego calcular e imprimir el promedio de los pesos
promedio_pesos = sum(Peso_de_Gatitos)
print(f"El promedio de los pesos de los 3 gatitos es {promedio_pesos}")
print("")

# Despues calcular el peso menor y peso mayor
peso_min = min(Peso_de_Gatitos)
peso_max = max(Peso_de_Gatitos)
print("")

print(f"El menor peso de los gatitos es {peso_min}")
print(f"El mamyor peso de los gatitos es {peso_max}")
print("")

# Por ultimo el Número de ingreso del gatito con más bajo peso.
print(f"El peso mas bajo de los gatitos es {Peso_de_Gatitos[1]}")
print("")


# Despues de terminar todo imprimir el diccionario completo, ordenado por número de ingreso
Nuevo_diccionario = (list(gatitos.items()))
print(Nuevo_diccionario)