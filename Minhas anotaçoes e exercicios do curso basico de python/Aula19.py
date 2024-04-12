dados='PEDRO',25
#comando para criar um dicionario:
dados =dict()
dados ={'nome':'Pedro','idade':25} #o dicionario e representado por '{}'

#para adicionar algo no dicionario e so usar:
dados['sexo']='M' #ele ira adicionar na sua lista

#para remover algo do dicionario:
del dados['idade']

#no dicionario voce pode abrir e fechar em qualquer lugar,contanto que feche a chave'{}'
Ex:
filme={'titulo':'Star Wars',#nao esquecer da virgula
        'ano':1977,
        'diretor':'George Lucas'
    }
#o comando:
print(filme.values()) # vai mostar oq esta dentro do dicionario EX:'Star Wars',1977,'George Lucas'

# eo comando:
print(filme.keys())#vai mostrar os nomes que voce usou pra adicionar no dicionario EX:'titulo','ano','diretor'

#para mostar a lista toda tando os nomes dos itens que usou pra adicionar quanto os nomes dos itens
#presentes nela
print(filme.items())

estado=dict()
brasil=list()
for c in range (0,3):
    estado['uf']=str(input('Unidade Federativa:'))
    estado['sigla']=str(input('Sigla do Estado:'))
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(f'O campo {k} tem valor {v}.')
#outro metodo:
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
