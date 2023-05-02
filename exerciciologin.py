#faça um codigo pro usuário digitar 3 vezes o nome e a senha e se ele errar o sistma bloqueia, mas se
#ele acertar, o programa encerra com ele logado!

nome = 'rodrigo'
senha = 1234
contador = 0
for x in range(3):
    contador = contador+1
    login = input('digite o nome aqui: ')
    password = int(input('digite a senha aqui: '))
    if login == nome and password == senha:
        print('Logado com sucesso!')
        break
    else:
        if contador != 3:
            print('login invalido. tente de novo')
        else: 
            print('acesso bloqueado')
            break

