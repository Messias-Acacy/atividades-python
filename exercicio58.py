from random import random, randint
valor = randint(1,10)
numero = int(input('Escreva  o número aqui: '))
while numero != valor:
    print('Você errou. Tente de novo! ')
    numero = int(input('Escreva  o número aqui: '))
print('Você venceu!')