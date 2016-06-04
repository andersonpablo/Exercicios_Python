# -*- coding: utf-8 -*-

ladoA = int(input("Digite o valor do primeiro lado: "))
ladoB = int(input("Digite o valor do segundo lado: "))
ladoC = int(input("Digite o valor do terceiro lado: "))

if (ladoA < ladoB + ladoC) and (ladoB < ladoA + ladoC) and (ladoC < ladoA + ladoB):
    if (ladoA == ladoB) and (ladoB == ladoC):
        print("O triângulo formado é equilátero!")
    elif (ladoA == ladoB) or (ladoA == ladoC) or (ladoB == ladoC):
        print("O triângulo formado é isósceles!")
    else:
        print("O triângulo formado é escaleno!")
else:
    print("Os lados informados não formam um triângulo!")