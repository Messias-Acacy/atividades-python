vetor_a = []
cont = 0
numero = int(input('digite um número aqui: '))
print(20*'=')
for x in range (30):
    vetor_a.append(int(input(f'digite o {x+1} número do vetor_a: ')))
    if vetor_a[x] == numero:
        cont = cont +1
print(f'o número {numero} apareceu {cont} vezes.')