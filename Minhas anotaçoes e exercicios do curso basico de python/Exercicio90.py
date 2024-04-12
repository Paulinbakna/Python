aluno=dict()
print('='*30)
print('RESULTADO DE APROVADOS'.center(30))
print('='*30)
while True:
    aluno['nome']=str(input('Nome do aluno(a):'))
    aluno['media']=float(input(f'Media do aluno(a) {aluno["nome"]} :'))
    print('-'*30)
    print(f'Nome do aluno(a): {aluno["nome"]}')
    print(f'Media do aluno(a): {aluno["media"]}')
    if aluno['media'] >=7:
        print(f'O aluno(a) {aluno["nome"]} foi Aprovado')
    elif 5<= aluno ['media'] <7:
        print(f'O aluno(a) {aluno["nome"]} esta de Recuperaçao')
    else:
        print(f'O aluno(a) {aluno["nome"]} foi Reprovado')
    print('='*30)
    resp=str(input('Quer Continuar? [S/N]')).strip().upper()[0]
    print('='*30)
    if resp == 'N':
        break
print('ATE MAIS!')