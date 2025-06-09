'''
2. Desarrollar un algoritmo con operaciones mixtas con números complejos:
A. Ingresar tres valores numéricos diferentes (entero, flotante y complejo)
B. Calcular y mostrar:
● Potencia Compleja (Complejo y Entero)
● Suma Mixta (Complejo y Flotante)
● Producto Mixto (Complejo y Entero)
● Módulo de Potencia Compleja. El módulo se realiza utilizando la función abs()
(Variable Potencia Compleja, con 3 decimales)
'''
NE = int(input("Ingresa un numero entero: "))

NF = float(input("Ingresa un numero flotante: "))

NC = complex(input("Ingresa un numero complejo (ej : 3+4j) "))

Potencia_Compleja = (NE**NC)

Suma_Mixta = (NC + NF)

Producto_Mixto = (NC + NE)

mod_potencia = abs(Potencia_Compleja)

#prints
print(                       )
"            "
"            "
print(f"{Potencia_Compleja:.3f}")