#f_i = fora do intervalo
# d_i = dentro do intervalo
f_i = 0
d_i=0
for c in range (1,11):
    valor = int(input('digite o valor aqui: '))
    f_i+=1
    if valor > 9 and valor <21:
        d_i+=1
print(f'dentro do intervalo  de 10 e 20 você tem {d_i} e fora você tem {f_i-d_i}')
#f_i = 0
#d_i=0
#for c in range (1,11):
#    valor = int(input('digite o valor aqui: '))
#    if valor > 9 and valor <21:
#        d_i+=1
#    else:
#        f_i+=1
#print(f'dentro do intervalo você tem {d_i} e fora você tem {f_i}')