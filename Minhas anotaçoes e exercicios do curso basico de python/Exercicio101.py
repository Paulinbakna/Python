from  datetime import date
print('='*40)
print('VERIFICADOR DE VOTAÇAO'.center(40))
print('='*40)
while True:
    def voto():
        idade= (2024 - ano)
        return idade


    ano=int(input('Em que ano voce nasceu?'))
    voto()
    if voto() <16:
        print(f'Com {voto()} anos: NAO VOTA!')
    if 16 <= voto() <18 or voto()>65:
        print(f'Com {voto()} anos: VOTO OPCIONAL')
    else:
        print(f'Com {voto()} anos: VOTO OBRIGATORIO!')
    resp=str(input('Quer continuar?[S/N]'))
    if resp in 'N':
        break
print('='*40)
print('<<<Volte Sempre!>>>'.center(40))
