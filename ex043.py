from datetime import date
atual = date.today().year
nascimento = int(input('ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('mirim')
elif idade <= 14:
    print('infantil')
elif idade <= 19:
    print('junior')
elif idade <= 25:
    print('senior')
elif idade > 25:
    print('master')
