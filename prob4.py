#exercicio 4
L1=[]
L2=[]
N=int(input('Digite um valor: '))
for i in range (N):
    L1.append(int(input('Digite outro valor ')))
for i in range (N):
    L2.append(int(input('Digite outro valor ')))
media=(sum(L2))/N
for i in range(N):
    L1[i]
    if L1[i]<media:
        print('Elementos abaixo da média ', L1[i])
    
