salario = float(input('digite o salario ddo funcionario: '))
aumento1 = (salario * 10) / 100
aumento2 = (salario * 15) / 100
if salario > 1250:
    print('Quem ganhava R${:.2f}, passou a ganhar R${:.2f}'.format(salario, salario + aumento1))
else:
    print('Quem ganhava R${:.2f}, passou a ganhar R${:.2f}'.format(salario, salario + aumento2))