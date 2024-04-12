from ex115.exlab.sistem import *
from time import sleep
from ex115.exlab.arquivo import *

arq='cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta=menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do Sistema'])
    if resposta == 1:
        cabeçalho('\033[36mOpçao 1\033[0m')
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('\033[96mOpçao 2\033[0m')
    elif resposta == 3:
        cabeçalho('Saindo do sistema...Ate logo')
    else:
        print('\033[31mERRO!digite uma opçao valida\033[m')
        sleep(2)