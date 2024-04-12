#o comando "try" signfica que pro programa tentar alguma coisa
# e o comando "except" significa se ele nao conseguir executar o comando "try"
try:
    a=int(input('Digite um numero:'))
    b=int(input('Digite outro numero'))
    r=a/b
#um "try" pode ter varios "except" e voce pode criar um except para cada tipo de erro
except (ValueError,TypeError):
    print('Tivemos um problema com os tipos de dados que voce digitou')
except ZeroDivisionError:
    print('Nao e possivel dividir um numero por zero!')
except KeyboardInterrupt:
    print('O Usuario preferiu nao informar os dados')
else:
    print(f'O resultado e {r:.1f}')
#o comando "finally" vai sempre acontecer mesmo se o programa nao der certo
finally:
    print('Volte Sempre! Muito Obrigado')