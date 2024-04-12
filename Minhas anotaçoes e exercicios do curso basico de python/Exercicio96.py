while True:
    def area(n1,n2):
        a=n1*n2
        print(f'A area de um terreno {n1} x {n2} e de {a}m².')

    print('Controle de terrenos'.center(30))
    print('-'*30)
    n1=float(input('Largura(m):'))
    n2=float(input('Comprimento(m):'))
    area(n1,n2)
    print('='*40)
    resp=str(input('Quer continuar?[S/N]')).strip().upper()[0]
    print('='*40)
    if resp in 'N':
        break
print('<<<Volte Sempre>>>'.center(40))
