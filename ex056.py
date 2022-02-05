from datetime import date
atual = date.today().year
total_maior = 0
total_menor = 0
for pessoa in range(1, 8):
    nasc = int(input('Em que ano {} pessoa nasceu?: '.format(pessoa)))
    idade = atual - nasc
    if idade >= 21:
        total_maior = total_maior + 1
    else:
        total_menor = total_menor + 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(total_maior))
print('E tambem tivemos {} pessoas menores '.format(total_menor))
