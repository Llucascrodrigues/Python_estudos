x=int(input())
hora=x//3600
seg=x%60
min=((x%3600)//60)
print("{}:{}:{}".format(hora, min, seg))

