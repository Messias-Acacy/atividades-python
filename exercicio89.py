temp = []
lista = []
contador_aluno = 0
while True:
    temp.append(input('Nome: '))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    lista.append(temp[:])
    temp = []
    confirm = input('Quer continuar? [S/N]: ')
    contador_aluno+=1
    if confirm not in "SIMsimYESyesYySs":
        break


print('=='*10)
print(f'{"No":<4} {"Aluno":<10}{"MÉDIA":^8}')
print('-'*13)

for posicao_alunos in range(contador_aluno):
    for alunos in range(2):
        if alunos == 0:
            print(f'{posicao_alunos:<4}',end='')
            print(f' {lista[posicao_alunos][alunos]:<10}',end='')
        else:
            media =(lista[posicao_alunos][alunos]+lista[posicao_alunos][alunos+1])/2
            print(f'{media:^8}',end='')
    print()

print('-'*19)
nota_aluno = int(input('Digite No para verificar a nota do aluno: [999 interrompe]: '))
while nota_aluno != 999:
    if nota_aluno >= contador_aluno:
        print('Aluno não encontrado!')
        nota_aluno = int(input('Digite No para verificar a nota do aluno: [999 interrompe]: '))
        continue
    else:
        print(f'O aluno: {lista[nota_aluno][0]} tem notas: {lista[nota_aluno][1:]}')
        nota_aluno = int(input('Digite No para verificar a nota do aluno: [999 interrompe]: '))
        
print('programa encerrado!')