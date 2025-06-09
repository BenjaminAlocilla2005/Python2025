'''
3. Crear un algoritmo que permita manipular cadenas de texto:
A. Ingresar una frase de máximo 30 caracteres.
B. Generar dos nuevas variables: una en mayúsculas y otra en minúsculas.
C. Utilizar un método propio para determinar cuántas veces aparece la letra «a» (tanto «a»
como «A») en la frase, y muestra el total.
D. Emplear otro método para imprimir la longitud de la frase original.
'''

Frase = str(input("Ingrese su frase: "))[0:30]
Mayusculas = Frase.upper()
Minusculas = Frase.lower()



Cantidad_de_a = Frase.count("a")
Cantidad_de_A = Frase.count("A")

print(Cantidad_de_a)
print(Cantidad_de_A)


