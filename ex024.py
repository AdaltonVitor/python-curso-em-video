nome = str(input('digite seu nome completo ')).strip()
print('Analisando seu nome ...')
print('Seu nome em minuscula é {}'.format(nome.lower()))
print('Seu nome em maiuscuola é {}'.format(nome.upper()))
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))