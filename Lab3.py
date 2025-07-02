# A) Primero creamos el diccionario, usando los codigos postales como claves y su valor debe ser un Sub-conjunto con la Ciudad, la temperatura y la precipitacion
ciudades = {
    5700000 : {
        "Ciudad" : "Castro",
        "Temperatura" : 11.8,
        "Precipitacion" : 2000
    },
    5770000 : {
        "Ciudad" : "Chonchi",
        "Temperatura" : 8.3,
        "Precipitacion" : 2800
    },
    5790000 : {
        "Ciudad" : "Quellón",
        "Temperatura" : 10.3,
        "Precipitacion" : 2950
    }
}
print(ciudades)
print("")

# B) Agregar a cada sub-diccionario una nueva clave llamada Clima que va a determinarse dependiendo de la temperatura
# y tambien implementar una estructura de control de errores utilizando try y except en caso de que la temperatura no esté disponible o se generé un error
try:
    Temp_Castro = ciudades[5700000]["Temperatura"]
    if Temp_Castro < 10:
        ciudades[5700000]["Temperatura"] = "Frío"
    elif Temp_Castro > 10:
        ciudades[5700000]["Temperatura"] = "Templado"
    else:
        ciudades[5700000]["Temperatura"] = "Cálido"
except ValueError:
    ciudades[5700000]["Temperatura"] = "Desconocida"

try:
    Temp_Chonchi = ciudades[5770000]["Temperatura"]
    if Temp_Chonchi < 10:
        ciudades[5770000]["Temperatura"] = "Frío"
    elif Temp_Chonchi > 10:
        ciudades[5770000]["Temperatura"] = "Templado"
    else:
        ciudades[5770000]["Temperatura"] = "Cálido"
except ValueError:
    ciudades[5770000]["Temperatura"] = "Desconocida"

try:
    Temp_Quellón = ciudades[5790000]["Temperatura"]
    if Temp_Quellón < 10:
        ciudades[5790000]["Temperatura"] = "Frío"
    elif Temp_Quellón > 10:
        ciudades[5790000]["Temperatura"] = "Templado"
    else:
        ciudades[5790000]["Temperatura"] = "Cálido"
except ValueError:
    ciudades[5790000]["Temperatura"] = "Desconocida"

# C) Agregar al sub-diccionario de Castro una nueva clave "Meses Más Lluviosos" que contenga una lista vacía.
# ciudades[5700000]

# D) Actualizar el valor de "Ciudad" para la ciudad de Chonchi, cambiándolo por "Ciudad de los Tres Pisos"
ciudades[5770000]["Ciudad"] = "Ciudad de los Tres Pisos" 

# E) Crear una lista llamada “lluvias” que contenga la precipitación de las tres ciudades.
lluvias = [ciudades[5700000]["Precipitacion"], ciudades[5770000]["Precipitacion"], ciudades[5790000]["Precipitacion"]]
suma_total = sum(lluvias)

# Mostrar la suma total de precipitaciones
print(f"La suma total de las Precipitaciones es de {suma_total}")
print("")

# Mostrar la mayor y menor precipitación
precipitacion_max = max(lluvias)
precipitacion_min = min(lluvias)
print(f"La precipitacion más alta es {precipitacion_max}")
print(f"La precipitacion más baja es {precipitacion_min}")
print("")

# Mostrar el índice (posición) de la precipitación más alta
lluvias[2]

# F) Casi terminando se imprime otra vez el diccionario completo con todos los cambios que se han hecho.
print(ciudades)
print("")

# G) Por ultimo obtener una lista de tuplas con las claves y valores del diccionario
print(ciudades.items())


