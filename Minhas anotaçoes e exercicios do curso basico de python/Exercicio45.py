from random import randint
from time import sleep
itens=('Pedra', 'Papel', 'Tesoura')
computador=randint(0,2)
print('''Sua opçoes
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador= int(input('Qual e sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*11)
print('Computador jogou {}!'.format(itens[computador]))
print('Jogador jogou {}!'.format(itens[jogador]))
print('-='*11)
if computador == 0:
    if jogador ==0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1:
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCEU!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVALIDA!')
