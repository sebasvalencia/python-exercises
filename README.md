

# Ejercicios de Python
### Español
Este repositorio contiene ejercicios de programación en Python, del diplomado de Machine Learning en Python de la Universidad EAFIT, organizados de manera modular y con tests completos.


## Nivel básico

1. Pide al usuario dos números. Imprime cuál de los dos números es mayor. Si son iguales, imprímelo. 
   ```py 
   compare_numbers.py
   test_compare_numbers.py
   ```
2. Pide al usuario una letra. Si es una vocal (a, e, i, o, u), imprime "Es una vocal". De lo contrario, imprime "No es una vocal". (Considera solo minúsculas).
3. Pide al usuario un número entero. Determina si es par o impar.

## Nivel intermedio

1. Pide al usuario tres números. Imprime cuál de los tres es el mayor.
2 .Pide al usuario un año. Determina si es un año bisiesto o no. (Un año es bisiesto si es divisible por 4, a menos que sea divisible por 100 pero no por 400).
3. Pide al usuario la temperatura en grados Celsius. Si la temperatura es mayor a 25, imprime "Hace calor". Si está entre 10 y 25 (inclusive), imprime "El clima es agradable". Si es menor a 10, imprime "Hace frío".
4. Pide al usuario el nombre de un día de la semana (en minúsculas). Determina si es un día laboral (lunes a viernes) o fin de semana (sábado o domingo).

## Nivel Avanzado

1. Simula una calculadora simple. Pide al usuario dos números y una operación (+, -, *, /). Realiza la operación correspondiente y muestra el resultado. Maneja el caso de división por cero.
2. Pide al usuario tres longitudes de lados. Determina si pueden formar un triángulo válido y, si es así, qué tipo de triángulo es (equilátero, isósceles o escaleno). (Para formar un triángulo válido, la suma de las longitudes de dos lados debe ser mayor que la longitud del tercer lado).
3. Simula un sistema de descuento basado en la cantidad de compra. Pide al usuario el total de la compra. Aplica los siguientes descuentos:
- Compras mayores a 1000: 20% de descuento
- Compras entre 500 y 1000 (inclusive): 10% de descuento
- Compras menores a 500: Sin descuento Imprime el precio final después del descuento.
  
4. Pide al usuario un año y un mes (como número, del 1 al 12). Determina cuántos días tiene ese mes. (Considera el año bisiesto para febrero).
5. Simula un sistema de tarifas de envío basado en el peso de un paquete y la zona de destino. Pide al usuario el peso del paquete (en kg) y la zona de destino ("local", "nacional", "internacional"). Calcula el costo de envío según las siguientes reglas:
- Local: 5usd por kg
- Nacional: 10usd por kg (mínimo 15usd)
- Internacional: 20usd por kg (mínimo 50usd) Si el peso es negativo o la zona no es válida, muestra un mensaje de error.

### English
Python Exercises
This repository contains Python programming exercises from the Machine Learning in Python diploma program at EAFIT University, organized in a modular format and with complete tests.

## Basic Level

1. Ask the user for two numbers. Print which of the two numbers is greater. If they are equal, print it.
```py 
   compare_numbers.py
   test_compare_numbers.py
   ```
2. Ask the user for a letter. If it is a vowel (a, e, i, o, u), print "It is a vowel." Otherwise, print "It is not a vowel." (Only considers lowercase letters.)
3. Ask the user for an integer. Determine if it is odd or even.

## Intermediate Level

1. Ask the user for three numbers. Print which of the three is greater.
2. Ask the user for a year. Determine whether it is a leap year or not. (A year is a leap year if it is divisible by 4, unless it is divisible by 100, but not by 400.)
3. Ask the user for the temperature in degrees Celsius. If the temperature is greater than 25, print "It's hot." If it's between 10 and 25 (inclusive), print "The weather is nice." If it's less than 10, print "It's cold."
4. Ask the user for the name of a day of the week (in lowercase). Determine if it's a weekday (Monday to Friday) or a weekend (Saturday or Sunday).

## Advanced Level

1. Simulate a simple calculator. Ask the user for two numbers and an operation (+, -, *, /). Perform the corresponding operation and display the result. Handle division by zero.
2. Ask the user for three side lengths. Determine if they can form a valid triangle and, if so, what type of triangle it is (equilateral, isosceles, or scalene). (To form a valid triangle, the sum of the lengths of two sides must be greater than the length of the third side.)
3. Simulate a discount system based on purchase quantity. Ask the user for the total purchase. Apply the following discounts:
- Purchases over 1000: 20% discount
- Purchases between 500 and 1000 (inclusive): 10% discount
- Purchases under 500: No discount. Print the final price after the discount.

4. Ask the user for a year and month (as numbers, from 1 to 12). Determine how many days there are in that month. (Consider leap year for February.)
5. Simulate a shipping rate system based on the weight of a package and the destination zone. Ask the user for the weight of the package (in kg) and the destination zone ("local," "national," "international"). Calculate the shipping cost according to the following rules:
- Local: USD 5 per kg
- National: USD 10 per kg (minimum USD 15)
- International: USD 20 per kg (minimum USD 50) If the weight is negative or the zone is invalid, an error message will appear.
