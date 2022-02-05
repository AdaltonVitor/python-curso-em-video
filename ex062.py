n = int(input('Digite um numero para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print('X' if c > 1 else '=', end='')
    f = f * c
    c = c - 1
print('{}'.format(f))
