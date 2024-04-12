nome=str(input('Digite uma frase:')).upper().strip()
print('A letra A aparece {} vezes ma frase'.format(nome.count('A')))
print('A primeiro letra A apareceu na posiçao {}'.format(nome.find('A')+1))
print('A ultima letra A apareceu na posiçao {}'.format(nome.rfind('A')+1))
