valorcasa = float(input('Digite o valor da casa que deseja comprar: '))
salario = float(input('Digite o seu salario para avaliacao de credito: '))
ano = int(input('Em quantos anos deseja pagar a casa ?: '))
prestacao = valorcasa / (ano * 12)
minimo = salario * 30 /100
print('O valor da prestacao da casa vai ser de R${:.2f}'.format(prestacao))

if salario <= minimo:
    print('Seu emprestimo foi aprovado')
else:
    print('Seu emprestimo nao foi aprovado')





