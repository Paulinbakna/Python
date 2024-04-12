from math import radians, sin, cos, tan
n1=float(input('Digite o angulo que voce deseja:'))
sen=sin(radians(n1))
cos=cos(radians(n1))
tan=tan(radians(n1))
print('O seno de {} e {:.2f}, o cosseno e {:.2f}, e a tangente e {:.2f}'.format(n1, sen, cos, tan))