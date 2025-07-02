print("====== MENÚ ======")
print("1. Hamburguesa")
print("2. Pizza")
print("3. Completo Italiano")

opción = input("Por favor, elige una opción (1-3): ")

match opción:
    case "1":
        print("Has elegido una Hamburguesa: Precio: $5000")
    case "2":
        print("Has elegido Pizza: Precio $7500")
    case "3":
        print("Has elegido Completo: Precio $2500")
    case _:
        print("Opcion no valida. Por favor, elige entre 1 y 3")


mes = 4
match mes:
    case 12 | 1 | 2:
        print("Verano")
    case 3 | 4 | 5:
        print("Otoño")
    case 6 | 7 | 8:
        print("Invierno")
    case 9 | 10 | 11:
        print("Primavera")
    case _:
        print("Mes invalido")

hora = 18
match hora:
    case h if 0 <= h < 6:
        print("Buenas madrugadas")
    case h if 6 <= h < 12:
        print("Buenos dias")
    case h if 12 <= h < 18:
        print("Buenas tardes")
    case h if 18 <= h < 24:
        print("Buenas noches")
    case _:
        print("Hora invalida")

x = [1,2,3]
match x:
    case [a, b, c]:
        print(f"Elementos de la lista x: {a}, {b}, {c}")

datos = {
    "nombre" : "Benja",
    "edad" : 19
    }

match datos:
    case {"nombre": n, "edad": e}:
        print(f"nombre: {n}, edad: {e}")

valor = 6
match valor:
    case x if x % 2 == 0:
        print(f"{valor} es un número Par")
    case x if x % 2 != 0:
        print(f"{valor} es un número Impar")