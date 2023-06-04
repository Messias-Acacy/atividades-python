def Intervalo_Primo(numero_inicial,numero_final):
    contador_primo = 0
    print(f'Números primos no intervalo de {numero_inicial} a {numero_final}\n')

    for y in range(numero_inicial,numero_final+1):
        for x in range(1,numero_final+1):
            if y % x == 0 and y != 0:
                contador_primo+=1
        if contador_primo == 2:
            print(y, end =' ')
        else:
            contador_primo = 0

print(Intervalo_Primo(1,50))