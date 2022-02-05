tot18 = toth = totm20 = 0
while True:
    idade = int(input('Informe  sua idade: '))
    sexo = ' '
    while sexo not in 'FM':#enqunto sexo nao estiver in F ou M
        sexo = str(input('Informe seu sexo [F/M]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1

    resposta = ' '
    while resposta not in 'S/N':# resposta nao estiver in S ou N

        resposta = str(input('Gostaria de cadastrar mais alguma pesoa? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
            break
print(f'Total de pessoas maiores de 18 anos{tot18}')
print(f'total de homens {toth}')
print(f'total de mulhres com menos de 20 anos {totm20}')
print('ACABOU')
