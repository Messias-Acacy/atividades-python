numero_1 = int(input('Escreva o primeiro valor: '))
numero_2 = int(input('Escreva o segundo valor: '))
valor =0
while valor !=5: # vc pode usar while true
    print("""MENU 
    [ 1 ] somar 
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números 
    [ 5 ] sair do programa""")
    valor = int(input('digite uma opção aqui: '))
    if valor == 1:
        print(f'a soma entre {numero_1}+{numero_2}={numero_1+numero_2}')
    elif valor == 2:
        print(f'a soma entre {numero_1}*{numero_2}={numero_1*numero_2}')
    elif valor == 3:
        if numero_2>numero_1:
            print(f' O maior número é: {numero_2}')
        else:
            print(f' O maior número é: {numero_1}')
    elif valor == 4:
        numero_1 = int(input('Escreva o primeiro valor: '))
        numero_2 = int(input('Escreva o segundo valor: '))
    elif valor == 5:
        valor = 5 # se usar while true, digite apenas break aqui e o programa vai encerrar.
    else:
        print('Digite um número de 1 a 5!')


        

