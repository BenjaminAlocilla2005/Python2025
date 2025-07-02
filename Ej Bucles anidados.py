def suma_columnas(matriz):
    suma_filas = [sum(fila) for fila in matriz]

    n_columnas = len(matriz[0]) if matriz else 0
    s_columnas = [0] * n_columnas

    for fila in matriz:
        for j in range(n_columnas):
            s_columnas[j] += fila[j]

    for i, suma in enumerate(suma_filas):
        print(f"Suma de fila {i}: {suma}")

    for j, suma in enumerate(suma_filas):
        print(f"Suma de columna {j}: {suma}")


lista_matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]
]

suma_columnas(lista_matriz)