x=int(input('Digite um número ou s para sair '))
L=[x]
menor_divisor=0
maior_divisor=0
if x%2==0:
    menor_divisor=2
elif x%3==0:
    if menor_divisor==2:
        menor_divisor=2
        maior_divisor=3
    else:
        menor_divisor=3
        maior_divisor=3
else:
    if menor_divisor==2:
        menor_divisor=2
        maior_divisor=5
    else:
        menor_divisor=5
        maior_divisor=5
   


while x!='s':
    if x=='s':
        x=str(x)
        L.pop(x)
        break
    else:
        x=(input('Digite um número ou s para sair '))
        if x!='s':
            x=int(x)
            if x%2==0:
                menor_divisor=2
            elif x%3==0:
                if menor_divisor==2:
                    menor_divisor=2
                    maior_divisor=3
                else:
                    menor_divisor=3
                    maior_divisor=3
            else:
                if menor_divisor==2:
                    menor_divisor=2
                    maior_divisor=5
                else:
                    menor_divisor=5
                    maior_divisor=5
        
        L.append(x)

print('O menor divisor é ', menor_divisor)
print('O maior divisor é ', maior_divisor)
    