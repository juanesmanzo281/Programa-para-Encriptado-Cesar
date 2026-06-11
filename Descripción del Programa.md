Cifrado César - Encriptador y Desencriptador en Python

Este proyecto es una aplicación interactiva por consola desarrollada en Python que implementa el clásico **Cifrado César**. Es una excelente demostración de lógica algorítmica, validación de datos por parte del usuario y modularización de código, ideal para formar parte de un portafolio de desarrollo de software.

El Cifrado César funciona desplazando cada letra del texto original un número fijo de posiciones hacia adelante o hacia atrás a lo largo del alfabeto.

## Características Principales

*   **Interfaz Interactiva por Consola:** Flujo guiado que pregunta dinámicamente si se desea codificar (`encode`) o decodificar (`decode`).
*   **Modularización del Código:** Separación limpia de responsabilidades. La lógica criptográfica reside en un módulo independiente, mientras que el flujo de interacción se maneja en el script principal.
*   **Soporte Completo en Español:** A diferencia de muchos algoritmos que solo contemplan el alfabeto inglés, este sistema incluye de forma nativa la letra **`ñ`**.
*   **Validación de Entradas Robusta:** Implementa bucles de control (`while True`) combinados con técnicas de limpieza de strings (`.lower().strip()`) para prevenir errores ante respuestas inesperadas del usuario.
*   **Ajuste de Desplazamiento Matemático:** Utiliza aritmética modular (`%`) para garantizar que desplazamientos mayores al tamaño del alfabeto (27 caracteres) den la vuelta correctamente sin romper el índice de la lista.

## Estructura del Proyecto

El repositorio está estructurado en dos scripts principales:

1.  **`funciones_y_alfabeto.py`**: El módulo lógico. Contiene el arreglo del alfabeto y define las funciones core:
    *   `encrypt(texto_original, espacio)`: Procesa strings y retorna su equivalente cifrado.
    *   `decrypt(encryptado, espacio)`: Revierte el cifrado con base en la clave numérica compartida.
2.  **`main.py`** *(Nombre recomendado para tu archivo principal)*: El motor del programa. Importa el módulo de funciones y controla los ciclos de ejecución continuos y menús de decisión.

## Tecnologías Utilizadas:

*   **Python 3.x** (Estructuras de control, manipulación de strings y listas, operaciones aritméticas).
*   **Git & GitHub** (Para el control de versiones y despliegue del portafolio).

## Instalación y Uso

Para ejecutar este proyecto de forma local en tu computadora, sigue estos pasos:

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/tu-usuario/cifrado-cesar-python.git
    ```

2.  **Navegar a la carpeta del proyecto:**
    ```bash
    cd cifrado-cesar-python
    ```

3.  **Ejecutar la aplicación:**
    ```bash
    python main.py
    ```

## Aprendizajes Clave Destacados:

Este desarrollo demuestra dominio sobre conceptos clave para un programador Junior:
*   **Aritmética Modular:** El uso de `(posicion + espacio) % tamaño_alfabeto` para prevenir errores de tipo `IndexError` fuera de los límites de la lista.
*   **Persistencia de Estado:** Uso de banderas booleanas (`fin = False`) para mantener o dar cierre a la sesión del programa por decisión del usuario.
*   **Sanitización de Datos:** Conversión estricta a minúsculas y eliminación de espacios en blanco sobrantes para asegurar la coincidencia exacta de datos.

---
*Desarrollado como parte de mi camino de aprendizaje en Fundamentos de Programación y Desarrollo de Software.*
