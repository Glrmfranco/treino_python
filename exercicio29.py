velocidade = float(input("Qual a velocidade atual do carro ? "))
if velocidade > 80:
    print('Multado! Voce excedeu o limite permitido que eh 80km/h')
    multa = (velocidade - 80) *7
    print('Voce deve pagar uma multa de R${}'.format(multa))
print('Tenha um bom dia! Dirija com seguranca')