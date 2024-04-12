#Faça um programa que leia 5 valores numericos e guarde=os em uma lista.
#No fina, mostre qual foi o maior e o menor valor digitado e as suas respectivas posiçoes na lista.
valores=list()
for cont in range (0,5):
    valores.append(int(input('Digite um valor:')))
print('=-='*10)
print(f'Lista dos valores digitados: {valores}')
print(f'O maior valor digitado foi {max(valores)} na posiçao {valores.index(max(valores))}')
print(f'O menor valor digitado foi {min(valores)} na posiçao {valores.index(min(valores))}')
