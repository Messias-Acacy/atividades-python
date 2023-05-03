confirm = 'Sim'
while confirm =='Sim':
    tempo = input('a partida começou e terminou no mesmo dia?[S/N]')
    while tempo !='S' and tempo != 'N':
        tempo = input('Confirme apenas com  S/N >>> ')
    Hora_inicio = int(input('digite a hora de início: '))
    Hora_Termino = int(input('digite a hora de termino: '))

    if tempo =='S':
        calculo = Hora_Termino-Hora_inicio
        
        if calculo < 0:
            print(f'o jogo durou: {(calculo)*-1} horas')
        elif calculo > 24:
            print('um jogo de xadrez não dura mais que 24 horas')
        else:
            print(f'O jogo durou: {calculo} horas')
    if tempo =='N':
        Hora_inicio = 24 - Hora_inicio

        calculo = Hora_Termino+Hora_inicio

    if Hora_Termino > Hora_inicio:
        print('o jogo excedeu 24 horas')
        
    else:
        print(f'o jogo durou exatamente: {calculo} horas.')
    confirm = input('quer continuar? digite exatamente "Sim": ')
print('Programa encerrado!')