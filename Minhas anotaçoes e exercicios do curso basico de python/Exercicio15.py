n1=float(input('Quantos dias alugados?'))
n2=float(input('Quantos Km rodados?'))
dias=n1*60
km=n2*0.15
total=dias+km
print('O total a ser pago e de R${:.2f}'.format(total))