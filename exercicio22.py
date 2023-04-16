nome = input('digite seu nome: ').strip() #o ponto strip tira os espaços inúteis antes e depois
print(f'seu nome em maíúsculo é: {nome.upper()}')
print(f'seu nome em maíúsculo é: {nome.lower()}')
nome_semspace = nome.count(' ') #criadas para fins educacionais
nome_comspace = len(nome)  # criacadas para fins educacionais
print (f"o seu nome tem {len(nome) - nome.count(' ')} no total sem contar os espaços.") # se tiver ('')  coloque "".
nome_i = nome.split() #lembre-se que isso cria uma lista e o [] vai puxar o primeiro elemento da lista
print(f'o seu nome inicial é {nome.split()[0]} e tem {len(nome.split()[0])} letras') # tirei a variavel para fins educacionais
#print('seu nome inicial tem {} letras'.format(nome.find(' '))) outra maneira de achar o nome procurando pelo primeiro espaço



