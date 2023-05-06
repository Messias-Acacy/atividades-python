from random import randint
somador = 0
N_dado = 0
print('Exemplo: digite 6 para um dado de 6 lados')
dados = int(input('digite aqui quantas faces o dado tem: '))
quantidade = int(input('digite a quantidade  lados do dado aqui: '))

for dado in range(quantidade):
    if dado+1 != quantidade:
        N_dado = randint(1,dados)
        somador = somador+N_dado
        print(N_dado, end=',')
    else:
        N_dado = randint(1,dados)
        somador = somador+N_dado
        print(N_dado, end='')
        print(f' = {somador}')