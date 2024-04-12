n1=float(input('Qual o preço do produto? R$'))
n2=float(input('Qual o valor do desconto? %'))
novo=n1-(n1*n2/100)
print('O produto custava R${:.2f} antes da promoçao, com o desconto de {}% ira custar R${:.2f}'.format(n1, n2, novo))