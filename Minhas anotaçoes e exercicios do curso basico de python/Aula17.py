#comando para adicionar algo na lista, ele vai criar um elemento na lista para esse item
lanche.append(9)

#comando para inserir algo na lista,colocar algo nela em qualquer posiçao
lanche.insert(0,9)

#os comandos 1 e 2 voce remove o item da lista completamente, e reposiciona a comtagem da lista,
# ja o comando 3 so remove o item que voce selecionar
del lanche[3]
lanche.pop(3) #pode usar o comando lanche.pop() para remover o item da ultima lista
lanche.remove()

#comando para remover algo na lista so se estiver nela, se nao estiver ele nao ira executar
if '9' in lanche:
    lanche.remove('9')

#comando para colocar os valores como voce preferir
valores=list(range(4,11))

#para criar um elemento de acordo com a ordem que voce quer
valores=[8,2,5,4,9,3,0]

#para colocar em ordem e so escrever o comando:
valores.sort()

#para colocar em ordem reversa e so escrever:
valores.sort(reverse=True)

#para colocar uma lista mais bonita:
valores= list[]
valores.append(5)
valores.append(9)
valores.append(4)

for c,v in enumerate(valores):
    print(f'Na posiçao {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

#para o programa ler o valor digitado pelo teclado
valores=list()
for cont in range (0,5):
    valores.append(int(input('Digite um valor:')))

#comando para copiar uma lista mas poder substituir ela
a=[2,3,4,7]
b=a[:]#usa o '[:]' para poder substituir algo se, alterar a lista 'a'
b[2]=8

carros={'carro1':'Fiat Estrada','valor1':101.990,
        'carro2':'Vw Polo','valor2':90.990,
        'carro3':'Chevrolet Onix','valor3':86.150,
        'carro4':'Hyundai HB20','valor4': 84.390,
        'carro5':'Dodge Ram Trx','valor5':577.650,
        'carro6':'Fiat Mob','valor6':71.990,
        'carro7':'Chevrolet S-10','valor7':302.900,
        'carro8':'Fiat Argo','valor8': 69.990,
        'carro9':'Chevrolet Tracker','valor9':127.900,
        'carro10':' Hyundai Creta','valor':  160.990}