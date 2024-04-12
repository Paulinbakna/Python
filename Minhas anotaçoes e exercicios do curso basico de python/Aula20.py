def mostralinha():
    print('='*40)
mostralinha()
print('SISTEMA DE ALUNOS'.center(40))
mostralinha()
mostralinha()
print('CADASTRO DE FUNCIONARIOS'.center(40))
mostralinha()
mostralinha()
print('ERRO DO SISTEMA'.center(40))
mostralinha()

def mensagem(msg):
    print('='*40)
    print(msg)
    print('='*40)
mensagem('SISTEMA DE ALUNOS'.center(40))
mensagem('CADASTRO DE FUNCIONARIOS'.center(40))
mensagem('ERRO DO SISTEMA'.center(40))

def soma(a,b):
    print(f'A={a}, B={b}')
    s=a+b
    print(f'A soma de A + B ={s}')
soma(4,5)
soma(8,9)
soma(2,1)
mostralinha()
def contador(*num):
    tam=len(num)
    print(f'Recebi os valores {num} e ao todo sao {tam}')
contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)
mostralinha()
def dobra(lst):
    pos=0
    while pos<len(lst):
        lst[pos]*=2
        pos+=1
valores=[7,2,5,0,4]
dobra(valores)
print(valores)
def soma(*valores):
    s=0
    for num in valores:
        s+=num
        print(f'Somando os valores {valores} temos {s}')
soma(5,2)
soma(2,9,4)
