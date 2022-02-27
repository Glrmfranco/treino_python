#Crie um numero e mostre seu dobro, triplo e raiz quadrada
numero = int (input('Digite seu numero '))
dobro = numero*2
triplo = numero*3 
rq = numero**(1/2)

print ('Seu numero eh {}, o dobro dele eh {}, o triplo dele eh {} e sua raiz quadrada eh {:.5f}'.format(numero,dobro,triplo,rq))