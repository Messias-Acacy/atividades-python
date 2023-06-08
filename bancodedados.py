encerrar = 'no'
nome_item = []
preco_item = []
ID_item = []
while True:
    print('SISTEMA DE ITENS')
    
    
    print("""

    [1] - ADICIONAR ITEM 
    [2] - PESQUISAR ITEM POR PREÇO OU ID
    [3] - ENCERRAR SISTEMA

    """)
    pesquisa = input('Selecione a opção: ')
    while pesquisa not in '1,2,3':
        print("""

        [1] - ADICIONAR ITEM 
        [2] - PESQUISAR ITEM POR PREÇO OU ID

        """,)
        pesquisa = input('Selecione a opção entre 1 e 3: ')


    match pesquisa:
        case '1':
            quantidade = int(input('Quantos itens você quer adicionar? '))
            for x in range(quantidade):
                escrever = input(f'digite o nome do {x+1} ítem: ')
                nome_item.append(escrever)
                escrever = input(f'digite o preço do {x+1} item:  ')
                preco_item.append(escrever)
                escrever = input(f'digite o ID do {x+1} item: ')
                ID_item.append(escrever)
                escrever = ''
        case '2':
            procurar = input('Digite o nome ou o ID do produto: ')
            for y in range(len(nome_item)):
                if procurar in nome_item[y] or procurar in ID_item[y]:
                    print(10*'-')
                    print(f"Nome do produto: {nome_item[y]}")
                    print(f"Preço do produto: {preco_item[y]}")
                    print(f"ID do produto: {ID_item[y]}")
                    print(10*'-')
        case '3':
            print('Ao usar essa função todos os itens do sistema sumirão para sempre! ')
            encerrar = input('Encerrar mesmo assim? Digite exatamente SIM')
            if encerrar == 'SIM':
                print('PROGRAMA ENCERRADO!')
                break



