from random import randint
numero_aleatorios = randint(1,20),randint(1,20),randint(1,20),randint(1,20),randint(1,20)
print(f'A listagem de números é: {numero_aleatorios}')
print(sorted(numero_aleatorios))
print(f'O menor valor é: {sorted(numero_aleatorios)[0]}')
print(f'O maior valor é: {sorted(numero_aleatorios)[4]}')
