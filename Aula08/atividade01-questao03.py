# -*- coding: utf-8 -*-

# 3. Faça um programa que leia os pontos dos últimos 10 jogos de um time de futebol e imprima o total de pontos do time
# nesses 10 jogos. Ou seja, você deve imprimir a soma de todos os pontos lidos. Os pontos podem ser 3 (três), em caso
# de vitória, 1 (um) em caso de empate e 0 (zero) no caso de derrota.

# Criando a variável i para contar de 1 até 10
i = 1
# Criando a variável total para somar os pontos do time
total = 0

# Laço condicional para contar de 1 até 10
while i <= 10:
    # Imprime as opções de pontos
    print("3 pontos em caso de vitória")
    print("1 ponto em caso de empate")
    print("0 pontos em caso de derrota")
    # Solicita que o usuário digite a quantidade de pontos recebida no jogo
    pontos = input("Digite os pontos que o time recebeu no "+str(i)+"o. jogo: ")
    # Soma os pontos recebidos no jogo com o total de pontos já recebidos anteriormente
    total = pontos + total
    # Soma o valor de i com 1
    i = i + 1

# Imprime o total de pontos recebidos pelo time
print("Seu time recebeu, no total, "+str(total)+" pontos")