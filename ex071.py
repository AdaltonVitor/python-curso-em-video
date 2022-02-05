total = 0
totmil = 0
cont = 0
menor = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preco do produto'))
    total = total + preco
    cont += 1
    if preco > 1000:
        totmil += 1

    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto




    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar [S/N]')).strip().upper()[0]

    if resposta == 'N':
        print('compra finalizada com sucesso')
        break
print(f'sua compra ficou no valor de R${total:.2f}')
print(f'temos {totmil:.2f} produtos custando mais de R$1000.00 ')
print(f'o produto mais barato foi {barato} que  custa R${menor:.2f}')
