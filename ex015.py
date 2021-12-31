salario = float(input('Qual o salario do funcionario? R$'))
novo = salario + (salario * 15 / 100)
print('O salario do funcionario era R${} e com o ajuste de 15% foi para R${} '.format(salario,novo))