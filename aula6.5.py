vetor_a = []
vetor_m = []
for x in range (4):
    vetor_a.append(int(input(f'Digite o {x+1} número: ')))
multiplicador = int(input('digite um número aqui para multiplicar: '))

for y in range (4):
    vetor_m.append(vetor_a[y]*multiplicador)

print(vetor_m)

