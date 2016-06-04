# -*- coding: utf-8 -*-

distancia = float(input("Digite a distância pecorrida em KM"))
valor_gasosa =  float(input("Digite o valor da gasolina em R$ "))

gasolina_gasta = (distancia/12)
valor_gasto = gasolina_gasta * valor_gasosa

print ("a quantidade de gasolina gasta é de:", gasolina_gasta, "L")
print ("o valor gasto é: ", valor_gasto, "R$")
