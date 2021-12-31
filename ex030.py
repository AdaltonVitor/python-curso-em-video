from random import randint
from time import sleep

computador = randint(0, 5)# faz o cumputador pensar

print('-=-'*20)
print('Vou pensar em um numero entre 0 e 5 . Tente adivinhar...')
print('-=-'*20)

joagdor = int(input('Em que numero pensei ? '))#jogador tenta  adivimhar

print('Processando ...')
sleep(5)
if joagdor == computador:
    print('Parabéns! voce ganhou')
else:
    print('Ganhei! pensei no numero {} e nao no {} '.format(computador, joagdor))
    