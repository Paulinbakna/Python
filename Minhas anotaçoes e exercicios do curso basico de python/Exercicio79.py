#Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista.
#Caso o numero ja exista la dentro,ele nao sera adicionado.No final serao exibidos todos
# os valores unicos digitados, em ordem crescente
valores=list()
while True:
    n=(int(input('Digite um valor: ')))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado!Nao vou adicionar na lista....')
    resp=str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp =='N':
        break
print('-='*30)
valores.sort()
print(f'Voce digitou os valores {valores}')
