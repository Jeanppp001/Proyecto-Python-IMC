# Proyecto Final Módulo 2 - Fundamentos de Python

**Autor:** [Tu Nombre y Apellido]  
**Fecha:** 09 de noviembre de 2026  
**Entorno de Desarrollo:** IntelliJ IDEA / VS Code

## 📌 Descripción del Proyecto
Este repositorio contiene la entrega final del Módulo 2, donde se consolidan los conocimientos adquiridos sobre estructuras de control, manejo de excepciones, casting de datos y colecciones en Python. El programa unifica dos retos principales en una sola aplicación con menú interactivo:

1. **Reto de Coordenadas (Semana 6):** Validación de entrada de datos numéricos (X, Y) mediante ciclos `while` y bloques `try-except`, determinando el cuadrante cartesiano al que pertenecen.
2. **Clasificador de Palabras (Semana 7):** Uso de Tuplas, Listas y Diccionarios para clasificar palabras dinámicamente en 4 "cuadrantes" basados en la longitud de la cadena de texto.

## 🚀 Instrucciones de Uso
1. Clona este repositorio en tu máquina local.
2. Ejecuta el archivo `Nombre_Apellido_proyectoM2.py` desde tu terminal o IDE.
3. Selecciona la opción `1` o `2` en el menú para ejecutar el reto deseado.
4. Sigue las instrucciones en pantalla. En el Reto 1, el sistema te impedirá avanzar si ingresas letras o ceros. En el Reto 2, escribe la palabra `salir` para generar el reporte final.

## 🧠 Reflexión sobre las Estructuras de Control
El uso de estructuras de control ha sido fundamental para transformar mi lógica de programación de una ejecución lineal a una **ejecución inteligente y defensiva**. 

- **Ciclos `while` con `try-except`:** Me permitieron entender que no podemos confiar ciegamente en la entrada del usuario. Al forzar un ciclo hasta que el dato sea válido (casting correcto a `float`), garantizamos la **integridad de los datos** y evitamos que el programa colapse (crashee) ante un error.
- **Condicionales `if/elif/else`:** Fueron el motor para la toma de decisiones, permitiendo que el programa reaccione de forma distinta según el contexto (ej. saber en qué cuadrante caerá un punto o una palabra).
- **Colecciones de Datos:** Comprender la diferencia entre la inmutabilidad de una **Tupla** (ideal para datos fijos como los nombres de los cuadrantes) y la flexibilidad de una **Lista** y un **Diccionario** (ideales para acumular datos dinámicos y relacionarlos mediante claves) me dio las herramientas para diseñar programas escalables y fáciles de mantener en el futuro.

En conclusión, estas estructuras no solo organizan el código, sino que lo hacen robusto, escalable y profesional.