quantidade = int(input("digitea quantidade de losangulos-> "))
tamanho = int(input("digite o tamanho do losangulos -> "))

for quantidade_losangos in range(quantidade):
    for tamanho_atual in range(1,tamanho+1):
        for espaco in range(tamanho_atual,tamanho+1):
            print(' ', end='')
        for asterisco_local in range(tamanho_atual):
            if tamanho_atual > 2 and asterisco_local > 0 and asterisco_local < tamanho_atual-1:
                print(' ',end=' ')
            else:
                print('*',end=' ')
        print()
    espaco_inverso = tamanho-1
    inverso_contador = 2
    for tamanho_inverso in range(tamanho-1):
        print(' '*inverso_contador,end='')
        for asterisco_local_inverso in range(tamanho-1,tamanho_inverso,-1):
            if (asterisco_local_inverso != tamanho-1) and (asterisco_local_inverso >= inverso_contador and asterisco_local_inverso != tamanho-1):
                print(' ',end=' ')
            else:
                print('*',end=' ')
        print()
        inverso_contador+=1