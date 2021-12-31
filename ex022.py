import random
n1 = input('primeiro aluno')
n2 = input('segundo aluno')
n3 = input('terceiro aluno')
lista = [n1, n2, n3]
random.shuffle(lista)
print('A ordem de apresentaçao será')
print(lista)