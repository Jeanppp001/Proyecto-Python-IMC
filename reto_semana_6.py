#======================================================================
# Reto de la semana 6 Fundamento de Python while , for, if, elif, else
#======================================================================

#======================================================================
## Objetivo:
# Asegurar la integridad de los datos de entrada
# mediante ciclos while que fuercen al usuario
# a introducir valores válidos.
## Entregable 
# Asegurar la integridad de los datos de entrada
# mediante ciclos while que fuercen al usuario
# a introducir valores válidos.
#======================================================================

print("Programa de Coordenadas")

#ciclo para pedir la cordenada X

while True:
    try:
        x = float(input("Ingrese la coordenada X: "))
        if x == 0:
            print("La coordenada X no puede ser 0, por favor ingrese un valor válido.")
        else:
            break # dato valido, salimos del ciclo
    except ValueError:
        print("Error: Debe ingresar un número válido para la coordenada X.")

#ciclo para pedir la cordenada Y

while True:
    try:
        y = float(input("Ingrese la coordenada Y: "))
        if y == 0:
            print("La coordenada Y no puede ser 0, por favor ingrese un valor válido.")
        else:
            break # dato valido, salimos del ciclo
    except ValueError:
        print("Error: Debe ingresar un número válido para la coordenada Y.")



# punto adicional agregare la validacion en que cuadrante se encuentra en la cordenada ingresada}

if x > 0 and y > 0:
    print("La coordenada ingresada se encuentra en el primer cuadrante.") 
elif x < 0 and y > 0:
    print("La coordenada ingresada se encuentra en el segundo cuadrante.")
elif x < 0 and y < 0:
    print("La coordenada ingresada se encuentra en el tercer cuadrante.")
else:
    print("La coordenada ingresada se encuentra en el cuarto cuadrante.")


print(f"Las coordenadas ingresadas son: ({x}, {y})")