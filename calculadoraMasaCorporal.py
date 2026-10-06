# Datos de la persona 

# --- NOMBRES Y APELLIDOS ---
# Validar textos (nombres/apellidos)
def validar_texto(valor, nombre_campo):
    texto_limpio = valor.strip()
    if not texto_limpio:
        raise ValueError(f"El {nombre_campo} no puede estar vacío.")
    
    # Quitamos los espacios
    if not texto_limpio.replace(" ", "").isalpha():
        raise ValueError(f"El {nombre_campo} solo puede contener letras y espacios.")
    return texto_limpio

primer_nombre = validar_texto(input("Ingrese su Primer Nombre: "), "primer nombre")
segundo_nombre = validar_texto(input("Ingrese su Segundo Nombre: "), "segundo nombre")
primer_apellido = validar_texto(input("Ingrese su Primer Apellido: "), "primer apellido")
segundo_apellido = validar_texto(input("Ingrese su Segundo Apellido: "), "segundo apellido")

print("Datos de nombre válidos.\n")


# EDAD, ALTURA Y PESO (Números) 

def validar_numero_positivo(valor, nombre_campo, es_decimal=False):
    try:
        # Intentamos convertir a float o int
        numero = float(valor) if es_decimal else int(valor)
        if numero <= 0:
            raise ValueError(f"El {nombre_campo} debe ser un número mayor a cero.")
        return numero
    except ValueError: raise ValueError(f"El {nombre_campo} debe ser un número válido y positivo.") # Si el usuario escribió letras, saltará este error

edad = validar_numero_positivo(input("Ingrese su Edad: "), "edad")
altura = validar_numero_positivo(input("Ingrese su Altura en metros: "), "altura", es_decimal=True)
peso = validar_numero_positivo(input("Ingrese su peso en kilogramos: "), "peso", es_decimal=True)

print("Datos físicos válidos.\n")

# Calculamos el índice de masa corporal (IMC)
imc = peso / (altura ** 2)

# Mostramos el resultado 
print("RESUMEN DE DATOS")
print(f"Primer Nombre:   {primer_nombre}")
print(f"Segundo Nombre:  {segundo_nombre}")
print(f"Primer Apellido: {primer_apellido}")
print(f"Segundo Apellido:{segundo_apellido}")
print(f"Edad:            {edad} años")
print(f"Altura:          {altura} metros")
print(f"Peso:            {peso} kg")
print(f"Su IMC es:       {imc:.2f}") # :.2f lo redondea a 2 decimales