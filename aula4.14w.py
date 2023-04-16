av1= int(input('digite aqui o valor da avaliação 1: '))
av2= int(input('digite aqui o valor da avaliação 2: '))
while av1 < 0 or av1 >10 or av2 <0 or av2 >10:
    print('Só são aceitos valores entre 0 a 10 para qualquer uma das avaliações')
    av1= int(input('digite aqui o valor da avaliação 1: '))
    av2= int(input('digite aqui o valor da avaliação 2: '))
media = (av1+av2)/2
print(f'a média desse aluno foi: {media}')
