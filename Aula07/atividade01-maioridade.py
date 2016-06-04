# -*- coding: utf-8 -*-

# 1. Leia a idade de uma pessoa e imprima uma mensagem dizendo se ela é maior ou menor de idade.
# Considere que uma pessoa maior de idade é aquela que tem 18 anos ou mais.

# Lê a idade
idade = int(input("Digite a sua idade: "))

# Verifica se a idade é maior ou igual a 18
if idade >= 18:
    # Se a idade for maior ou igual a 18, imprime a mensagem 'Você é maior de idade'
    print("Você é maior de idade")
else:
    # Caso contrário, imprime a mensagem 'Você é menor de idade'
    print("Você é menor de idade")