total18 = 0
totalh = 0
totalm = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo? [M/F]')).strip().upper()[0]
    if idade >= 18:
        total18 = total18 +1
    if sexo == 'M':
        totalh = totalh + 1
    if sexo == 'F' and idade < 20:
        totalm = totalm +1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break


print(f'Total de pessoas com mais de 18 anos: {total18}')
print(f'Ao todos temos {totalh} homens cadastrados')
print(f'E temos {totalm} mulheres com menos de 20 anos')