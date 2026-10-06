# Calculadora de IMC con Validación de Datos

Este es un script de Python diseñado para recopilar datos personales y físicos de un usuario a través de la terminal. Destaca por su **robusto sistema de validación de entradas**, asegurando que los datos ingresados sean correctos antes de procesarlos, y finaliza calculando e imprimiendo el **Índice de Masa Corporal (IMC)**.

## Características

- **Validación de Textos (Nombres/Apellidos):** 
  - Asegura que los campos no estén vacíos ni contengan solo espacios.
  - Rechaza números y caracteres especiales, permitiendo únicamente letras y espacios (ideal para nombres compuestos como "Juan Carlos").
- **Validación de Números (Edad, Altura, Peso):**
  - Previene que el programa colapse si el usuario ingresa texto en campos numéricos.
  - Asegura que todos los valores físicos sean números positivos y mayores a cero.
  - Diferencia entre números enteros (edad) y decimales (altura y peso).
- **Cálculo Automático:** Calcula el IMC utilizando la fórmula estándar: `peso / (altura²)`.
- **Salida Formateada:** Muestra un resumen limpio y estructurado utilizando *f-strings*, redondeando el IMC a 2 decimales.

## Requisitos

- **Python 3.6 o superior** (necesario para el uso de *f-strings*).

No requiere ninguna librería externa, utiliza únicamente las funciones integradas (built-in) de Python.

## Cómo ejecutar

1. Clona o descarga el archivo en tu computadora.
2. Abre tu terminal o consola de comandos.
3. Navega hasta la carpeta donde guardaste el script.
4. Ejecuta el siguiente comando:

---Datos de Entrada---
Ingrese su Primer Nombre: Juan
Ingrese su Segundo Nombre: Carlos
Ingrese su Primer Apellido: Perez
Ingrese su Segundo Apellido: Gomez
Datos de nombre válidos.

Ingrese su Edad: 25
Ingrese su Altura en metros: 1.75
Ingrese su peso en kilogramos: 70
Datos físicos válidos.

---Dato de salida por la terminañ---
RESUMEN DE DATOS
Primer Nombre:   Juan
Segundo Nombre:  Carlos
Primer Apellido: Perez
Segundo Apellido:Gomez
Edad:            25 años
Altura:          1.75 metros
Peso:            70 kg
Su IMC es:       22.86