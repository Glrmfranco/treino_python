a = int(input('Digite o primeiro numero '))
b = int(input('Digite o segundo numero '))
c = int(input('Digite o terceiro numero '))

if a<b and a<c:
    menor = a
if b<c and b<a:
    menor = b
if c<b and c<a:
    menor = c   

print('O menor numero eh o {}'.format(menor))

if a>b and a>c:
    maior = a
if b>c and b>a:
    maior = b
if c>b and c>a:
    maior = c         

print('O maior numero eh o {}'.format(maior))