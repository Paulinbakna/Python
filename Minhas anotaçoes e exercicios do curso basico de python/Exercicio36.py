casa=float(input('Qual o valor da casa?R$'))
salario=float(input('Qual e o salario do comprador?R$'))
anos=int(input('Em quantos anos ele deseja pagar?'))
prestaçao= casa/(anos*12)
minimo=prestaçao*30/100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestaçao sera de R${:.2f}'.format(prestaçao))
if prestaçao<= minimo:
    print('Emprestimo pode ser concedido!')
else:
    print('Emprestimo negado!')