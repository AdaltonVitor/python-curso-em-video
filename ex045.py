peso = float(input('Qual oseu peso? (Kg) '))
altura = float(input('Q8ual a sua altura? (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa e de {:.1f} '.format(imc))
if imc < 18.5:
    print('voce esta abixo do peso normal')
elif imc <= 18.5 or imc < 25 :
    print('voce esta no peso normal')

elif imc <= 25 or imc < 30:
    print('voce eta com sobrepeso')

elif imc <= 30 or imc < 40:
    print('voce esta com obsidade ')

else:
    print('voce esta com obsidade morbida')
