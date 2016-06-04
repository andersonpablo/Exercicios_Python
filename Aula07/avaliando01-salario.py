# -*- coding: utf-8 -*-

# 1. Suponha que um funcionário ganha R$ 800,00 por semana por 30 horas de trabalho. Esse mesmo funcionário recebe
# R$ 150,00 para cada hora extra de trabalho durante a semana, sendo que ele pode trabalhar no máximo até 40 horas.
# Faça um programa que receba a quantidade de horas trabalhas por um funcionário (horas >= 30 e horas <= 40) e informe
# o seu salário final naquela semana.

# Lê a quantidade de horas trabalhadas durante a semana
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas na semana: "))

# Fixa o valor do salário base conforme o enunciado da questão
salario_base = 800

# Verifica se a quantidade de horas trabalhadas excede o limite máximo
if horas_trabalhadas > 40:
    # Se exceder, imprime a mensagem abaixo
    print("A quantidade de horas trabalhadas excede o limite máximo e portanto será fixado em 40 horas")
    # Fixa o valor de horas_trabalhadas em 40
    horas_trabalhadas = 40

# Calcula a quantidade de horas extras
horas_extra = horas_trabalhadas - 30

# Calcula quanto o funcionário receberá pelas horas extras trabalhadas
bonus = horas_extra * 150

# Calcula o salário final com base no salario_base e o bonus pelas horas extras
salario_final = salario_base + bonus

# Imprime o resultado
print("Seu salário será R$ ", salario_final)