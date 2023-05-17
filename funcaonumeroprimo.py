def funcao_primo(numero):
    cont_primo = 0
    if numero != 1:
        for x in range(1,numero+1):
                if numero%x == 0:
                    cont_primo+=1
        if cont_primo >2:
            print('o número não é primo')
        else:
            print('o número é primo')
    else:
         print('o número nao é primo')

while True:
    numero = int(input('digite o número aqui: '))
    print(funcao_primo(numero))
    confirmar = input('deseja continuar? [S/N]: ')
    if confirmar not in 'SsimYESSIMSim':
        break