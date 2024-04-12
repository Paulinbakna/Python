matriz=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
par=col3=col2=0
for l in range(0,4):
    for c in range(0,5):
        matriz[l][c]=int(input(f'Digite um valor para [{l},{c}]: '))
print('='*50)
for l in range(0,4):
    for c in range(0,5):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c]%2==0:
            par+=matriz[l][c]
    print()
print('='*50)
print(f'A soma de todos os valores pares digitados e: {par} ')
for l in range(0,4):
    col3+=matriz[l][2]
print(f'A soma dos valores da coluna 3 e: {col3} ')
print(f'O maior valor da segunda linha e : {max(matriz[1])}')
print('='*50)
