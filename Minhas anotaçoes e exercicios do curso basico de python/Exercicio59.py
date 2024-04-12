from time import sleep
opçao=0
n1=int(input('Digite o primeiro valor: '))
n2=int(input('Digite o segundo valor: '))
while opçao != 5:
    print('''
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos numeros
[ 5 ] sair do programa''')
    opçao=int(input('>>>>>>>Qual e sua opçao?'))
    if opçao == 1:
        somar=n1+n2
        print('A soma dos valores {} + {} e {}'.format(n1,n2,somar))
    elif opçao == 2:
        multiplicar=n1*n2
        print('A multiplicaçao dos valores {} x {} e {}'.format(n1,n2,multiplicar))
    elif opçao ==3:
        if n1>n2:
            maior=n1
        elif n2>n1:
            maior=n2
            print('Entre {} e {} o maior valor e {}'.format(n1,n2,maior))
        elif n1==n2:
            print('Os numeros {} e {} sao iguais'.format(n1,n2))
    elif opçao == 4:
        print('Informe os novos valores abaixo.')
        n1=int(input('Digite o novo valor:'))
        n2=int(input('DIgite mais um novo valor:'))
    elif opçao == 5:
        print('Ok o programa sera finalizado....')
        sleep(2)
    else:
        print('Opçao invalida digite novamente!')
    print('=-='*10)
print('Programa finalizado!')