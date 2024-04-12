from time import  sleep
def ajuda(com):
    titulo(f'Acessando o manual do comando\'{com}\'')
    help(com)
    sleep(2)


def titulo(msg,cor=0):
    tam=len(msg)+4
    print('~'*tam)
    print(f'{msg}')
    print('~'*tam)
    sleep(1)


comando=''
while True:
    titulo('SISTEMA DE AJUDA PyHelp')
    comando=str(input('Funçao ou biblioteca > '))
    if comando.upper()=='FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO!')
