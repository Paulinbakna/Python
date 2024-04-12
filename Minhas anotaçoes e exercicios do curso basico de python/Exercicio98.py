from  time import  sleep
while True:
    def contador(i,f,p):
        print('='*40)
        print(f'Contagem de {i} ate {f} de {p} em {p}')
        if p<0:
            p*=-1
        if p==0:
            p=1
        if i< f:
            cont=i
            while cont <=f:
                print(f'{cont}',end=' ')
                sleep(0.5)
                cont+=p
            print('FIM!')
        else:
            cont=i
            while cont>=f:
                print(f'{cont}',end=' ')
                sleep(0.5)
                cont-=p
            print('FIM!')

    contador(1,10,1)
    contador(10,0,2)
    print('='*40)
    print('Agora e sua vez de personalizar a contagem!')
    ini=int(input('Inicio: '))
    fim=int(input('Fim:    '))
    pas=int(input('Passo:  '))
    contador(ini,fim,pas)
    print('='*40)
    resp = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    print('='*40)
    if resp in 'N':
        break
print('<<<Volte Sempre!^-^>>>')