primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao do PA: '))
termo = primeiro 
cont = 1 
total = 0 
mais = 10

while mais != 0:
    total = total + mais 
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo +=  razao
        cont +=  1
    print('pausa')
    mais = int(input('quantos termos voce quer mostrar a mais ?: '))
print('Progressao finalizada com {} termos mostrados '.format(total))