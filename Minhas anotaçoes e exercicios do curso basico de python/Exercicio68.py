from random import randint
v=0
print('=-'*13)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*13)
while True:
    jogador=int(input('Digite um numero: '))
    computador=randint(0,10)
    total=jogador+computador
    tipo= ' '
    while tipo not in 'PpIi':
        tipo=str(input('Par ou Impar?[P/I]')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador jogou {computador} e o total foi {total}',end=' ')
    print('DEU PAR!'if total % 2==0 else 'DEU IMPAR!',end=' ')
    if tipo == 'P':
        if total % 2==0:
            print('Voce VENCEU!')
            v+=1
        else:
            print('Voce PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 ==1:
            print('Voce VENCEU!')
            v+=1
        else:
            print('Voce PERDEU!')
            break
    print('Vamos jogar novamente....')
    print('=-'*13)
print(f'GAME OVER! Voce venceu {v} vezes.')
