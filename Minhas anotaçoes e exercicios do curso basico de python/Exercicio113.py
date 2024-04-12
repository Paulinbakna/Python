
def leiaint(msg):
    while True:
        try:
            valor=int(input(msg))
        except (ValueError,TypeError):
            print('\033[0;31mERRO! Digite um numero inteiro valido.\033[m ')
            continue
        except KeyboardInterrupt:
            print('\033[32mO usuario preferiu finalizar o programa.\033[0m')
            return 0
        else:
            return valor

def leiafloat(msg):
    while True:
        try:
            num=float(input(msg))
        except (ValueError,TypeError):
            print('\033[0;31mERRO!Digite um numero flutuante valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[32mO usuario preferiu nao informar os valores.\033[0m')
            return 0.0
        else:
            return num
while True:
    n=leiaint('Digite um numero inteiro:')
    m=leiafloat('Digite um numero flutuante : ')
    print(f'O numero inteiro digitado foi {n} e o numero flutuante digitado foi {m}')
    print('='*40)
    resp=str(input('Quer continuar?[S/N]')).strip().upper()[0]
    print('='*40)
    if resp in 'N':
        break
print('-----Volte Sempre-----')
