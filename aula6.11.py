vetor_a = []

for x in range (5):
    vetor_a.append(input(f'digite o  {x+1} nome: '))

for y in range (5):
    print(f'{vetor_a[y]} posição {y} >>>> {vetor_a[4-y]} posição {4-y}')