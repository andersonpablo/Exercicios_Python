# -*- coding: utf-8 -*-

# 2. Faça um algoritmo que leia uma quantidade de N números que serão digitados e, ao final do processamento do
# algoritmo, mostre qual foi o maior número digitado.

# Lê a quantidade de valores a serem digitados
quantidade = input("Digite a quantidade de valores que serão inseridos: ")

#
i = 1
maior = 0

while i <= quantidade:
    # Solicita que o usuário digite um valor
    valor = input("Digite o " + str(i) + "o. valor: ")
    if i == 1:
        maior = valor
    elif(valor > maior):
        maior = valor
    i = i + 1

print("O maior valor digitado foi " + str(maior))