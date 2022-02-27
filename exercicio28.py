from random import randint
from time import sleep

computador = randint(0, 5) #Faz o PC sortear um numero
print('='*20)
print('Vou pensar em um numero de 0 e 5. Tente adivinhar... ')
print('='*20)
jogador = int(input('Em que numero eu pensei? '))
print('Processando...')
sleep(1.75)

if jogador == computador:
        print('Parabens, voce acertou o numero')

else:
        print('Voce perdeu, eu pensei no numero {} e nao no {}'.format(computador,jogador))
3