
nota = int(input("Digite sua nota de 1 a 10 ")) 

if (nota >= 0) and (nota <= 20):
	print("Conceito E")
	
elif (nota >= 21) and (nota <= 40):
	print("Conceito D")

elif (nota >= 41) and (nota <= 60):
	print("Conceito C")
		
elif (nota >= 61) and (nota <= 80):
	print("Conceito B")

elif (nota >= 81) and (nota <= 100):
	print("Conceito A")
		
else:
	print("Digite uma nota válida")