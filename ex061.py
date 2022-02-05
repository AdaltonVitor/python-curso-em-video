from time import sleep
n1 = int(input('digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
opcao = 0
while opcao != 5:
    print('''    [1] somar
    [2]multiplicar
    [3]maior
    [4]novos numeros
    [5]sair do programa
    ''')
    opcao = int(input('Qual e a sua opcao? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} e {} e = {}'.format(n1, n2, soma))

    elif opcao == 2:
        multuplicacao = n1 * n2
        print('A multiplicacao entre {} e {} = {}'.format(n1, n2, multuplicacao))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))

    elif opcao == 4:
        print('informe os numeros novamente')
        n1 = int(input('digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))


    elif opcao == 5:
        print('Finalizando.....')
    else:
        print('Opcao invalida. Tente novamente')
    print('=-='* 10)
    sleep(2)


print(' Fim do programa! volte sempre')