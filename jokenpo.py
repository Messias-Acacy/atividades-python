from random import randint
print(""" Escolha entre 1 - ✂, 2 - 🧻, 3 - 🥌""")
while True:
    escolha_inimigo = randint(1,3)
    escolha = int(input('Digite a opção aqui: '))
    while escolha <1 or escolha > 3:
        print('digite uma opção entre 1 e 3!')
        escolha = int(input('Digite a opção aqui: '))

    um ='✂'
    dois = '🧻'
    tres =  '🥌'


    if escolha_inimigo ==1:
        if escolha ==1:
            print(f'O inimigo escolheu {um} ! Empate!')
        elif escolha ==2:
            print(f'O inimigo escolheu {um} ! Você perdeu!!')
        else:
            print(f'O inimigo escolheu {um} ! Você ganhou!')
    elif escolha_inimigo ==2:
        if escolha ==1:
            print(f'O inimigo escolheu {dois} !Você venceu!')
        elif escolha ==2:
            print(f'O inimigo escolheu {dois} !Empate!')
        else:
            print(f'O inimigo escolheu {dois} ! Você perdeu!')
    else:
        if escolha ==1:
            print(f'O inimigo escolheu {tres} ! Você perdeu!')
        elif escolha ==2:
            print(f'O inimigo escolheu {tres} !Você ganhou! ')
        else:
            print(f'O inimigo escolheu {tres} ! Empate!')

