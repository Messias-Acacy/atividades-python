numero = int(input('digite o número aqui: '))
n_divid = 0
for c in range (1,numero+1):
    if numero%c==0:
        n_divid=n_divid+1
if n_divid == 2:
    print('o número é primo')
else:
    print('o número não é primo')
