from random import shuffle
nome1 = str(input('digite o nome do primeiro aluno aq: '))
nome2 = str(input('digite o nome do segundo aluno aq: '))
nome3 = str(input('digite o nome do terceiro aluno aq: '))
nome4 = str(input('digite o nome do quarto aluno aq: '))
lista_alunos = [nome1,nome2,nome3,nome4]
shuffle(lista_alunos)
print(f'os ecolhidos foram colocados nessa ordem: {lista_alunos}!')
