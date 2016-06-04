# -*- coding: utf-8 -*-

# 3. Em uma eleição presidencial existem 4 candidatos. Os votos são informados através de código. Os dados utilizados
# para a contagem dos votos obedecem à seguinte codificação:
# a) 1, 2, 3, 4 = Voto para os respectivos candidatos
#			1 para Cecília Meireles
#			2 para Ariano Suassuna
#			3 para Machado de Assis
#			4 para Graciliano Ramos
#
# b) 5 para voto em branco
#
# c) 1234 para encerrar a votação
#
# d) Qualquer outro valor diferente dos anteriores para anular o voto
#
# Faça um programa que calcule e escreva:
# - O total de votos para cada candidato;
# - O total de votos nulos;
# - O total de votos em branco.

# Cria as variáveis necessárias para contar os votos para cada candidato, nulos e brancos
cecilia = 0
ariano = 0
machado = 0
graciliano = 0
brancos = 0
nulos = 0

# Inicia um laço infinito (loop inifinto) que só será interrompido chamando a instrução break
while True:
    # Imprime as opções
    print("Escolha uma das opções abaixo:")
    print("1 para votar em Cecília Meireles")
    print("2 para votar em Ariano Suassuna")
    print("3 para votar em Machado de Assis")
    print("4 para votar em Graciliano Ramos")
    print("5 para votar em branco")
    print("1234 para encerrar a votação")
    print("Qualquer outro valor para votar nulo")
    # Lê a opção escolhida pelo usuário
    opcao = input("Escolha uma das opções anteriores: ")

    # Se for escolhida a opção 1...
    if opcao == 1:
        # Soma-se um voto para Cecília
        cecilia = cecilia + 1
    # Caso contrário, se for escolhida a opção 2...
    elif opcao == 2:
        # Soma-se um voto para Ariano
        ariano = ariano + 1
    # Caso contrário, se for escolhida a opção 3...
    elif opcao == 3:
        # Soma-se um voto para Machado
        machado = machado + 1
    # Caso contrário, se for escolhida a opção 4...
    elif opcao == 4:
        # Soma-se um voto para Graciliano
        graciliano = graciliano + 1
    # Caso contrário, se for escolhida a opção 5...
    elif opcao == 5:
        # Soma-se um voto em branco
        brancos = brancos + 1
    # Caso contrário, se for escolhida a opção 1234
    elif opcao == 1234:
        # Interrompe o laço
        break
    # Caso contrário...
    else:
        # Soma-se um voto nulo
        nulos = nulos + 1

# Imprime o resultado das eleições
print("### APURAÇÃO DAS ELEIÇÕES ###")
print("Cecília Meireles recebeu " + str(cecilia) + " votos")
print("Ariano Suassuna recebeu " + str(ariano) + " votos")
print("Machado de Assis recebeu " + str(machado) + " votos")
print("Graciliano Ramos recebeu " + str(graciliano) + " votos")
print("Total de votos nulos: " + str(nulos))
print("Total de votos em branco: " + str(brancos))