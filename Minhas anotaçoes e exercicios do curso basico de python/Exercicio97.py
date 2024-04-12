while True:
    def escreva(msg):
        lin=len(msg)
        print('='*lin)
        print(msg)
        print('='*lin)
    msg=str(input('Digite uma mensagem:'))
    escreva(msg)
    print('='*40)
    resp=str(input('Quer continuar?[S/N]')).strip().upper()[0]
    print('='*40)
    if resp in 'N':
        break
print('<<<Volte Sempre>>>'.center(40))
