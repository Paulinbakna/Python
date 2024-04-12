#para adicionar uma lista em outra lista e so usar o comando
pessoas=list()#nao esquecer de criar a lista que vai adicionar a outra lista
pessoas.append(dados[:])

#para criar uma lista composta:
pessoas=[['Pedro',25],['Mario',19],['Joao',32]]

#para escolher os itens dentro da lista que voce adicionou e so usar o comando:
print(pessoas[0][0])#os numeros siginificam a posiçao que voce quer que apareca
#para mostrar tudo e so usar:
print(pessoas[1])

#para criar  e adicionar uma lista:
galera=list()
dado=list()
for c in range (0,3):
    dado.append(str(input('None: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
#para mostrar uma lista dos maiores e menores de idade:
for p in galera:
    if p[1] >=21:
        print(f'{p[0]} e maior de idade')
        totmai+=1
    else:
        print(f'{p[0]} e menor de idade')
        totmem+=1
print(f'Temos {totmai} maiores e {totmen} menores de idade')
