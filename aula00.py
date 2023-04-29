#nome = input('digite o nome: ')
#contador = 1
#for x in nome:
#    print(f'{x}-{contador}')
#    contador+=1

#contador = 0
#for x in nome:
#    contador+=1
#for y in range(contador-1,-1,-1):
#    print(nome[y])

nome = input('digite o nome: ')
contador = 0
reverso = 0
for x in nome:
    contador+=1
for y in range(contador-1,-1,-1):
    print(f'{nome[reverso]} >>> {nome[y]}')
    reverso=reverso+1