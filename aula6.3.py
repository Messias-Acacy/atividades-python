n_alunos = int(input('digite o número de alunos: '))
lista_alunos = []

for x in range (n_alunos):
    lista_alunos.append(input(f'digite o nome do {x+1} Aluno: '))

nome = input('qual o nome do aluno que você quer procurar?')

for y in range(n_alunos):
    if lista_alunos[y] == nome:
        print(f'{lista_alunos[y]} está na {y} posição')
