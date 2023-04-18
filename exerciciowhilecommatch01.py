dinheiro = float(input('Digite um valor para fazer as compras!'))
condicao = 0
saldo = 0 + dinheiro
while condicao == 0:
    print(f""" MENU DE OPÇÕES
    Saldo atual: {saldo}
    [1] - MILK SHAKE > R$ 12.00
    [2] - CAMISA POLO > R$ 15.00
    [3] - QUEIJO PREMIUM > RS 50.00/KG
    [4] - CAMISA SOCIAL > R$ 35.00

    DIGITE QUALQUER OUTRA COISA PARA SAIR DO MENU DE OPÇÕES
    Exp: SAIR

    """)
    opcao = input('digite uma opção do menu aqui >>> ')
    
    match opcao:

        case '1':
            quantidade = int(input('Quantos você quer comprar? '))
            saldo = saldo - (quantidade*12)
            print(f'Você comprou {quantidade} MILK SHAKE(S) por {saldo}')
            if saldo <= 0:
                print("Você não tem mais saldo!")
                confirmacao = input('Deseja reabastecer seu valor para  continuar comprando?  digite S para confirmar\nOU digite qualquer coisa para encerrar o programa: ').upper().strip()[0]
                if confirmacao == 'S':
                    condicao = 0
                    dinheiro = float(input('Digite um valor para fazer as compras!'))
                    saldo = saldo+dinheiro

                else: 
                    condicao = 1
                    print('programa encerrado!')

        case '2':
            quantidade = int(input('Quantos você quer comprar? '))
            saldo = saldo - quantidade*15.00
            print(f'Você comprou {quantidade} CAMISA(S) POLO(S) por {saldo}')
            if saldo <= 0:
                print("Você não tem mais saldo!")
                confirmacao = input('Deseja reabastecer seu valor para  continuar comprando? digite S para confirmar\nOU digite qualquer coisa para encerrar o programa').upper().strip()[0]
                if confirmacao == 'S':
                    condicao = 0
                    dinheiro = float(input('Digite um valor para fazer as compras!'))
                    saldo = saldo+dinheiro

                else: 
                    condicao = 1
                    print('programa encerrado!')
            
        case '3':
            quantidade = float(input('Quantos quilos você quer comprar? '))
            saldo = saldo - quantidade*50.00
            print(f'Você comprou {quantidade} KG de  QUEIJO PREMIUM  por {saldo}')
            if saldo <= 0:
                print("Você não tem mais saldo!")
                confirmacao = input('Deseja reabastecer seu valor para  continuar comprando? digite S para confirmar\nOU digite qualquer coisa para encerrar o programa').upper().strip()[0]
                if confirmacao == 'S':
                    condicao = 0
                    dinheiro = float(input('Digite um valor para fazer as compras!'))
                    saldo = saldo+dinheiro

                else: 
                    condicao = 1
                    print('programa encerrado!')

        case '4': 
            quantidade = int(input('Quantos você quer comprar? '))
            saldo = saldo - quantidade*35.00
            print(f'Você comprou {quantidade} CAMISA(S)  SOCIAL(IS) por {saldo}')
            if saldo <= 0:
                print("Você não tem mais saldo!")
                confirmacao = input('Deseja reabastecer seu valor para  continuar comprando? digite S para confirmar\nOU digite qualquer coisa para encerrar o programa').upper().strip()[0]
                if confirmacao == 'S':
                    condicao = 0
                    dinheiro = float(input('Digite um valor para fazer as compras!'))
                    saldo = saldo+dinheiro

                else: 
                    condicao = 1
                    print('programa encerrado!')

        case _:
            print('Programa encerrado!')
            condicao = 1