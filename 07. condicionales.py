edad = 19

if edad >= 18 and edad < 65:
    print("Eres mayor de edad")
elif edad >= 65:
    print("Eres un adulto mayor")
else:
    print("Eres menor de edad")
print("Este print esta fuera del if")

print("Usted puede votar" if edad >= 18 else "Usted no puede votar")


licencia = False
edad = 19
automovil = False

print(">>> Testeando los comparadores y el IF")
if licencia:
    print("Puedo conducir por tengo licencia")
else:
    print("No tengo licencia para conducir")

print(">>> Utilizando el segundo condicional IF")
if edad >= 18:
    print("Soy mayor de edad")
else:
    print("No puedo conducir porque soy menor de edad")

print(">>> Utilizando el tercer condicional IF")
if automovil:
    print("Tengo automovil")
else:
    print("No tengo automovil")