r1 = float(input('primeiro segmento '))
r2 = float(input('degundo segmento '))
r3 = float(input('terceiro segmento '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmento acima podem formar um triangulo ', end='')
    if r1 == r2 == r3:
        print('EQILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÒSELES!')
else:
    print('Os segmentos acima nao podem formar um triangulo')