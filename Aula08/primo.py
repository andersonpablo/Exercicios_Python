escreval ("digite um valor")
leia (n)

n = int(input("Digite um n�mero inteiro")) 

for i in range(1,n):

if ( n % i == 0 ):
contador++
     
if ( contador == 2 ):
print ("ele � primo")
	
escreval ("Ele n�o � primo")