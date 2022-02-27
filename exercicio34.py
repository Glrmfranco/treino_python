salario = float(input('Qual o salario do funcionario? '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)    

print('Quem ganhava R$\033[1;31m{:.2f}\033[m passa a ganhar R$\033[1;32m{:.2f}\033[m'.format(salario, novo))
