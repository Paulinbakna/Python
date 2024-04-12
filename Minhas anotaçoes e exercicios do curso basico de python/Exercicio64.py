num=0
total=0
cont=0
num=int(input('Digite um numero [999 para parar]:'))
while num != 999:
    cont=cont+1
    total=total+num
    num = int(input('Digite um numero [999 para parar]:'))
print('voce digitou {} numeros e a soma entre eles foi {}'.format(cont,total))
