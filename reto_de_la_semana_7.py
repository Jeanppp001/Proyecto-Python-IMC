# ==============================================================================
# BLOQUE 1: DEFINICIÓN DE COLECCIONES (Listas, Tuplas y Diccionarios)
# ==============================================================================

# 1. TUPLA: Es inmutable (no puede cambiar). Es ideal para datos fijos como 
# los nombres de los cuadrantes, ya que garantiza que no se alterarán por error.
CUADRANTES = ("Cuadrante I", "Cuadrante II", "Cuadrante III", "Cuadrante IV")

# 2. LISTA: Es mutable y ordenada. La usaremos para almacenar el historial 
# dinámico de todas las palabras que el usuario intente ingresar.
historial_palabras = []

# 3. DICCIONARIO (Resultados): Estructura de clave-valor. Nos permite almacenar 
# los resultados agrupados por cuadrante. Es altamente escalable.
registro_resultados = {
    CUADRANTES[0]: [],
    CUADRANTES[1]: [],
    CUADRANTES[2]: [],
    CUADRANTES[3]: []
}

# 4. DICCIONARIO (Mensajes): Centraliza los mensajes del sistema. Si en el 
# futuro queremos cambiar un texto o agregar idiomas, solo editamos este diccionario.
mensajes_sistema = {
    "bienvenida": "--- Bienvenido al Clasificador de Palabras ---",
    "instruccion": "Ingresa palabras para clasificarlas. Escribe 'salir' para terminar.",
    "error_vacio": "Error: No puedes ingresar cadenas vacías.",
    "despedida": "Sesión finalizada. Generando reporte..."
}

# ==============================================================================
# BLOQUE 2: VARIABLES BÁSICAS (Tipos Primitivos)
# ==============================================================================


palabra_ingresada = ""       # Tipo: String (Cadena de texto)
ejecutando = True            # Tipo: Boolean (Verdadero/Falso para el bucle)
indice_cuadrante = 0         # Tipo: Integer (Número entero para el índice)
longitud_palabra = 0         # Tipo: Integer (Número entero)



# ==============================================================================
# BLOQUE 3: LÓGICA DEL PROGRAMA Y USO DE ÍNDICES
# ==============================================================================

# Accedemos al diccionario de mensajes para imprimir la bienvenida
print(mensajes_sistema["bienvenida"])
print(mensajes_sistema["instruccion"])

while ejecutando:
    # Pedimos datos al usuario (Variable primitiva: String)
    palabra_ingresada = input("\nPalabra: ")
    
    # Validación de salida
    if palabra_ingresada.lower() == 'salir':
        ejecutando = False
        continue
        
    # Validación de cadena vacía
    if palabra_ingresada.strip() == "":
        print(mensajes_sistema["error_vacio"])
        continue

    # --- USO DE LA LISTA ---
    # Agregamos la palabra al historial (Registro de intentos)
    historial_palabras.append(palabra_ingresada)
    
    # --- CÁLCULO Y ACCESO A LA TUPLA POR ÍNDICE ---
    # Calculamos la longitud de la palabra (Variable primitiva: int)
    longitud_palabra = len(palabra_ingresada)
    
    # Usamos el operador módulo (%) para obtener un índice entre 0 y 3
    indice_cuadrante = longitud_paladrante = longitud_palabra % 4 
    
    # Accedemos a la TUPLA mediante su índice para obtener el nombre exacto
    nombre_cuadrante_asignado = CUADRANTES[indice_cuadrante]
    
    # --- USO DEL DICCIONARIO DE RESULTADOS ---
    # Guardamos la palabra en la lista correspondiente dentro del diccionario
    registro_resultados[nombre_cuadrante_asignado].append(palabra_ingresada)
    
    print(f"-> '{palabra_ingresada}' asignada a {nombre_cuadrante_asignado}")

# ==============================================================================
# BLOQUE 4: IMPRESIÓN DE RESULTADOS (Escalabilidad)
# ==============================================================================
print("\n" + mensajes_sistema["despedida"])
print(f"Total de palabras intentadas: {len(historial_palabras)}")

# Iteramos sobre el diccionario de resultados para mostrar un reporte escalable
for cuadrante, palabras in registro_resultados.items():
    print(f"\n{cuadrante} ({len(palabras)} palabras):")
    if palabras:
        for p in palabras:
            print(f"  - {p}")
    else:
        print("  (Sin palabras registradas)")