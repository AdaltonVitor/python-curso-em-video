from math import hypot
cateto_oposto = float(input('Digite o cateto oposto'))
cateto_adjacente = float(input('Digite o cateto adjacente: '))
print('o cateto oposto do seu triangula é {},\n  e o cateto adjacente e {}\n '',loga sua hipotenusa sera {:.2f}'.format(cateto_oposto, cateto_adjacente, hypot(cateto_oposto, cateto_adjacente)))