distancia = int(input('Digite a distancia da viagem em km para calcular a passagem: '))
preco1 = distancia * 0.50
preco2 = distancia * 0.45

if distancia <=200:
    print('O preco da passagem eh de R${:.2f}'.format(preco1))

else:
    print('O preco da passagem eh de R${:.2f}'.format(preco2))