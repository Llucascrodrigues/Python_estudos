#exercicio 08
L1=[]
L2=[]
N=int(input('Digite um valor: '))
for i in range (N):
    L1.append(float(input('Digite outro valor ')))
med1=(sum(L1))/N 
i=int(input('Digite um valor: '))
for i in range (N-1):
    L2.append(L1[i+1])
med2=(sum(L2))/(N-1)
print('A média da primeira parte é'med1)#os valores são diferentes do que está dando na lista
print('A média da segunda parte é'med2)
#se verificar a media dos valores dados é diferente do que está na lista!
