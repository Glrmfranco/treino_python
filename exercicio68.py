from random import randint

print('-'*30)
print('Vamos jogar par ou impar')
print('-'*30)
cont = 0 
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    cont = cont +1
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]')).upper().strip()[0]
        print(f'Voce jogou {jogador} e o computador {computador}. Total {total}')

    if tipo == 'P':
        if total % 2 == 0:
            print('Voce ganhou !!')
        else:
            print('Voce perdeu !!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce ganhou !!')

        else:
            print('Voce perdeu !!')
            break
    print('Vamos jogar novamente...')
print(f'Fim de jogo, voce venceu {cont} vezes')

        




