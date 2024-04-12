from datetime import date
atual=date.today().year
n1=int(input('Em que ano o atleta nasceu?:'))
idade=atual-n1
print('O atleta tem {} anos'.format(idade))
if idade<=9:
    print('Categoria: MIRIM')
elif idade==10 or idade <=14:
    print('Categoria: INFANTIL')
elif idade==15 or idade <=19:
    print('Categoria: JUNIOR')
elif idade==20 or idade <=25:
    print('Categoria: SENIOR')
elif idade>25:
    print('Categoria: MASTER')
