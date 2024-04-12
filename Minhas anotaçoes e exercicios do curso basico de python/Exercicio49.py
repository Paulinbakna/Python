n1=int(input('Digite um numero para ver sua tabuada:'))
print('='*12)
for c in range(1,11):
    print('{} x {:2}= {}'.format(n1,c,n1*c))
print('='*12)
