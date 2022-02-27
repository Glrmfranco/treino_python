resp = 'S'
media = 0
soma = 0 
quantidadevalor = 0
maior = 0
menor = 0 
while resp in 'Ss':
    num = int(input('Digite um numero:'))
    soma += num
    quantidadevalor = quantidadevalor +1
    if quantidadevalor == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / quantidadevalor
print('Voce digitou {} numeros e a media foi {:.2f}'.format(quantidadevalor, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
