#o conceito de lista, q é basicamente um vetor q agrega várias variáveis. O choice faz uma escolha refente a um elemento da lista
from random import choice
nome1 = input('digite o nome do primeiro aluno aq: ')
nome2 = input('digite o nome do segundo aluno aq: ')
nome3 = input('digite o nome do terceiro aluno aq: ')
nome4 = input('digite o nome do quarto aluno aq: ')
lista_alunos = [nome1,nome2,nome3,nome4]
print(f'O escolhido para isso foi {choice(lista_alunos)}!')
