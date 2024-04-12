from ex115.exlab.sistem import *
def arquivoExiste(nome):
    try:
        a=open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a=open(nome,'wt+')
        a.close()
    except:
        print('Houve um ERRO na criaçao do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a=open(nome,'rt')
    except:
        print('ERRO ao ler o arquivo')
    else:
        cabeçalho('\033[94mPESSOAS CADASTRADAS\033[0m')
        print(a.read())