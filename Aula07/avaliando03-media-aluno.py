# -*- coding: utf-8 -*-

# 3 Faça um programa em Python para calcular a média parcial de um aluno em uma disciplina semestral de acordo com as
# instruções a seguir. O programa deve informar se o estudante foi aprovado, ficou em avaliação final ou foi reprovado;
# O aluno é considerado aprovado se obtiver média igual ou superior a 60 pontos; O aluno deve ir para a prova final
# caso a sua média seja maior ou igual a 30; O aluno está reprovado se a sua média for menor que 30; A fórmula para o
# cálculo da média está descrita abaixo. A variável n1 representa a nota do primeiro bimestre e n2 a nota do segundo
# bimestre: media = (2 * n1 + 3 * n2) / 5

# Lê a nota do primeiro bimestre
n1 = int(input("Digite a nota do primeiro bimestre (de 0 a 100): "))
# Lê a nota do segundo bimestre
n2 = int(input("Digite a nota do segundo bimestre (de 0 a 100): "))

# Calcula a média ponderada conforme o enunciado da questão
media = (2 * n1 + 3 * n2) / 5

# Verifica se a média é maior ou igual a 60
if media >= 60:
    # Se for, informa que o aluno foi aprovado
    print("Aprovado!")
# Caso contrário, verifica se a média é maior ou igual a 30. Não é mais necessário verificar se a média é maior ou igual
# a 60, porque isso já foi verificado no if anterior
elif media >= 30:
    # Se for, informa que o aluno ficou em recuperação
    print("Recuperação!")
# Caso contrário, só sobrou uma possibilidade: o aluno ficou com média inferior a 30
else:
    # Informa que o aluno foi reprovado
    print("Reprovado!")