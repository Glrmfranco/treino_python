while True:
    num = int(input('Digite um numero para ver a sua taboada: '))
    if num < 0:
        break
    for cont in range(1,11):
        resultado = num * cont
        print(f'{num} x {cont} = {resultado}')        
print('Fim')
