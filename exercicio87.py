matriz = [[],[],[]]
somador_par = 0
somador_coluna = 0
somador_linha = 0


for x in range(3):
    for y in range(3):
        matriz[x].append(int(input(f'digite o {y+1} valor da posicao {x} aqui: ')))
    print()

maior_linha = matriz[1][0]

for z in range(3):
    for a in range(3):
        if matriz[z][a] %2 == 0 and matriz[z][a]!= 0:
            somador_par = somador_par + matriz[z][a]
        print(f'[{matriz[z][a]}]',end=' ')
    print()
    
    if matriz[1][z] > maior_linha:
        maior_linha = matriz[1][z]
   
    somador_coluna+=matriz[z][2]

print()
print(f'A soma dos valores pares é: {somador_par}')
print(f'A soma da terceira coluna é: {somador_coluna}')
print(f'O maior valor da segunda linha é: {maior_linha}')







    