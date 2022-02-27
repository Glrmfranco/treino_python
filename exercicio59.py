v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))

escolha = 0

while escolha != 5:
    
    print(' [1] somar \n [2] multiplicar \n [3] maior numero \n [4] novos numeros \n [5] sair do programa')
    escolha = int(input('Escolha uma opcao: '))
    if escolha == 1:
        soma = v1 + v2
        print('{} + {} = {}'.format(v1,v2,soma))
    if escolha == 2:
        multiplicar = v1 * v2 
        print('{} + {} = {}'.format(v1,v2,multiplicar))
    if escolha == 3:
        if v1 > v2:
            print('O maior numero eh {}'.format(v1))
        else:
            print('O maior numero eh {}'.format(v2))
    if escolha == 4:
            print('Informa os numeros novamente: ')
            v1 = int(input('Digite o primeiro valor: '))
            v2 = int(input('Digite o segundo valor: '))
    else:
        print('Opcao invalida')     
 
print('Fim')