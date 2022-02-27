soma = 0
cont = 0
for numero in range(0, 6):
    numero = int(input('Digite um numero:'))
    if numero % 2 == 0:
        soma = soma + numero
        cont = cont + 1 
print('Voce informou {} numeros pares e a soma deles eh de {}'.format(cont, soma))

