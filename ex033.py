distancia = float(input('Digite a distancia da sua viagem em km '))
print('Voce esta prestes a começar uma viagen de {}Km ' .format(distancia))
custo = distancia * 0.50
promocional = distancia * 0.45
if distancia <= 200 :
    print('E o valor da sua passagen sera de R${:.2f} '.format(custo))
else:
    print('E o valor da sua passagen sera de R${:.2f} '.format(promocional))
