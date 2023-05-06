from random import randint
confirmar = 'sim'
while confirmar in "SImsimYESyes":
    somador = 0
    N_dado = 0
    print('Exemplo: digite 6 para um dado de 6 lados')
    dados = int(input('digite aqui quantas faces o dado tem: '))
    quantidade = int(input(f'digite a quantidade  lados do D{dados} aqui: '))
    print(f'Você girou: {quantidade}D{dados}!')
    print(10*'-')
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
    print(10*'-')
    
    confirmar = input('quer continuar? [SIM/NÃO]: ')
    if confirmar not in "SIMsimYESyes":
        print('Programa encerrado!')
        break
    