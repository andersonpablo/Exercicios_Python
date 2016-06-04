# -*- coding: utf-8 -*-

# 1. Crie uma lista com as notas de 5 alunos, como por exemplo: [80.0, 76.0, 56.8, 68.0, 92.5].
# 2. Usando append, adicione mais 3 notas à sua lista.
# 3. Usando del, remova a primeira e a terceira notas.

# Criando uma lista de notas
notas = [ 80.0, 75.0, 56.8, 68.8, 92.5 ]

# Adicionando a primeira nota
notas.append(85.4)
# Adicionando a segunda nota
notas.append(87.2)
# Adicionando a terceira nota
notas.append(76.3)

# Imprimindo a lista para ver o resultado
print(notas)

# A primeira nota fica na posição 0, portanto temos que remover o valor nessa posição
del(notas[0])

# A terceira nota fica na posição 2 (lembre-se que a contagem das posições começa em 0 e não em 1)
del(notas[2])

# Imprimindo a lista para ver o resultado
print(notas)