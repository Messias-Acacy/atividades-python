nome = []
senha = []
for x in range(5):
    nome.append(input('digite o nome aqui: '))
    senha.append(input('digite a senha aqui: '))

for y in range (5):
    print(f'Usuário: {nome[y]} Senha: {senha[y]} estão na posição {y} ')
    print()