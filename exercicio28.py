from random import random, randint
valor = randint(1,5)
numero = int(input('Escreva  o número aqui: '))
if numero == valor:
    print('Você venceu!')
else:
    print('Você perdeu')