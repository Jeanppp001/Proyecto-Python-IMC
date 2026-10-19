# ==========================================
# PARTE 1: Validación de longitud de palabra
# ==========================================
print("--- VALIDACIÓN DE PALABRA ---")
palabra = input("Ingresa una palabra: ")

# Criterio: Se utiliza la función len() para obtener la longitud N
longitud = len(palabra) 

# Estructura if-elif-else para determinar si tiene entre 4 y 8 letras
if longitud < 4:
    # Criterio: Identifica correctamente palabras con menos de 4 letras
    print(f"Hacen falta letras. Tu palabra tiene {longitud} letras (mínimo 4).")
elif longitud > 8:
    # Criterio: Identifica correctamente palabras con más de 8 letras
    print(f"Sobran letras. Tu palabra tiene {longitud} letras (máximo 8).")
else:
    # Mensaje claro para el caso correcto (entre 4 y 8 letras)
    print("Palabra correcta.")


# ==========================================
# PARTE 2: Determinación de cuadrante
# ==========================================
print("\n--- DETERMINACIÓN DE CUADRANTE ---")
# Se solicitan dos números (se usan float para permitir decimales)
x = float(input("Ingresa el primer número (Coordenada X): ")) # la variable x representa la coordenada X y el float permite que el usuario ingrese números decimales    
y = float(input("Ingresa el segundo número (Coordenada Y): ")) # la variable y representa la coordenada Y y el float permite que el usuario ingrese números decimales

# Estructura condicional basada en si son mayores o menores a cero
if x > 0 and y > 0:
    print("El punto se encuentra en el Cuadrante I (+, +).")
elif x < 0 and y > 0:
    print("El punto se encuentra en el Cuadrante II (-, +).")
elif x < 0 and y < 0:
    print("El punto se encuentra en el Cuadrante III (-, -).")
elif x > 0 and y < 0:
    print("El punto se encuentra en el Cuadrante IV (+, -).")
else:
    # Manejo del caso donde alguno o ambos números son exactamente cero (ejes)
    print("El punto se encuentra sobre un eje (no pertenece a ningún cuadrante)")