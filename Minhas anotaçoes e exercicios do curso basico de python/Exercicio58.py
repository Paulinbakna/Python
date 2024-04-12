from random import  randint
computador=randint(0,10)
print('Sou seu computador...Acabei de pensar em um numero entre 0 e 10')
print('Sera que voce consegue adivinhar qual foi?')
acertou=False
palpites=0
while not acertou:
    jogador=int(input('Qual e seu palpite?'))
    palpites+=1
    if jogador ==computador:
        acertou= True
    else:
        if jogador<computador:
            print('Mais...Tente mais uma vez.')
        elif jogador>computador:
             print('Menos...Tente mais uma vez.')
print('Acertou com {} tentativas.Parabens'.format(palpites))
