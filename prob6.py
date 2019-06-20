x=int(input('Digite um número ou s para sair '))
L=[]
i=0
L.append(x)
count=0
L_1=[]
maior_par=0
menor_par=0
maior_impar=0
menor_impar=0
if x%2==0:
    L_1.append('par')
else:
    L_1.append('Ímpar')

while x!='s':
    if x=='s':
        x=str(x)
        break
    else:
        x=(input('Digite um número ou s para sair '))
        count=count+1
        if x!='s':
            x=int(x)
        L.append(x)
L.pop()
L_1.pop()
for i in range (0,count,1):
    if L[i]%2==0:
        L_1.append('Par')
        if L[i]>L[i-1]:
            maior_par=L[i]
        if L[i-1]>L[i]:
            menor_par=L[i]
    else:
        L_1.append('Ímpar')
        if L[i]>L[i-1]:
            maior_impar=L[i]
        if L[i-1]>L[i]:
            menor_impar=L[i]
        

print('O maior número par é ', maior_par)
print('O maior número impar é ', maior_impar)
print('O menor número par é ', menor_par)
print('O menor número impar é ', menor_impar)