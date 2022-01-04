print('-='*20)
print('Analisador de triangulo')
print('-='*20)
r1 = float(input('primeiro segmento '))
r2 = float(input('degundo segmento '))
r3 = float(input('terceiro segmento '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmento acima podem formar um triangulo')
else:
    print('Os segmentos acima nao podem formar um triangulo')