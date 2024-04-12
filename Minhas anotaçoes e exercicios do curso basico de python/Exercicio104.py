while True:
    def leiaint(msg):
        ok = False
        valor=0
        while True:
            n=str(input(msg))
            if n.isnumeric():
                valor=int(n)
                ok=True
            else:
                print('\033[0;31mERRO! Digite um numero inteiro valido.\033[m ')
            if ok:
                break
        return valor



    n=leiaint('Digite um numero:')
    print(f'Voce digitou o numero {n}')
    print('='*40)
    resp=str(input('Quer continuar?[S/N]')).strip().upper()[0]
    print('='*40)
    if resp in 'N':
        break
print('-----Volte Sempre-----')
