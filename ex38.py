casa = float(input('qual o valor da casa ? '))
salario = float(input('qual seu salario mensal ? '))
ano = int(input('em quantos anos pretende pagar'))
prestacao = casa / (ano * 12)
minimo = salario * 30 / 100
print('''
para pagar uma casa de r${:.2f} em {:.2f} anos 
a prestacao sera de R${:.2f}
'''.format(casa, ano, prestacao))
if prestacao <= minimo:
    print('o emprestimo pode sr concedido')
else:
    print('emprestimo negado')