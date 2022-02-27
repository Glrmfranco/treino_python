#nome = str(input('Qual o seu nome completo? ')).strip()
#print ('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
nome = input('Digite seu nome completo: ').strip()
i = nome.split()
ver = i[0]
confira = ('Silva'.title() in ver) or ('Silva'.lower() in ver) or ('SILVA' in nome.upper())
z = (ver[0:][5:] in nome)

print('Seu nome possui Silva? {}'.format(confira and z).replace('True', 'Sim').replace('False', 'Não'))
