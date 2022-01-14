print('{:=^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Qual o preço das compras? '))
print('''FORMA DE PAGAMENTO
[1] dinheiro ou cheque
[2] a vista no cartao
[3] em ate 2x no cartao
[4] em 3x ou mais no cartao
''')
opcao = int(input('qual a sua opcao? '))

if opcao == 1:
    total = preco - (preco * 10 / 100)

elif opcao == 2:
    total = preco - (preco * 5 / 100)

elif opcao == 3:
    total = preco
    parcela = preco / 2
    print('sua compra sera parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))

elif opcao == 4:
    total = preco + (preco * 20 /100)#preco total + juros
    totalparcela = int(input('quantas parcelas'))#perguntado o numero de parcelas
    parcela = total / totalparcela # programando valor de cada parcela
    print('sua compra sera parcelada em {}x de R${:.2f} COM JUROS'.format(totalparcela, parcela))
else:
    total = preco
    print('OPCAO INVALIDA de pagamento. Tente novamente')#tratando opcao invalida

print('Sua compra de R${:.2f} vai custar R${} no final'.format(preco, total))