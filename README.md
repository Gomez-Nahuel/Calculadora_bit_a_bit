# Calculadora Bit a Bit

Trabajo práctico realizado para Matemática 1 en conjunto con Programación 1 para la carrera de Tecnicatura en Programación a Distancia de la Universidad Nacional Tecnológica ( TUPaD - UTN ).

- COMISION: M2025-14
- ALUMNOS:
  * Javier Gonzalez
  * Federico Esteban Garcia
  * Nahuel Gomez
  * Alexis Gomez Gonzalez
  * Federico Garcia Bengolea

Una calculadora diseñada para realizar operaciones bit a bit y verificar el funcionamiento de las compuertas lógicas **AND**, **OR** y **XOR**.

<!-- INSERTAR VIDEO DE PRESENTACIÓN -->

## Características

- **Operación AND:** Produce una salida de 1 (verdadero) solo si todas las entradas son 1.
Es como decir "Ambas condiciones deben cumplirse".
- **Operación OR:** Genera una salida de 1 si al menos una de las entradas es 1.
Es como decir "Una u otra condición puede cumplirse".
- **Operación XOR:** La salida es 1 únicamente si las entradas son diferentes (una es 1 y la otra 0).
Es como decir "Solo una condición puede cumplirse, pero no ambas".

## ¿Cómo funciona?

1. **Menu de ingreso**: Se inicia el programa con un menu opcional.
2. **Entrada de datos:** El usuario introduce dos números en formato decimal.
3. **Conversión a binario:** Los números son convertidos a su representación binaria.
4. **Operaciones:** Se ejecutan las compuertas lógicas AND, OR y XOR que haya elegido el usuario sobre los números binarios.
5. **Resultado:** Los resultados de cada operación son mostrados por consola.

### Descripción de proyecto y objetivo
Calculadora bit a bit. Esta calculadora convierte números en base 10 a números en base 2 con el fin de obtener un número en base 2 resultante de la operación de una determinada compuerta utilizando como valor de entrada a la misma los bits de igual peso de cada uno de los números ingresados inicialmente.
Para poder realizar la aplicación no solo fue necesario conocimiento sobre Python, sino que además tuvimos que aplicar conocimientos adquiridos en la materia matemática. Procedimientos como el cambio de base de un número y la operación propia de cada compuerta utilizada por la aplicación fueron parte fundamental para la realización del mismo.
### Forma de trabajo
Utilizamos mayormente la metodología de `pair programming`. Utilizamos esta metodología con el fin de poder conocernos como equipo y para que cada uno pudiera aportar puntos de vista en tiempo real al momento de desarrollo.
Decidimos estructurar la aplicación con un archivo que contiene una función `calculadora` la cual es la encargada de integrar las diferentes funciones que componen esta calculadora. Adicionalmente tenemos un archivo llamado `functions` el cual contiene las definiciones de todas las funciones utilizadas por la calculadora para funcionar. También incorporamos la librería `colorama` que nos permite formatear los mensajes de salida a la terminal.
### Descripción de funcionamiento
La calculadora invoca la función calculadora la cual llama inicialmente a la funcion que muestra el menú al usuario. Una vez que el usuario selecciona la opción de la compuerta que desea utilizar se le piden los números a evaluar los cuales deben ser enteros para que se pueda avanzar.
La función `calculadora` inicialmente utiliza la funición `convertir_a_binario` para posteriormente ingresarlos como parámetro de las funciones que hacen las operaciones. Estas funciones utilizan otra funcion llamada `emparejar_largo` para poder operar bit a bit. Posteriomente el resultado en binario se pasa a decimal con la funcion `convertir_a_decimal`.
