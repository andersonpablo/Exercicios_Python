# -*- coding: utf-8 -*-

# 4. Faça um programa que calcule o que deve ser pago por um produto, considerando o preço normal de venda e a escolha
# da condição de pagamento. Utilize os códigos da tabela abaixo para ler qual a condição de pagamento escolhida
# (1, 2 ou 3) e efetuar o cálculo do valor do preço final do produto.
# 1 - À vista em dinheiro ou cheque, recebe 10% de desconto.
# 2 - À vista no cartão de crédito, 5% de desconto.
# 3 - Em 2 vezes, preço normal de venda, sem juros.

# Lê o preço do produto
preco = float(input("Digite o preço do produto: "))

# Imprime as opções de pagamento
print("Formas de pagamento disponíveis")
print("Digite 1 para pagamento a vista em dinheiro ou cheque com recebe 10% de desconto;")
print("Digite 2 para pagamento a vista no cartão de crédito com 5% de desconto;")
print("Digite 3 para pagamento em 2 vezes com preço normal de venda sem juros.")

# Lê a forma de pagamento
forma_pagamento = int(input("Escolha a forma de pagamento (1, 2 ou 3): "))

# Verifica se a forma de pagamento escolhida foi a 1
if forma_pagamento == 1:
    # Imprime como será a forma de pagamento
    print("Pagamento a vista em dinheiro ou cheque com recebe 10% de desconto")
    # Calcula o desconto de 10%
    desconto = preco * 0.1
# Caso contrário, verifica se a forma de pagamento escolhida foi a 2
elif forma_pagamento == 2:
    # Imprime como será a forma de pagamento
    print("Pagamento a vista no cartão de crédito com 5% de desconto")
    # Calcula o desconto de 5%
    desconto = preco * 0.05
# Caso contrário, só sobrou a terceira forma de pagamento
else:
    # Imprime como será a forma de pagamento
    print("Pagamento em 2 vezes com preço normal de venda sem juros")
    # Fixa o desconto em zero
    desconto = 0

# Recalcula o preço do produto com base no valor do desconto
preco = preco - desconto

# Imprime o valor a ser pago
print("Valor a ser pago: R$ ", preco)