vetor = []

while True:
    n = int(input('arara: '))
    if n not in vetor:
        vetor.append(n)
        print(vetor)
    confirmador = input('quer continuar? [S/N]')
    if confirmador in 'nN':
        break