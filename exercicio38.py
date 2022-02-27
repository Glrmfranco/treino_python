n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1>n2:
    print('O primeiro valor eh maior')
elif n2<n1:
    print('O segundo valor eh maior')

elif n2==n1:
    print('Nao existe valor maior, os dois sao iguais')