# Exercício 9
# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e 
# mostre a temperatura em graus Celsius.  °C=5×((°F−32)/9)

import math

temp_celsius = float(input("Type the temperature in Celsius (Cº): "))
temp_fahrenheit = (temp_celsius *9/5) + 32
rounded_fahrenheit = round(temp_fahrenheit, 2)

print("This temperature equivalent in Fahrenheit:", rounded_fahrenheit)