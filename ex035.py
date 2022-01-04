a = float(input('Digite o primeiro numero: '))
b = float(input('Digite o segundo numero: '))
c = float(input('Digite o terceiro numero: '))
#definindo o menor  numero
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
#definindo maior numero
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor numero e {} '.format(menor))
print('o valor maior e {}'.format(maior))
