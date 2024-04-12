#Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista,
# ja na posiçao correta de inserçao(sem usar o sort()). No final mostre a lista ordenada na tela.
valores=list()
for c in range(0,5):
    n=int(input('Digite um valor: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
    else:
        pos=0
        while pos < len(valores):
            if n<= valores[pos]:
                valores.insert(pos,n)
                print(f'Adicionado na posiçao {pos} da lista...')
                break
            pos+=1
print('-='*30)
print(f'Os valores digitados em ordem foram {valores}')
