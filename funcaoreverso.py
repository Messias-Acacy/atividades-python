def funcao_contrario(texto):
    cont = 0
    cont2= 0
    for x in texto:
        if x !=' ':
            cont=cont+1
        cont2+=1
    print(f'Seu texto tem {cont} letras')
    print('o texto ao contrário fica: ')
    for y in range(cont2-1,-1,-1):
        print(f'{texto[y]}', end=' ')

texto = input('digite o texto aqui: ')
print(funcao_contrario(texto))