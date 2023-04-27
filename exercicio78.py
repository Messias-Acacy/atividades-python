vetor = []
maior_valor = 0
menor_valor = 0
n = 1
for x in range(5):
    vetor.append(int(input(f'digite aqui o {x+1}: ')))

for y in range(5):   
    if n ==1:
        maior_valor = vetor[y]
        menor_valor = vetor[y]
    n = 0    
    if vetor[y] > maior_valor:
        maior_valor = vetor[y]
    
    if vetor[y] < menor_valor:
        menor_valor = vetor[y]

    
for h in range(5):
    if vetor[h] == maior_valor:
        print(f'O maior valor foi: {vetor[h]} na posição {h}')
    if vetor[h] == menor_valor:
        print(f'O  maior valor foi: {vetor[h]} na posição {h}')