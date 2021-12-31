preço = float(input('Digite o preço de um produto R$ '))
novo = preço-(preço * 5 / 100)
print('O produto custava R${}e com 5% de  desconto saira por R${}'.format(preço,novo))