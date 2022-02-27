num = cont = soma = 0
num = int(input('Digite um numero [999 para parar o programa] :'))
while num != 999:
    soma = soma + num
    cont = cont + 1
    num = int(input('Digite um numero [999 para parar o programa] :'))
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(cont,soma))