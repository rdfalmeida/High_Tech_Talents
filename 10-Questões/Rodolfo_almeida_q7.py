# Exercício 8
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

hourly_wage = float(input("Informe o valor de sua hora: "))
monthly_hours = float(input("Informe as horas trabalhadas no mês: "))

salary = hourly_wage * monthly_hours

print("O seu salário é R$:", salary)