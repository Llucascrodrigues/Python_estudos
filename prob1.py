x=float(input('Escolha um número '))
y=float(input('Escolha outro número '))
região=0
if 0<=x<=10:
    if 15<=y<=20:
        região='A'
    else:
        região='B'
elif 10<x<=15:
    if 0<=y<=20:
        região='C'
elif 15<x<=20:
    if 0<=y<=5:
        região='E'
    elif 5<y<=20:
        região='D'
print('A região é ', região)
    