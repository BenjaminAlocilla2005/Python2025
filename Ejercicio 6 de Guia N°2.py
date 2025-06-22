# Nombres de los Integrantes: Benjamin Alocilla y Ana Villegas

# para simular el comportamiento del reloj primero usamos def

# luego debemos usar for, in y range 3 veces y poner primero las horas, luego los minutos y por ultimo los segundos
def reloj_digital():
    for hora in range(24): 
        for minuto in range(60):
            for segundo in range(60):
                print(f"{hora:02d}:{minuto:02d}:{segundo:02d}") # por ultimo se debe de usar un print y usar 3 corchetes donde se pone la hora, el minuto y los segundos, tambien poner dentro de estos :02d

print("Reloj sin pausas")
reloj_digital()