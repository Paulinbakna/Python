def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError,TypeError):
            print('\033[31mERRO!Digite um numero inteiro valido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mO usuario preferiu nao digitar o numero.\033[m')
        else:
            return n
def linha(tam=42):
    return '-'*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c=1
    for item in lista:
        print(f'\033[32m{c}\033[0m - \033[34m{item}\033[0m')
        c+=1
    print(linha())
    opc=leiaint('\033[32mSua opçao:\033[0m')
    return opc
