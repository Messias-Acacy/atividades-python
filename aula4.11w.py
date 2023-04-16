c_w = 0 # esse é o número de dados q eu vou usar
t_n = 0 #total de números
while c_w <9: # esse <9 é porque o primeiro valor de c_w (contador de while) é 0
    numero = int(input('digite um valor aqui: '))
    t_n= t_n+numero
    c_w = c_w+1
print(f' a média entre esses 10 números é: {t_n/c_w}')

