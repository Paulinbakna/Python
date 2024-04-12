matriz=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for l in range(0,4):
    for c in range(0,5):
        matriz[l][c]=int(input(f'Digite um valor para [{l},{c}]: '))
print('='*50)
for l in range(0,4):
    for c in range(0,5):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
