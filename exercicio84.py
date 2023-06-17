vetor_pessoa = []
vetor_peso = []

while True:
    vetor_pessoa.append(input('Nome: '))
    vetor_peso.append(int(input('Peso: ')))
    confirm = input('Quer continuar? [S/N]: ')
    if confirm not in 'SIMsimsSYESyesYy':
        break

maior = vetor_peso[0]
menor = vetor_peso[0]

print(f'Você cadastrou {len(vetor_pessoa)} pessoas')

for x in range(len(vetor_pessoa)):
    if vetor_peso [x]> maior:
        maior = vetor_peso[x]
    if vetor_peso[x] < menor:
        menor = vetor_peso[x]

print(f'O maior peso foi de {maior} KG que contempla o peso de:',end=' ')
for y in range(len(vetor_pessoa)):
    if vetor_peso[y] == maior:
        print(vetor_pessoa[y], end=' ')
print()
print(f'O menor peso foi de {menor} KG que contempla o peso de:',end=' ')

for z in range(len(vetor_pessoa)): 
    if vetor_peso[z] == menor:
        print(vetor_pessoa[z], end=' ')




