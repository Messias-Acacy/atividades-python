estrelas = int(input('digite aqui a quantidade de *: '))
vezes = int(input('Quantas vezes isso vai ocorrer? '))

for y in range(vezes):
    for x in range(1,estrelas+1):
        print(x*'*')
    for z in range(estrelas-1,0,-1):
        print(z*'*')