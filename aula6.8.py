nome = []
senha = []
for x in range(2):
    nome.append(input('digite o nome aqui: '))
    senha.append(input('digite a senha aqui: '))

print(20*'=')
password = input('digite  a sua senha: ')

for y in range (2):
    if (senha[y]) == password:
        print(f'você está logado! Bem-vindo, {nome[y]}')
        break
print('Senha incorreta')