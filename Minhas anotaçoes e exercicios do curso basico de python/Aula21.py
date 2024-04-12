#comando para mostrar quais sao as funcionalidades que o comando possui:
help()
help(print)

#outro comando para mostrar as funcionalidades do comando:
print(input.__doc__)#o comando doc

#comando para criar e mostrar a funcionalidade de um programa que voce criou
#basta digitar 3 aspaas duplas. EX: """ """
""""""
def contador(i,f,p):
    """
    ->FAz uma contagem e mostra na tela
    :param i:inicio da contagem
    :param f:fim da contagem
    :param p:passo da contagem
    :return:sem retorno
    """
    c=i
    while c<=f:
        print(f'{c}',end='')
        c+=p
    print('FIM!')
help(contador)

#parametros opcionais:
#para fazer o comando def funcionar mesmo se nao for informado o numero e so adicionar '=0' EX:
def somar(a=0,b=0,c=0)#assim ele poderar somar qualquer quantidade de numero mesmo se for vazio
    s=a+b+c
    print(f'A soma e igual a {s}')
#escopo de variavel
#comando para voce criar duas variaveis, uma dentro do def e outra fora ou seja voce pode declarar duas variaveis
def funçao():
    n1=4
    print(f'N1 dentro vale {n1}')

n1=2
funçao()
print(f'N1 fora vale {n1}')

#para usar somente o valor dentro do dif e nao o de fora e so usar o comando global: EX
def teste(b):
    global a #comando para valer somente o valor dentro do dif e ignorar o fora dele
    a=8
    b+=4
    c=2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a=5
teste(a)
print(f'A fora vale {a}')

#para msotrar somente um print com todos os valores presentes no def e so usaro return.EX:
def somar(a=0,b=0,c=0):
    s=a+b+c
    return s

r1=somar(3,2,5)#porem precisa adidionar algo para funcionar o return. Ex o r1 ou o print
r2=somar(2,2)
r3=somar(6)
print(f'Os resultados foram {r1,r2,r3}')
