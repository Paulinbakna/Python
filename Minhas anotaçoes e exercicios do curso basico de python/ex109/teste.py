from ex109 import moeda

n=float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(n)} e {moeda.metade(n,True)}')
print(f'O dobro de {moeda.moeda(n)} e {moeda.dobro(n,True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(n,10,True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(n,13,True)}')
