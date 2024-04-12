n1=float(input('Qual o salario do funcionario?R$'))
n2=float(input('Qual a porcentagem de aumento do salario?'))
novo=n1+(n1*n2/100)
print('Um funcionario que ganhava R${}, com o aumento de {}%, passa a ganhar R${:.2f}'.format(n1,n2, novo))