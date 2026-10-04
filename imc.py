# 1. Capturar datos desde el teclado con input()
#nombre = input("Ingresa tu nombre: ")
#edad = input("Ingresa tu edad: ")
#peso = input("Ingresa tu peso (en kg): ")
#estatura = input("Ingresa tu estatura (en metros, ej. 1.75): ")

# 2. Casting (conversión de tipos)
#edad = int(edad)              # edad → entero
#peso = float(peso)            # peso → flotante
#estatura = float(estatura)    # estatura → flotante

# 3. Aplicar la fórmula del IMC: IMC = peso / estatura²
#imc = peso / (estatura ** 2)

# Mostrar resultados
#print("\n--- Resultados ---")
#print(f"Nombre:   {nombre}")
#print(f"Edad:     {edad} años")
#print(f"Peso:     {peso} kg")
#print(f"Estatura: {estatura} m")
#print(f"IMC:      {imc:.2f}")

# Clasificación del IMC
#if imc < 18.5:
#    clasificacion = "Bajo peso"
#elif imc < 25:
    #clasificacion = "Peso normal"
 #elif imc < 30:
    #clasificacion = "Sobrepeso"
#else:
   # clasificacion = "Obesidad"

#print(f"Clasificación: {clasificacion}")
#############################################Semana 3 cadenas de texto########################################################################################################

# 1. Capturar datos desde el teclado con input()
Primernombre = input("Ingresa tu primer nombre: ")
Segunonombre = input("Ingresa tu segundo nombre: ")
Primerapellido = input("Ingresa tu apellido paterno: ")
Segundoapellido = input("Ingresa tu apellido materno: ")
edad = input("Ingresa tu edad: ")
peso = input("Ingresa tu peso (en kg): ")
estatura = input("Ingresa tu estatura (en metros, ej. 1.75): ")

# 2. Casting (conversión de tipos)
edad = int(edad)              # edad → entero
peso = float(peso)            # peso → flotante
estatura = float(estatura)    # estatura → flotante

# 3. Aplicar la fórmula del IMC: IMC = peso / estatura²
imc = peso / (estatura ** 2)

# Se utiliza capitalizar() para mostrar los nombres y apellidos con la primera letra en mayúscula y el resto en minúscula
print(f"PrimerNombre:   {Primernombre.capitalize()}")
print(f"Segundo nombre: {Segunonombre.capitalize()}")
print(f"Primer apellido: {Primerapellido.capitalize()}")
print(f"Segundo apellido: {Segundoapellido.capitalize()}")
print(f"Edad:     {edad} años")
print(f"Peso:     {peso} kg")
print(f"Estatura: {estatura} m")
print(f"IMC:      {imc:.2f}")



