matriz = [[],[],[]]

for x in range(3):
    for y in range(3):
        matriz[x].append(int(input(f'digite o {y+1} valor da posicao {x} aqui: ')))
    print()

for z in range(3):
    for e in range(3):
        print(f'[{matriz[z][e]}]',end=' ')
    print()
    