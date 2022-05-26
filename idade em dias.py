d=int(input())
ano=d//365
rest=d%365
mes=rest//30
dias=rest%30
print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(ano, mes, dias))

