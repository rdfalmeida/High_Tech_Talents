# Exercício 6
# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

raio_circulo = float(input("Informe o raio do círculo: "))
area_circulo = math.pi*raio_circulo**2

print("A área do círculo é:", round(area_circulo, 4))