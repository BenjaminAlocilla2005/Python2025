entrada = input("Ingrese un valor entero: ") # Valor ingresado es un str

try:
    numero = int(entrada)
    print(f"Número ingresado: {numero}")
except ValueError: # Error por tipo de dato
    print("Error de valor: el valor ingresado no es entero")
except Exception as e: # Errores genericos e inesperados
    print(f"Error inesperado: {e}")
else:
    print("Conversión exitosa!")


try:
    archivo = open("Documentos/Python-2025/holamundo.py")
    contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print("El archivo no existe.")
else:
    print("Lectura exitosa.")
finally:
    try:
        archivo.close()
        print("Archivo cerrado")
    except NameError:
        print("No fue necesario cerrar el archivo.")