lanche=('Hamburguer','Suco','Pizza','Pudim')

#comando para colocar em ordem alfabetica
print(sorted(lanche))
#forma que nao mostra a posiçao
for comida in lanche:
    print(f'Eu vou comer {comida}')
#forma pra mostrar a posiçao
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posiçao {cont}')
#outra forma pra mostrar a posiçao
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida}na posiçao {pos}')
print('Comi pra caramba!')
print('='*40)
a=(2,5,4)
b=(5,8,1,2)
c=a+b
#comando para colocar em ordem
print(sorted(c))

#comando para contar quantos elementos tem na tupla
print(c.count(5))

#usa os comandos abaixo para saber qual e o maior e o menor numero de uma tupla
max(),min()

#comando para mostrar em que posiçao esta o numero ou palavra
print(c.index(8))


del#comando para apagar a tupla, faz com que ela nao apareça ,mais no programa,
# e podem adicionar quem posiçao da tupla voce quer que nao apareça
