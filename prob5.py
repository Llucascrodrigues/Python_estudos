#Exercicio 5
x=float(input('Digite uma cordenada '))
y=float(input('Digite uma cordenada '))
A=((x-5)**2)+((y-10)**2)-5**2
B=((x-10)**2)+((y-10)**2)-5**2
if 5<=y<=15:
    if 0<=x<5:
        print('O pontos estão em A')
    elif 5<=x<10:
        print('O pontos está na intersecção de A e B')
    elif 10<=x<=15:
        print('O pontos estão em B')
else:
    print('O pontos estão fora da circunfêrencia')
