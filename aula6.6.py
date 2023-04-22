vetor_a = []
vetor_inverso = []
n = int(input('digite a  quantidade de números do vetor: '))
for x in range (n):
    vetor_a.append(input('escreva aq: '))
contador = 0
for y  in range(n):
    contador = contador -1
    vetor_inverso.append(vetor_a[(n-1)-y])
print(vetor_inverso)
