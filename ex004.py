   # faça um programa que leia algo pelo teclado
   #  e mostre na tela o seu tipo primitivo
   #  e todas as informacoes possiveis sobre ela


a=input('Digite algo')

print('O tipo primitivo desse valor é',type(a))

print('Só tem espaços?',a.isspace())

print('É un numero?',a.isnumeric())

print('È alfabetico?',a.isalpha())

print('È alphanumerico?',a.isalnum())

print('Esta em maiusculas?',a.isupper())

print('Esta em minusculas?',a.islower())

print('Esta capitalizada?',a.title())