print('{:=^40}'.format('LOJAS PAULIN'))
preço=float(input('Qual o preço das compras?R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] A vista dinheiro/cheque
[ 2 ] A vista cartao
[ 3 ] 2x no cartao
[ 4 ] x ou mais cartao''')
opçao= int(input('Qual e a opçao?'))
if opçao == 1:
    total=preço-(preço*10/100)
    print('Pagando a vista voce ira pagar R${}'.format(total))
    print('Sua compra de R${:.2f} ira custar R${:.2f} no final'.format(preço,total))
elif opçao == 2:
    total=preço-(preço*5/100)
    print('Pagando a vista no cartao voce ira pagar R${}'.format(total))
    print('Sua compra de R${:.2f} ira custar R${:.2f} no final'.format(preço,total))
elif opçao == 3:
    total=preço / 2
    print('Pagando parcelado em 2x no cartao voce ira pagar duas parcelas no valor de R${} sem juros'.format(total))
    print('Sua compra de R${:.2f} ira custar R${:.2f} no final'.format(preço,total))
elif opçao == 4:
    n1=int(input('Quantas parcelas?'))
    total=preço+(preço*20/100)
    parcela=(total/n1)
    print('sua compra sera parcelada em {}x de R${:.2f} com juros'.format(n1,parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço,total))
else:
    total=0
    print('Opçao invalida digite novamente')
