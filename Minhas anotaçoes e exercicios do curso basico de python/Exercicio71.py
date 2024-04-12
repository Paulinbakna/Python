print('='*25)
print('BEM VINDO AO BANCO POBRE')
print('='*25)
valor=int(input('Qual valor voce deseja sacar?R$'))
total = valor
ced=50
totced=0
while True:
    if total >=ced:
        total-=ced
        totced+=1
    else:
        if totced>0:
            print(f'Total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced=20
        if ced == 20:
            ced=10
        if ced == 10:
            ced=1
        totced=0
        if total ==0:
            break
print('='*25)
print('Volte sempre ao BANCO POBRE! Tenha um Bom Dia!')
print('='*25)