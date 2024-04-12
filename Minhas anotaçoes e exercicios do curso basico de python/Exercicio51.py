print('='*20)
print('{:^20}'.format('10 TERMOS DE UMA PA'))
print('='*20)
n1 = int(input('Primeiro termo:'))
n2 = int(input('Razao:'))
decimo= n1+(10-1)*n2
for c in range(n1,decimo+n2,n2):
    print('{}'.format(c),end='➜')
print('ACABOU!')