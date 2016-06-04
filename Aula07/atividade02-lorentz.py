# -*- coding: utf-8 -*-

# 2. Tendo como entrada a altura em centímetros (p.ex. 1.70m = 170cm) e o sexo de uma pessoa
# (“m” para masculino ou “f” para feminino), calcule o seu peso ideal de acordo com a fórmula abaixo, conhecida como
# fórmula de Lorentz. Nessa fórmula, o valor “k” é igual a 4 para homens e 2 para mulheres.

# Lê a altura
altura = int(input("Digite a sua altura em centímetros: "))

# Lê o sexo
sexo = input("Digite 'm' para masculino ou 'f' para feminino: ")

# Verifica se o sexo é masculino
if sexo == "m":
    # Se o sexo for masculino, cria a variável 'k' e atribui o valor 4
    k = 4
else:
    # Se o sexo for feminino, cria a variável 'k' e atribui o valor 2
    k = 2

# Calcula o peso ideal com base na fórmula de Lorentz
peso = altura - 100 - ((altura - 150) / k)

# Mostra o peso ideal
print("Seu peso ideal é ", peso, " Kg")