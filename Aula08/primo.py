escreval ("digite um valor")
leia (n)

n = int(input("Digite um número inteiro")) 

for i in range(1,n):

if ( n % i == 0 ):
contador++
     
if ( contador == 2 ):
print ("ele é primo")
	
escreval ("Ele não é primo")