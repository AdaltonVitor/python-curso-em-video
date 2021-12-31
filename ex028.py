frase = str(input('Digite uma frase ')).strip().upper()
print('A letra A aparece {} veses '.format(frase.count('A')))
print('O primeiro A esta na posicao {}'.format(frase.find('A')+1))
print('O ultimo A aparece na popopsiçao {}'.format(frase.rfind('A')+1))
