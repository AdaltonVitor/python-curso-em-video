print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Qual valor vc deseja sacar? '))
total = valor
cedula = 50
totalcedula = 0
while True:
    if total >= cedula:# se o total for maior ou igual a 50
        total -= cedula# o total passa a ser 50
        totalcedula += 1# aqui o total de cedula recebe + 1
    else:
        if totalcedula > 0:
            print(f'total de {totalcedula} cedulas de {cedula}')

        if cedula == 50:#se a cedula for igual a 50
            cedula = 20# a cedula passa a ser 20

        elif cedula == 20:#se a cedula for igaul a 20
            cedula  = 10

        elif cedula == 10:#se a cedula for igual a 10
            cedula = 1
        totalcedula = 0

        if total == 0:# se a cedula chegar a zero para o sistema
            break
print('='*30)
print('volte sempre ao banco CEV')