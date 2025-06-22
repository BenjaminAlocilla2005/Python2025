# Nombres de los Integrantes: Benjamin Alocilla y Ana Villegas

# primero usar def, nombrar la variable como factorial, usar parentesis y dos puntos
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Ejemplo de uso
numero = int(input("Inserta un numero: "))
print(f"El factorial de {numero} es {factorial(numero)}")