campeonato=('Palmeiras','Gremio','Ateletico-MG','Flamengo','Botafogo','Red Bull Bragantino','Fluminense',
            'Athletico-Pr','Internacional','Fortaleza','Sao Paulo','Cuiaba','Corinthians',
            'Cruzeiro','Vasco','Bahia','Santos','Goias','Coritiba','America-MG' )
print('-='*40)
print(f'Lista de tiimes do Brasileirao:{campeonato}')
print('-='*40)
print(f'Os 5 primeiros colocados sao:{campeonato[0:5]}')
print('-='*40)
print(f'Os ultimos 4  colocados na tabela sao: {campeonato[16:20]}')
print('-='*40)
print(f'Times em ordem alfabetica: {sorted(campeonato)}')
print('-='*40)
print('O Corinthians esta na {}° posiçao'.format(campeonato.index('Corinthians')+1))
print('-='*40)
