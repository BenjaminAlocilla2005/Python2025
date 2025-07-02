# Lista vacia
frutas = []

# Lista de solo numeros
n = [1,2,3,4,5]

# Lista de solo strings
ramos = list(["Programación", "Quimica", "POO", "Programacion"])

# METODO COUNT
print(ramos.count("Programación"))

ramos.append("Matematicas")
print(ramos)

ramos[1] = "Comunicacion"
print(ramos)

# OTRA FORMA DE INSERTAR UN ELEMENTO A LA LISTA
ramos.insert(0,"Algebra")
print(ramos)

# ELIMINAR EL ULTIMO ELEMENTO DE LA LISTA
ramos.pop()
print(ramos)

# ORDENANDO ELEMENTO DE UNA LISTA DE FORMA DESCENDENTE A ASCENDENTE
print(ramos.sort())
ramos.sort()
print(ramos)

# ORDENANDO ELEMENTOS DE UNA LISTA SEGUN SU CANTIDAD DE CARACTERES
# Key es una propiedad del método sort y se pasa un valor que es el métoso len
ramos.sort(key=len)
print(ramos)

# OCUPANDO EL MÉTODO EXTEND
ramos.extend(n)
print(ramos)

ramitos = ["Calculo", "Automatas"]
print(ramitos)