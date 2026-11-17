import random

def simular_canica(niveles=12):
    """
    Simula el recorrido de una canica a través de los niveles de obstáculos 
    (tipo tablero de Galton), decidiendo aleatoriamente en cada nivel si la 
    canica cae a la izquierda o a la derecha.
    
    Args:
        niveles (int, optional): Número de niveles u obstáculos que atraviesa 
                                 la canica. Por defecto es 12.
                                 
    Returns:
        int: El índice del contenedor final donde termina la canica (0 a niveles).
    """
    contenedor_final = 0
    
    # Simula la caída de la canica por cada nivel
    for _ in range(niveles):
        # 0 = izquierda (no suma), 1 = derecha (suma 1)
        direccion = random.randint(0, 1)
        contenedor_final += direccion 
        
    return contenedor_final


def ejecutar_simulacion_masiva(num_canicas=3000, **kwargs):
    """
    Ejecuta la simulación de múltiples canicas y almacena los resultados.
    
    Args:
        num_canicas (int): Número de canicas a simular. Por defecto 3000.
        **kwargs: Argumentos adicionales para pasar a simular_canica 
                  (ej: niveles=8)
    
    Returns:
        list: Lista con los contenedores finales de todas las canicas simuladas.
    """
    resultados = []
    
    # Bucle de 3,000 repeticiones
    for i in range(num_canicas):
        # Llama a simular_canica y almacena su valor de retorno
        contenedor = simular_canica(**kwargs)
        resultados.append(contenedor)
    
    return resultados


def mostrar_estadisticas(resultados):
    """
    Muestra estadísticas básicas de los resultados de la simulación.
    
    Args:
        resultados (list): Lista de contenedores finales.
    
    Returns:
        dict: Diccionario con estadísticas calculadas.
    """
    total = len(resultados)
    minimo = min(resultados)
    maximo = max(resultados)
    
    # Calcular distribución por contenedor
    distribucion = {}
    for contenedor in resultados:
        distribucion[contenedor] = distribucion.get(contenedor, 0) + 1
    
    estadisticas = {
        'total_canicas': total,
        'contenedor_minimo': minimo,
        'contenedor_maximo': maximo,
        'distribucion': distribucion
    }
    
    return estadisticas


# --- Bloque principal de ejecución ---
if __name__ == "__main__":
    print("=" * 60)
    print("SIMULACIÓN MASIVA DE CANICAS - TABLERO DE GALTON")
    print("=" * 60)
    
    # 1. Ejecutar simulación con 3,000 canicas (usando valor por defecto de 12 niveles)
    print("\n🎯 Simulando 3,000 canicas con 12 niveles...")
    resultados_3000 = ejecutar_simulacion_masiva(num_canicas=3000)
    
    # 2. Mostrar que se generaron exactamente 3,000 resultados
    print(f"✅ Total de resultados generados: {len(resultados_3000)}")
    
    # 3. Mostrar primeros 20 resultados como ejemplo
    print(f"\n📋 Primeros 20 resultados: {resultados_3000[:20]}")
    
    # 4. Obtener y mostrar estadísticas
    stats = mostrar_estadisticas(resultados_3000)
    print(f"\n📊 Estadísticas:")
    print(f"   - Contenedor mínimo: {stats['contenedor_minimo']}")
    print(f"   - Contenedor máximo: {stats['contenedor_maximo']}")
    
    # 5. Mostrar distribución (cuántas canicas cayeron en cada contenedor)
    print(f"\n📈 Distribución de canicas por contenedor:")
    for contenedor in sorted(stats['distribucion'].keys()):
        cantidad = stats['distribucion'][contenedor]
        porcentaje = (cantidad / stats['total_canicas']) * 100
        barra = "█" * int(porcentaje / 2)
        print(f"   Contenedor {contenedor:2d}: {cantidad:4d} canicas ({porcentaje:5.2f}%) {barra}")
    
    # 6. Ejemplo adicional: simulación con diferente número de niveles usando **kwargs
    print("\n" + "=" * 60)
    print("🎯 Simulación adicional con 8 niveles (usando **kwargs)...")
    resultados_8_niveles = ejecutar_simulacion_masiva(num_canicas=1000, niveles=8)
    stats_8 = mostrar_estadisticas(resultados_8_niveles)
    print(f"✅ Total de resultados: {len(resultados_8_niveles)}")
    print(f"   - Rango de contenedores: {stats_8['contenedor_minimo']} a {stats_8['contenedor_maximo']}")
    
    print("\n" + "=" * 60)
    print("¡Simulación completada exitosamente!")
    print("=" * 60)