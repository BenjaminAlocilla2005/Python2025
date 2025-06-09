""""
1. Crear un algoritmo que sirva de Conversor de Temperatura:
A. Solicitar por consola una temperatura en grados Celsius (números flotantes)
B. Calcular su equivalente en grados Fahrenheit y Kelvin utilizando las fórmulas
correspondientes.
C. Mostrar los tres valores en pantalla, redondeados a 2 decimales
"""

Grados_Celsius = float(input("Ingresa los grados Celsius: "))

Grados_Fahrenheit = (Grados_Celsius * 1.8) + 32

Grados_Kelvin = Grados_Celsius + 273.15

# Despues de Calcular los grados Celsius con sus equivalentes en grados Fahrenheit y Kelvin
# Vemos cuanto nos sale
print(round(Grados_Celsius,2))

print(round(Grados_Fahrenheit,2))

print(round(Grados_Kelvin,2))