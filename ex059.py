sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]# pergunte se o sexo e M/f

while sexo not in 'MmFf':  # enquanto sexo nao estiver em M/F
    sexo = str(input('Dados invalidos. Por favor seu sexo: ')).strip().upper()[0]

print('Sexo {} registrado com sucesso'.format(sexo))
