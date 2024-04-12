print('='*40)
print('FICHA DE UM JOGADOR'.center(40))
print('='*40)
while True:
    def ficha(jog='<desconhecido>',gols=0):
        print(f'o jogador {jog} fez {gols} no campeonato')

    n=str(input('Digite o nome do jogador:'))
    g=str(input('Digite o numero de gols:'))
    if g.isnumeric():
        g=int(g)
    else:
        g=0
    if n.strip()=='':
        ficha(gols=g)
    else:
        ficha(n,g)
    print('='*40)
    reps=str(input('Quer continuar?[S/N]')).strip().upper()[0]
    print('='*40)
    if reps in 'N':
        break
print('<<<<Volte Sempre>>>>')
