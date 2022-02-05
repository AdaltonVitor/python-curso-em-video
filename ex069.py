from random import randint
v = 0
while True:
    computador = randint(0, 10)
    print('=' * 30)
    jogador = int(input('Diga um valor'))
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar? ')).strip().upper()[0]
        print('=' * 30)
    print(f'voce jogou {jogador} e o computador {computador} . total de {total}', end='')
    print('Deu Par ' if total % 2 == 0 else 'Deu Impar')
    if tipo == 'P':
        if total % 2 == 0:
            v += 1
            print('Voce Venceu')
        else:
            print('Voce perdeu ')
            break
    elif tipo == "I":
        if total % 2 == 1:
            v += 1
            print('Voce Venceu')
        else:
            print('Voce Perdeu')
            break
    print('Vamos jogar novamente')
print(f'Gamer over! voce venceu {v} veses')
