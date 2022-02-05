cont = soma = 0
while True:
    n = int(input('Digite um valor [ou 999 para parar]'))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'foram somados {cont} numeros e a soa entre eles é {soma}')