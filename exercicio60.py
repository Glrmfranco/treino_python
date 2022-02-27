#numero = int(input('Digite um numero para calcular o seu fatorial: '))
#c = numero
#f = 1
#print('Calculando {}! = '.format(numero), end='')
#while c > 0:
#    print('{}'.format(c), end='')
#    print(' x ' if c > 1 else ' = ', end='')
#    f = f * c 
#    c -= 1
#print('{}'.format(f))
contador = 0
pulo = int(input('numero pra pular'))
for c in range(0, 30, pulo):
    contador = contador +1
    print('{} \n{}'.format(c, contador), end='')