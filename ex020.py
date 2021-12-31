import math
angulo = float(input('digite o valor do angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('com o angulo {} o seno é {:.2f}\n o cosseno e {:.2f} e a tangente {:.2f}'.format(angulo, seno, cosseno, tangente))