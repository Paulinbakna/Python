cont=total=totmil=maior=menor=0
barato=' '
print('='*14)
print('LOJAS FAZ O L')
print('='*14)
while True:
    produto=str(input('Nome do produto:'))
    preco=int(input('Preço R$'))
    print('='*14)
    cont+=1
    total=total+preco
    if preco > 1000:
        totmil+=1
    if cont == 1 or preco <menor:
        menor = preco
        barato=produto
    resp=' '
    while resp not in 'SN':
        resp=str(input('Quer continuar?[S/N]')).strip().upper()[0]
        print('='*14)
    if resp == 'N':
        break
print('==========FIM DO PROGRAMA==========')
print(f'Total gasto na compra R${total}')
print(f'Temos {totmil} produtos que custam mais de R$1000,00')
print(f'O produto mais barato foi  {barato} que custa R${menor:.2f}')
