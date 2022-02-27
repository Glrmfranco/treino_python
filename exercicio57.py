sexo = str(input('Qual o seu sexo ? [M/F]')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, por favor informe seu sexo [M/F]')).upper()[0].strip()
print('Sexo {} registrado com sucesso'.format(sexo))

