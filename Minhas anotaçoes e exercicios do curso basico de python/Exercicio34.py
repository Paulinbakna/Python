n1=float(input('Qual e o  salario do funcionario?R$'))
if n1 <= 1250:
    novo=n1+(n1*15/100)
else:
    novo=n1+(n1*10/100)
print('Quem ganhava R${} passa a ganhar R${} agora'.format(n1,novo))