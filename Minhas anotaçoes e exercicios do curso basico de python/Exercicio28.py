from random import randint
computador= randint(0, 5)
print('-=-'*30)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-'*30)
jogador=int(input('Em que numero estou pensando?'))
if jogador == computador:
    print('Voce Ganhou! eu pensei no numero {}'.format(computador))
else:
    print('Voce Perdeu! eu pensei no numero {}'.format(computador, jogador))