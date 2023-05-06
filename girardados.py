while True:
    somador = 0
    from random import randint
    print(""" PROGRAMA PARA GIRAR DADOS!
    ESCOLHA UM DOS DADOS ABAIXO PARA GIRAR!
    [1] - D6
    [2] - D8
    [3] - D10
    [4] - D12
    [5] - D20
    [6] - D100
    [7] - SAIR
    
    obs.: você digitar, por exemplo: D6 ou 1 para iniciar!
    """)

    opcao = input('Digite aqui uma opção: ')

    if opcao in '7sairSAIR':
        print('Programa encerrado!')
        break

    else:
        quantia = int(input('digite a quantidade de dados que quer girar: '))
        

    if opcao in 'D61d':
        print(f'Você girou {quantia}D6')
        print(6*'-')
        for d6 in range(quantia):
            if d6+1 != quantia:
                dados = randint(1,6)
                print(dados,end = ',')
                somador = somador + dados
            else:
                dados = randint(1,6)
                print(dados, end = '')
                somador = somador + dados
                print(f' = {somador}')
                print(6*'-')

    elif opcao in 'D82d':
        print(f'Você girou {quantia}D8')
        print(6*'-')
        for d8 in range(quantia):
            if d8+1 != quantia:
                dados = randint(1,8)
                print(dados,end = ',')
                somador = somador + dados
            else:
                dados = randint(1,8)
                print(dados, end = '')
                somador = somador + dados
                print(f' = {somador}')
                print(6*'-')

    elif opcao in 'D103d':
        print(f'Você girou {quantia}D10')
        print(6*'-')
        for d10 in range(quantia):
            if d10+1 != quantia:
                dados = randint(1,10)
                print(dados,end = ',')
                somador = somador + dados
            else:
                dados = randint(1,10)
                print(dados, end = '')
                somador = somador + dados
                print(f' = {somador}')
                print(6*'-')

    elif opcao in 'D124d':
        print(f'Você girou {quantia}D12')
        print(6*'-')
        for d12 in range(quantia):
            if d12+1 != quantia:
                dados = randint(1,12)
                print(dados,end = ',')
                somador = somador + dados
            else:
                dados = randint(1,12)
                print(dados, end = '')
                somador = somador + dados
                print(f' = {somador}')
                print(6*'-')

    elif opcao in 'D205d':
        print(f'Você girou {quantia}D20')
        print(6*'-')
        for d20 in range(quantia):
            if d20+1 != quantia:
                dados = randint(1,20)
                print(dados,end = ',')
                somador = somador + dados
            else:
                dados = randint(1,20)
                print(dados, end = '')
                somador = somador + dados
                print(f' = {somador}')
                print(6*'-')

    elif opcao in 'D1006d':
        print(f'Você girou {quantia}D20')
        print(6*'-')
        for d100 in range(quantia):
            if d100+1 != quantia:
                dados = randint(1,100)
                print(dados,end = ',')
                somador = somador + dados
            else:
                dados = randint(1,100)
                print(dados, end = '')
                somador = somador + dados
                print(f' = {somador}')
                print(6*'-')
    
    else:
        print(10*'--')
        print("""
        
        OPÇÃO / DADO INVÁLIDO!
         
           """)
        print(10*'--')