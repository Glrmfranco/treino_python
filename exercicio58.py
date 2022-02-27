from random import randint

computador = randint(0, 10)
print('='*20)
print('Vou pensar em um numero de 0 e 10. Tente adivinhar... ')
print('='*20)
jogador = int(input('Em que numero eu pensei? '))
tentativa = 0

while jogador != computador:
    print('Eu pensei no numero {} e voce no {}, tente novamente'.format(computador, jogador))
    computador = randint(0, 10)
    jogador = int(input('Em que numero eu pensei? '))
    tentativa = tentativa +1
    if jogador == computador:
        print('Parabens, depois de {} tentativas , voce acertou'.format(tentativa))
print('Fim do jogo')
