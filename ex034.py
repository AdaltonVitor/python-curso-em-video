from datetime import date
ano = int(input("Que ano quer analisar? Oloque 0 para analisar o ano atual: "))
if ano == 0:
    ano = date.today().year#pegando o ano atual da maquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:#calculando ano bissesto
    print('O ano {} é bissexto' .format(ano))
else:
    print('O ano {} nao é bissexto' .format(ano))