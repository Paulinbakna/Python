from time import sleep
from random import randint
jogo={'jogador 1': randint(1,6),
      'jogador 2': randint(1,6),
      'Jogador 3': randint(1,6),
      'jogador 4': randint(1,6)}
ranking=list()
print('Valores sorteados:')
print('-'*26)
for  k,v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking=sorted(jogo.items(),key=lambda item: item[1], reverse=True) #para colocar o dicionario com os numeros em ordem
print('='*26)
print('==RANKING DOS JOGADORES==')
for i,v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)
