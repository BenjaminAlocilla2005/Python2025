num = 0
while num <= 200:
    print(num)
    num += 2
else:
    print("Mi condición es igual o mayor a 200")

while True:
    parametro = input("> ")
    if parametro == "exit":
        break
    else:
        print(parametro)
    
n = 0
while n <= 50:
    n += 1
    if n == 40:
        continue
    print(n)

nueva_lista = [1,2,3,4,5,6,7,8,9,10]
for i in nueva_lista:
    print(i)

for i in range(1,11,2):
    print(i)

for n in range(2,10):
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} es un número compuesto, divisible por {i}")
    else:
        print(f"{n} es un número primo")

matriz = [
    [1, 2, 3], # Fila 1
    [4, 5, 6], # Fila 2
    [7, 8, 9]  # Fila 3
]  #c0 #c1 #c2
for fila_id, fila in enumerate(matriz):
    for col_id, valor in enumerate(fila):
        print(f"Posición ({fila_id},{col_id}) = {valor}")