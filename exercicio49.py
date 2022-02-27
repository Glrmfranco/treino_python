num = int(input('Digite um numero para fazer a sua tabuada: '))
for c in range(1, 11):
    resultado = num * c
    print('{} X {} = {} '.format(num, c, resultado))