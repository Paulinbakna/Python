peso = float(input('Qual seu peso?'))
altura = float(input('Qual sua altura?'))
imc = peso/altura**2
print('O IMC dessa pessoa e de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta abaixo do peso!')
elif imc == 18.6 or imc <= 25:
    print('Voce esta no peso ideal!')
elif imc == 25.1 or imc <= 30:
    print('Voce esta em sobrepeso!')
elif imc == 30.1 or imc <= 40:
    print('Voce esta com obesidade!')
elif imc > 40:
    print('Voce esta com obesidade morbida')
