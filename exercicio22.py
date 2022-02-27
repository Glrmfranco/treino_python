#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculas
#O nome com todas as letras minusculas
#Quantas letras ao todo(sem considerar espacos)
#Quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome: ')).strip()
print('Seu nome em maiusculas eh {}'.format(nome.upper()))
print('Seu nome em minusculas eh {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras '.format(len(nome)-nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome eh {} e ele tem {} letras'.format(separa[0], len(separa[0])))