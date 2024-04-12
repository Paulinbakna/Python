#Crie um programa que vai ler varios numeros e colocar em uma lista.
#Depois disso mostre:
#a)Quantos numeros foram digitados,b)Alista de valores ordenada dde forma decrescente,
# c)Se o valor 5 foi digitado e esta ou nao na lista
valores=list()
cont=0
while True:
    n=int(input('Digite um valor:'))
    valores.append(n)
    cont+=1
    r=str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if r =='N':
        break
print('-='*30)
print(f'Voce digitou {cont} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente sao {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 nao foi encontrado na lista!')
