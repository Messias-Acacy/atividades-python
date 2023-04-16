nota=0
nota_total=0
numero_alunos = int(input('Digite o número de alunos: '))
for c in range(1,numero_alunos+1,1):
    nota = float(input(f'Qual a nota do {c} Aluno?'))
    nota_total = nota + nota_total
print(f'O A média da turma é: {nota_total/c}')