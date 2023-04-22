vetor = []
contador = 0
somador = 0
for x in range (5):
   vetor.append(int(input(f'Digite a nota do {x+1} aluno: ')))
   somador = somador + vetor[x]
   if vetor[x] >= 7:
      contador = contador + 1
media = somador/(x+1)
print(f'a media da turma é de: {media} e {contador} ficaram acima da média.')







