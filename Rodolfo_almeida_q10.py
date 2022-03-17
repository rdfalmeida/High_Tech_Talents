# Exercício 10
# Faça um programa que peça a temperatura em graus Celsius,
# transforme e mostre em graus Fahrenheit. °F=(°C×9/5)+32

import math

temp_fahrenheit = float(input("Type the temperature in Fahrenheit(Fº): "))
temp_celsius = 5*((temp_fahrenheit-32)/9)
rounded_celsius = round(temp_celsius, 2)

print("This temperature equivalent in Celsius:", rounded_celsius)