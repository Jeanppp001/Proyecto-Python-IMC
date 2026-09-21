# 1. Capturar datos desde el teclado con input()
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
peso = input("Ingresa tu peso (en kg): ")
estatura = input("Ingresa tu estatura (en metros, ej. 1.75): ")

# 2. Casting (conversión de tipos)
edad = int(edad)              # edad → entero
peso = float(peso)            # peso → flotante
estatura = float(estatura)    # estatura → flotante

# 3. Aplicar la fórmula del IMC: IMC = peso / estatura²
imc = peso / (estatura ** 2)

# Mostrar resultados
print("\n--- Resultados ---")
print(f"Nombre:   {nombre}")
print(f"Edad:     {edad} años")
print(f"Peso:     {peso} kg")
print(f"Estatura: {estatura} m")
print(f"IMC:      {imc:.2f}")

# Clasificación del IMC
if imc < 18.5:
    clasificacion = "Bajo peso"
elif imc < 25:
    clasificacion = "Peso normal"
elif imc < 30:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

print(f"Clasificación: {clasificacion}")






