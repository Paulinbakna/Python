n1=float(input('Primeira nota:'))
n2=float(input('Segunda nota:'))
media=(n1+n2)/2
print('Tirando {} e {}, a media do aluno e de {}'.format(n1,n2,media))
if media<5.0:
    print('Infelizmente o aluno nao  atingiu a media e foi reprovado')
elif media==5 or media <=6.9:
    print('O aluno esta de recuperaçao')
elif media>7.0:
    print('O aluno foi aprovado!')
