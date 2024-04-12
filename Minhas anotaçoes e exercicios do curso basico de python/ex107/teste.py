import moeda

n=float(input('Digite um numero:'))
print(f'A metade de R${n} e R${moeda.metade(n)}')
print(f'O dobro de R${n} e R${moeda.dobro(n)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(n,10)}')
print(f'Diminuindo 13%, temos R${moeda.diminuir(n,13)}')
