# -*- coding: utf-8 -*-

# 5. A partir de um texto fornecido pelo usuário, conte quantos caracteres esse texto possui, sem contar os espaços
# em branco.

# Lê a frase do usuário
frase = raw_input("Digite uma frase: ")

# Cria a variável i para contar de 0 até o tamanho da frase
i = 0
# Cria a variável contador para contar quantos caracteres a frase tem
contador = 0

# Laço condicional para iterar na frase
while i < len(frase):
    # Se o caractere i da frase for diferente de espaço em branco...
    if frase[i] != " ":
        # Soma-se 1 a contador
        contador = contador + 1
    # Soma-se 1 a i
    i = i + 1

# Imprime o resultado
print("Sua frase tem " + str(contador) + " caracteres")