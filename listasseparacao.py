lista = []
lista_impar = []
lista_par = []
quantidade_numero = int(input('Digite a quantidade de valores a serem colocados na lista: '))
for x in range(1,quantidade_numero+1):
    lista.append(int(input(f'Digite aqui o {x} da lista: ')))

for y in range(quantidade_numero):
    if lista[y] != 0:
        if lista[y] % 2 != 0:
            lista_impar.append(lista[y])
        else:
            lista_par.append(lista[y])

print(lista)
print(lista_impar)
print(lista_par)
