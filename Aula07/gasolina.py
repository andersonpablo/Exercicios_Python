# -*- coding: utf-8 -*-

distancia = float(input("Digite a dist�ncia pecorrida em KM"))
valor_gasosa =  float(input("Digite o valor da gasolina em R$ "))

gasolina_gasta = (distancia/12)
valor_gasto = gasolina_gasta * valor_gasosa

print ("a quantidade de gasolina gasta � de:", gasolina_gasta, "L")
print ("o valor gasto �: ", valor_gasto, "R$")
