def resumo(n,a,d):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado:     R${n:.2f}')
    print(f'Dobro do preço:      R${n*2:.2f}')
    print(f'Metade do preço:     R${n/2:.2f}')
    print(f'{a}% de aumento:      R${n+(n*a/100):.2f}')
    print(f'{d}% de reduçao:      R${n-(n*d/100):.2f}')
    print('-'*30)
    return n,a,d

