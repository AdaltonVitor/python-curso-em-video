velocidade = float(input('Qual a velocidade do carro em Km/h? '))

multa = (velocidade-80) * 7

if velocidade > 80:
    print('Multado! Voçe exedeu o limite permitido uqe e de 80Km/h')
    print('voçe foi multado no valor de R${:.2f}'.format( multa))

print('Tenha um bom dia! Dirija com segurança!')