distancia= float(input('Qual e a distancia da sua viagem?'))
print('Voce esta prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia <= 200:
    valor= distancia * 0.50
    print('Sua viagem ira custa R${:.2f}'.format(valor))
else:
    valor= distancia * 0.45
    print('Sua viagem ira custar R${:.2f}'.format(valor))
print('Tenha uma otima viagem!')