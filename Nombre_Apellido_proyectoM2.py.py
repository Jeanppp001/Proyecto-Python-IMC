"""
Proyecto Final - Módulo 2: Fundamentos de Python
Autor: [Tu Nombre y Apellido]
Fecha: 09 de noviembre de 2026

Descripción:
Este programa consolida los retos de la semana 6 (Coordenadas y Cuadrantes)
y la semana 7 (Clasificador de Palabras por Longitud) en un único menú 
interactivo, aplicando manejo de excepciones, estructuras de control y 
colecciones de datos.
"""

import sys


def reto_coordenadas():
    """
    Reto Semana 6: Coordenadas y Cuadrantes
    Solicita las coordenadas X e Y, valida que sean números distintos de cero 
    mediante ciclos while y try-except, y determina en qué cuadrante se encuentra.
    """
    print("\n" + "=" * 60)
    print("RETO 1: PROGRAMA DE COORDENADAS Y CUADRANTES")
    print("=" * 60)

    # Ciclo para asegurar la integridad de la coordenada X (Casting a float)
    while True:
        try:
            x = float(input("Ingrese la coordenada X: "))
            if x == 0:
                print("La coordenada X no puede ser 0, ingrese un valor válido.")
            else:
                break  # Dato válido, salimos del ciclo
        except ValueError:
            print("Error: Debe ingresar un número válido para la coordenada X.")

    # Ciclo para asegurar la integridad de la coordenada Y (Casting a float)
    while True:
        try:
            y = float(input("Ingrese la coordenada Y: "))
            if y == 0:
                print("La coordenada Y no puede ser 0, ingrese un valor válido.")
            else:
                break  # Dato válido, salimos del ciclo
        except ValueError:
            print("Error: Debe ingresar un número válido para la coordenada Y.")

    # Determinación del cuadrante usando estructuras if/elif/else
    if x > 0 and y > 0:
        cuadrante = "primer"
    elif x < 0 and y > 0:
        cuadrante = "segundo"
    elif x < 0 and y < 0:
        cuadrante = "tercer"
    else:
        cuadrante = "cuarto"

    print(f"\nLa coordenada ingresada ({x}, {y}) se encuentra en el {cuadrante} cuadrante.")


def reto_clasificador_palabras():
    """
    Reto Semana 7: Clasificador de Palabras
    Clasifica palabras en 4 cuadrantes según su longitud usando tuplas, 
    listas y diccionarios.
    """
    print("\n" + "=" * 60)
    print("RETO 2: CLASIFICADOR DE PALABRAS POR LONGITUD")
    print("=" * 60)

    # BLOQUE 1: DEFINICIÓN DE COLECCIONES
    # Tupla inmutable para los nombres de los cuadrantes
    CUADRANTES = ("Cuadrante I", "Cuadrante II", "Cuadrante III", "Cuadrante IV")
    
    # Lista mutable para el historial dinámico
    historial_palabras = []
    
    # Diccionario de resultados (clave-valor)
    registro_resultados = {
        CUADRANTES[0]: [],
        CUADRANTES[1]: [],
        CUADRANTES[2]: [],
        CUADRANTES[3]: []
    }
    
    # Diccionario de mensajes para centralizar textos (escalabilidad)
    mensajes_sistema = {
        "bienvenida": "--- Bienvenido al Clasificador de Palabras ---",
        "instruccion": "Ingresa palabras para clasificarlas. Escribe 'salir' para terminar.",
        "error_vacio": "Error: No puedes ingresar cadenas vacías.",
        "despedida": "Sesión finalizada. Generando reporte..."
    }

    # BLOQUE 2: LÓGICA DEL PROGRAMA
    print(mensajes_sistema["bienvenida"])
    print(mensajes_sistema["instruccion"])

    ejecutando = True
    while ejecutando:
        palabra_ingresada = input("\nPalabra: ")

        # Validación de salida
        if palabra_ingresada.lower() == 'salir':
            ejecutando = False
            continue

        # Validación de cadena vacía
        if palabra_ingresada.strip() == "":
            print(mensajes_sistema["error_vacio"])
            continue

        # Registro en historial (Uso de Lista)
        historial_palabras.append(palabra_ingresada)

        # Cálculo de índice usando el operador módulo (Uso de índices)
        longitud_palabra = len(palabra_ingresada)
        indice_cuadrante = longitud_palabra % 4

        # Acceso a la Tupla y al Diccionario
        nombre_cuadrante_asignado = CUADRANTES[indice_cuadrante]
        registro_resultados[nombre_cuadrante_asignado].append(palabra_ingresada)
        print(f"-> '{palabra_ingresada}' asignada a {nombre_cuadrante_asignado}")

    # BLOQUE 3: IMPRESIÓN DE RESULTADOS
    print("\n" + mensajes_sistema["despedida"])
    print(f"Total de palabras intentadas: {len(historial_palabras)}")

    for cuadrante, palabras in registro_resultados.items():
        print(f"\n{cuadrante} ({len(palabras)} palabras):")
        if palabras:
            for p in palabras:
                print(f"  - {p}")
        else:
            print("  (Sin palabras registradas)")


def menu_principal():
    """
    Menú principal para navegar entre los retos.
    """
    while True:
        print("\n" + "=" * 60)
        print("PROYECTO FINAL M2 - FUNDAMENTOS DE PYTHON")
        print("=" * 60)
        print("1. Reto Semana 6: Coordenadas y Cuadrantes")
        print("2. Reto Semana 7: Clasificador de Palabras")
        print("3. Salir")
        print("-" * 60)

        opcion = input("Seleccione una opción (1-3): ")

        if opcion == '1':
            reto_coordenadas()
        elif opcion == '2':
            reto_clasificador_palabras()
        elif opcion == '3':
            print("Gracias por usar el programa. ¡Hasta luego!")
            sys.exit()
        else:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")


if __name__ == "__main__":
    menu_principal()