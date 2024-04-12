print('='*30)
print('Sequencia de Fibonacci')
print('='*30)
n=int(input('Digite um numero: '))
t1=0
t2=1
print('~'*30)
print('{} ➞ {}'.format(t1,t2),end='')
cont=3
while cont <=n:
    t3=t2+t1
    print('➞ {}'.format(t3),end='')
    t2=t1
    t1=t2
    cont+=1
print('➞ FIM!')
print('~'*30)