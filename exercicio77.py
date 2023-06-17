tupla = ('programador','aprender','dançar','cantar','python')
contador_tupla = 0

for x in tupla:
    print(f'Na palavra {tupla[contador_tupla]} temos as vogais: ')
    for y in range(len(x)):
        if tupla[contador_tupla][y] in 'aeiou':
            print(tupla[contador_tupla][y], end=' ')
    contador_tupla+=1
    print()