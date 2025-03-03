# Cuatro en Raya - Python

Un juego clásico de "Cuatro en Raya" implementado en Python como parte de una experiencia de aprendizaje sobre programación orientada a objetos, manejo de excepciones y estructuras de control.

## Descripción del Proyecto

Este proyecto implementa el juego "Cuatro en Raya" utilizando clases y métodos en Python. Se enfoca en reforzar los conceptos de:

- **Programación Orientada a Objetos (POO)**: Uso de clases, encapsulación y atributos privados.
- **Manipulación de estructuras de datos**: Uso de listas anidadas para representar el tablero.
- **Gestión de errores**: Validaciones de entrada del usuario para evitar valores fuera de rango o incorrectos.
- **Interacción con el usuario**: Uso de `os.system()` y `time.sleep()` para mejorar la experiencia visual y hacer el juego más intuitivo.

## Características

- Juego para dos jugadores en consola.
- Representación visual del tablero.
- Manejo de errores y validación de entradas.
- Detección de ganador basado en filas, columnas y diagonales.

## Instalación y Ejecución

1. Clona este repositorio:
   ```sh
   git clone https://github.com/filazdev/juego_cuatro_en_raya.git
   ```
2. Accede al directorio del proyecto:
   ```sh
   cd cuatro-en-raya
   ```
3. Ejecuta el juego con:
   ```sh
   python cuatro_en_raya.py
   ```

Si prefieres ejecutar el juego como un archivo ejecutable, se han generado las carpetas `build` y `dist`, donde se encuentra el archivo `.exe` listo para su ejecución en sistemas Windows.

## Captura de Pantalla

![image](https://github.com/user-attachments/assets/ab103e0b-f859-4092-97fe-219be7b9dca8)



## Aprendizajes Clave

### 1. Programación Orientada a Objetos (POO)
- Uso de **clases** para estructurar el código.
- Métodos privados (`_metodo()`) para mantener la encapsulación.
- Creación de instancias de la clase `CuatroEnRaya`.

### 2. Manejo de Estructuras de Datos
- Uso de **listas anidadas** para representar el tablero.
- Iteraciones eficientes para verificar victorias.

### 3. Control de Flujo y Validación de Entradas
- Evitar que los jugadores seleccionen columnas llenas.
- Manejo de excepciones (`try-except`) para evitar errores con entradas no numéricas.

## Mejoras Futuras

- Implementación de una interfaz gráfica con Tkinter o Pygame.
- Modo de juego contra una IA con heurísticas básicas.
- Soporte para diferentes tamaños de tablero.

## Contribuciones

¡Si deseas mejorar este proyecto, siéntete libre de hacer un fork y enviar un pull request!
