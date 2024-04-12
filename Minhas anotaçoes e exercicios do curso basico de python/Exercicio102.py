print('='*40)
print('CALCULADORA DE FATORIAL'.center(40))
print('='*40)
while True:
    def fatorial(n,show=True):
        f = 1
        for c in range(n, 0, -1):
            if show:
                print(c, end='')
                if c > 1:
                    print(' x ', end='')
                else:
                    print(' = ', end='')
            f *= c
        return f


    n = int(input('Digite um numero:'))
    print(fatorial(n,show=True ))
    print('='*40)
    perg=str(input('Quer continuar?[S/N]')).strip().upper()[0]
    print('='*40)
    if perg in 'N':
        break
print('<<<<<VOLTE SEMPRE!>>>>>')


