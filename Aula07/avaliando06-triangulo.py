# -*- coding: utf-8 -*-

# 6. Determinar o tipo de um triângulo dados os valores dos seus três lados. Você deve inserir testes de acordo com as
# expressões abaixo para verificar se os valores fornecidos para os lados formam um triângulo e, caso formem, escrever
# qual o tipo do triângulo. Nas expressões abaixo, “a”, “b” e “c” representam os lados do triângulo. Triângulo: Figura
# geométrica de três lados, em que cada lado é menor que a soma dos outros dois:
# (a < b + c) and (b < a + c) and (c < a + b)
# Triângulo equilátero: Os três lados são iguais: (a == b) and (b == c)
# Triângulo isósceles: Apenas dois lados são iguais: (a == b) or (a == c) or (b == c)
# Triângulo escaleno: Todos os lados são diferentes: (a != b) and (b != c) and (c != a)

# Lê o valor do primeiro lado
a = int(input("Digite o valor do primeiro lado: "))
# Lê o valor do segundo lado
b = int(input("Digite o valor do segundo lado: "))
# Lê o valor do terceiro lado
c = int(input("Digite o valor do terceiro lado: "))

# Verifica se os lados informados formam um triângulo com base na fórmula do enunciado da questão
if (a < b + c) and (b < a + c) and (c < a + b):
    # Se formarem, verifica se os lados formam um triângulo equilátero (três lados iguais)
    if (a == b) and (b == c):
        # Se formar um triângulo equilátero, imprime a mensagem abaixo
        print("O triângulo formado é equilátero!")
    # Caso contrário, verifica se os lados formam um triângulo isósceles (dois lados iguais)
    elif (a == b) or (a == c) or (b == c):
        # Se formar um triângulo isósceles, imprime a mensagem abaixo
        print("O triângulo formado é isósceles!")
    # Caso contrário, só sobrou uma possibilidade: o triângulo é escaleno (três lados diferentes)
    else:
        # Imprime a mensagem informando que o triângulo é escaleno
        print("O triângulo formado é escaleno!")
# Caso os lados não formem um triângulo...
else:
    # Imprime a mensagem abaixo
    print("Os lados informados não formam um triângulo!")