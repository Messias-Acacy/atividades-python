n = int(input('digite o valor para o número dos vetores: '))
vetor_a = []
vetor_b = []
vetor_soma = []
for x in range (n):
    vetor_a.append(int(input(f'digite o {x+1} valor do Vetor_a: ')))
print(20*'=')
for y in range (n):
    vetor_b.append(int(input(f'digite o {y+1} valor do Vetor_b: ')))
for z in range(n):
    vetor_soma.append(vetor_a[z]+vetor_b[z])
print(vetor_soma)
