# -*- coding: utf-8 -*-

# 4. Dada uma lista de inteiros, faça um programa que procure se um número está na lista. O número a ser buscado deve
# ser fornecido pelo usuário do programa.

# Definindo a lista de números
numeros = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# Lê o número a ser buscado
numero = input("Digite o número que deseja buscar: ")

# Verifica se o número está na lista
if numero in numeros:
    # Se estiver, imprime a mensagem abaixo
    print("Seu número está na lista!")
else:
    # Caso contrário, imprime a mensagem abaixo
    print("Seu número não está na lista!")