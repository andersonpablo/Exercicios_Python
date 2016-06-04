# -*- coding: utf-8 -*-

# 2. Faça um algoritmo para calcular a área de um círculo, dado o valor do seu raio, que deve ser positivo
# (maior que 0). A fórmula da área do círculo é: area = 3.14 * (raio ** 2).

# Lê o valor do raio
raio = float(input("Digite o raio do círculo: "))

# Verifica se o valor é positivo
if raio > 0:
    # Se for positivo, calcula a área conforme a fórmula do enunciado da questão
    area = 3.14 * (raio ** 2)
    # Imprime o resultado
    print("A área do círculo é: ", area)
else:
    # Se o raio for negativo, imprime a mensagem abaixo
    print("O valor do raio precisa ser positivo!")