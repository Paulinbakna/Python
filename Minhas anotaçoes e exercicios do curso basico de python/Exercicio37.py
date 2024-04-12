n1=int(input('Digite um numero inteiro:'))
print('''Escolha uma das bases para conversao:
[ 1 ] Converter BINARIO
[ 2 ] Converter OCTAL
[ 3 ] Converter HEXADECIMAL''')
opçao= int(input('Sua opçao: '))
if opçao==1:
    print('{} convertido para BINARIO e igual a {}'.format(n1, bin(n1)[2:]))
elif opçao==2:
    print('{} convertido para OCTAL e igual a {}'.format(n1,oct(n1)[2:]))
elif opçao==3:
    print('{} convertido para HEXADECIMAL e igual a {}'.format(n1, hex(n1)[2:]))
else:
    print('Opçao invalida!')