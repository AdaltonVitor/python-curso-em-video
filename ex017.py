km = float(input('Quantos km o carro percorreu?' ))
dias = int(input('Por quantos dias o carro foi alugado? '))
diaria = dias * 60
km_total = km * 0.15
total = diaria + km_total
print('O valor do aluguel sera de R${:.2f}'.format(total))
