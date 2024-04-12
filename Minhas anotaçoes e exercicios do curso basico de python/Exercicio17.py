import math
n1=float(input('Qual o valor do cateto oposto?'))
n2=float(input('qual o valor do cateto adjacente?'))
h= math.hypot(n1, n2)
print('A hipotenusa vai medir {:.2f}'.format(h))