num = int(input('digite um numero inteiro '))
print('''Escolha umas das bases para conversao
[1]converter para binario
[2]converter para octal
[3]converter para hexadecimal

''')
opçao = int(input('sua opçao'))
if opçao == 1:
    print('{} convertido para binario e igual a {} '.format(num, bin(num)[2:]))
elif opçao == 2:
    print('{} convertido para octal e igual a {} '.format(num, oct(num)[2:]))
elif opçao == 3:
    print('{} convertido para hexadecimal e igual a {} '.format(num, hex(num)[2:]))
else:
    print('opcao invalida tente outra opcao ')