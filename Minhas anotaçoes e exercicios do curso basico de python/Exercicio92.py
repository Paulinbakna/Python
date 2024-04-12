from datetime import datetime
print('='*40)
print('REGISTRADOR DE DADOS'.center(40))
print('='*40)
dados=dict()
dados['nome']=str(input('Nome:'))
dados['ano de nascimento']=int(input('Ano de Nascimento: '))
dados['carteira de trabalho']=int(input('Carteira de Trabalho(0 nao tem):'))
if dados['carteira de trabalho'] !=0:
    dados['ano de contrataçao'] = int(input('Ano de contrataçao:'))
    dados['salario'] = float(input('Salario: R$'))
    print('='*40)
    print(f'- Nome registrado: {dados["nome"]}')
    dados['idade']=datetime.now().year-dados['ano de nascimento']
    print(f'- Idade: {dados["idade"]}')
    print(f'- ctps: {dados["carteira de trabalho"]}')
    print(f'- ano de contrataçao: {dados["ano de contrataçao"]}')
    print(f'- salario: R$ {dados["salario"]}')
    dados['aposentadoria']=dados['idade']+((dados['ano de contrataçao']+35)-datetime.now().year)
    print(f'- idade de aponsentadoria: {dados["aposentadoria"]} ')
else:
    print('=' * 40)
    print(f'- Nome registrado: {dados["nome"]}')
    dados['idade'] = datetime.now().year - dados['ano de nascimento']
    print(f'- Idade: {dados["idade"]}')
    print(f'- ctps: {dados["carteira de trabalho"]}')
print('='*40)
