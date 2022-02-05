while True:
    n = int(input('Voce quer ver a tauadade qual valor? '))
    if n < 0:
        break
    print('='*30)
    for c in range (1, 11):
        print(f'{n} X {c} = {n*c}')
    print('='*30)
