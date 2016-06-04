# -*- coding: utf-8 -*-

# 6. Leia um texto com 10 caracteres minúsculos e diga quantas vogais foram lidas.

# Cria uma lista com as vogais
vogais = [ 'a', 'e', 'i', 'o', 'u' ]

# Lê o texto do usuário
texto = raw_input("Digite uma frase: ")

# Cria a variável i para contar de 0 até o tamanho do texto
i = 0
# Cria a variável contador para contar quantas vogais o texto tem
contador = 0

# Laço condicional para iterar no texto
while i < len(texto):
    # Se o caractere da posição i estiver contido na lista vogais...
    if texto[i] in vogais:
        # Soma-se 1 a contador
        contador = contador + 1
    # Soma-se 1 a i
    i = i + 1

# Imprime a quantidade de vogais do texto
print("Seu texto possui " + str(contador) + " vogais")