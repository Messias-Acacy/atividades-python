lista = []

for x in range(5):
    numero = int(input(f'digite o  valor da posição {x} do vetor'))
    lista.append(numero)
print(lista)

maior = lista[0]
menor = lista[0]


for z in range(5):
    if maior < lista[z]:
        maior = lista[z]
    if menor > lista[z]:
        menor = lista[z]
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
print(f'a lista é: {lista}')