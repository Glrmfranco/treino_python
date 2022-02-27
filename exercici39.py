from datetime import date
nascimento = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
idade = atual - nascimento
print('Voce tem {} anos'.format(idade))
if idade <=17:
    print('Voce ainda nao precisa se alistar ao exercito')
    saldo = 18 - idade
    ano = atual + saldo
    print('Seu alistamento sera no ano {}'.format(ano))
elif idade==18:
    print('Voce precisa se alistar ao exercito este ano')
elif idade>18:
    saldo = idade - 18 
    ano = atual - saldo
    print('Caso ainda nao tenha se alistado voce esta atrasado {} anos para se alistar'.format(saldo))
    print('Seu alistamento foi no ano {}'.format(ano))

    