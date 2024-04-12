n1=float(input('Quantos reais voce tem na carteira?R$'))
dolar=n1/4.97
euro=n1/5.35
peso=n1/0.0060
print('Com R$ {} voce pode comprar US$ {:.2f} dolares'.format(n1, dolar))
print('Com R$ {} voce pode comprar EUR$ {:.2f} Euros'.format(n1, euro))
print('Com R$ {} voce pode comprar P$ {:.2f} pesos argentino'.format(n1, peso))