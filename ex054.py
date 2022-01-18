num = int(input('digite um numero: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        total = total + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[m0 o numero {} foi dividido {} veses '.format(num, total))
if total == 2:
    print('E por isso ele e PRIMO')
else:
    print('E por isso ele nao e primo')