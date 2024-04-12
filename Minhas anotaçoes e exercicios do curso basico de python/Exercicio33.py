a= int(input('Primeiro numero:'))
b= int(input('Segundo numero:'))
c=(int(input('Terceiro numero:')))
menor = a
if b<a and b<c:
    menor =b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior= b
if c>a and c>b:
    maior = c
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))
