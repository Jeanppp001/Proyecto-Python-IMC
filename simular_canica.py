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


# Ejemplo de uso
if __name__ == "__main__":
    # Simulación con valor por defecto (12 niveles)
    resultado = simular_canica()
    print(f"La canica cayó en el contenedor: {resultado}")
    
    # Simulación con parámetro personalizado
    resultado2 = simular_canica(niveles=8)
    print(f"Con 8 niveles, la canica cayó en el contenedor: {resultado2}")