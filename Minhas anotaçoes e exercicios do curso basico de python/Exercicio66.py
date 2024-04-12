cont=soma=0
while True:
    num=int(input('Digite um numero [999 para parar]:'))
    if num == 999:
        break
    cont+=1
    soma=soma+num
print(f'Foram digitados {cont} numeros e a soma entre eles e {soma}!')
