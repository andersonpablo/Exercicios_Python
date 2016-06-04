# -*- coding: utf-8 -*-

# 1. Faça um algoritmo que leia n valores e calcule a média aritmética desses valores.

# Lê a quantidade de valores a serem digitados
quantidade = input("Digite um número: ")

# Criando a variável i para contar de 1 até o valor da variável quantidade
i = 1
# Criando a variável que será usada para somar os valores digitados pelo usuário
somatorio = 0

# Laço condicional para contar de 1 até o valor da variável quantidade
while i <= quantidade:
    # Solicita que o usuário digite um valor
    valor = input("Digite o " + str(i) + "o. valor: ")
    # Soma o valor com o somatório dos valores digitados anteriormente
    somatorio = somatorio + valor
    # Incrementa o valor de i em 1
    i = i + 1

# Calcula a média aritmética dos valores digitados
media = somatorio / quantidade

# Imprime o resultado
print("A média dos valores digitados é " + str(media))