from random import sample
from time import sleep
jogos=list(range(1,61))
print('='*30)
print('JOGA NA MEGA SENA'.center(30))
print('='*30)
n=int(input('Quantos jogos voce quer que eu sorteiei?'))
print('='*7,f'SORTEANDO {n} JOGOS','='*6)
for c in range (1,n+1):
    bilhete=sample(jogos,6)
    sleep(1)
    print(f'Jogo {c}: {sorted(bilhete)}')
print('='*8,f'< BOA SORTE! >','='*8)