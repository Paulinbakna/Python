cont=('Zero','Um','Dois','Tres','Quatro','Cinco',
      'Seis','Sete','Oito','Nove','Dez',
      'Onze','Doze','Treze','Quatorze','Quinze',
      'Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
while True:
    num=int(input('Digite um numero de 0 a 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente.',end='')
print(f'Voce digitou o numero {cont[num]}')
