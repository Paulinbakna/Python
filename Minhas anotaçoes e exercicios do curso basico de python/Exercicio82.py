#Crie um programa que vai ler varios numeros e colocar em uma lista
# Depois disso,crie duas listas extras que vao conter apenas pares e os valores impares digitados,respectivamente
#ao final mostre o conteudo das tres listas geradas
valores=list()
impar=list()
par=list()
while True:
    n=int(input('Digite um numero:'))
    valores.append(n)
    r=str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if n%2==0:
        par.append(n)
    else:
        impar.append(n)
    if r =='N':
        break
print('-='*30)
valores.sort()
print(f'A lista completa e : {valores}')
print(f'A lista de pares e: {par}')
print(f'A lista de impares e: {impar}')
print('-='*30)
