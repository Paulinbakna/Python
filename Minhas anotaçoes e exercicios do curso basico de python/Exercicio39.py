ano=int(input('Em que ano voce nasceu?'))
tempo=2024-ano
idade=18
print('Quem nasceu em {} tem {} ano/anos em {}'.format(ano, tempo,2024 ))
if tempo<idade:
    saldo=idade-tempo
    print('Voce ainda vai precisar se alistar e falta {} ano/anos para voce se alistar'.format((saldo)))
    falta=2024+saldo
    print('Seu alistamento sera no ano de {}'.format(falta))
elif tempo==idade:
    print('Esta na hora de voce se alistar!')
elif tempo>idade:
    falta=tempo-idade
    print('Voce ja passou {} ano/anos de se alistar!'.format((falta)))
    passou=2024-falta
    print('Seu alistamento foi em {}'.format(passou))
