from random import randint
dado = input('digite o dado que você quer girar: ')
while dado not in "1,2,4,6,8,10,12,20,100":
    print('Digite uma opção de dado válida!')
    dado = input('digite o dado que você quer girar: ')
quantidade = int(input(f'digite aqui a quantidade de D{dado} que você quer girar: '))
resultado = 0

for x in range(1,quantidade+1):
    random = randint(1,int(dado))
    if x < quantidade:
        if x == 1:
            print(f'({random}', end=',')
        else:
            print(f'{random}', end=',')
    else:
        print(f'{random})', end =' = ')
    resultado = resultado+random

print(resultado)

