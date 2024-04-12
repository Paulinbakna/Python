palavras=('aprender','programar','limguagem','python',
          'curso','gratis','estudar','praticar','mercado','programador','futuro')
for p in palavras:
    print(f'\n Na palavra {p.upper()} temos as vogais: ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')
