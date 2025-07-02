def dividir_numeros():
    try:
        # Solicitar dos numeros para poder dividirlos
        n1 = float(input("Ingresa el primer numero: "))
        n2 = float(input("Luego el segundo: "))

        resultado = n1/n2
        print(f"El resultado de la division es: {resultado:.2f}")

    except ValueError:
           print("¡Error! debes ingresar números")
    except ZeroDivisionError:
           print("¡Error! no se puede dividir entre 0")
    except Exception as e:
           print(f"Ocurrio un error que no se esperaba: {e}")
    finally:
           print("Fin del programa")

#Llama a la funcion
dividir_numeros()
    