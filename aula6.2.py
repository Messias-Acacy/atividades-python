n_alunos = int(input('digite o número de alunos: '))
lista_alunos = []

for x in range (n_alunos):
    lista_alunos.append(input(f'digite o nome do {x+1} Aluno: '))

for y in range (n_alunos):
   print(lista_alunos[y],'-',y)