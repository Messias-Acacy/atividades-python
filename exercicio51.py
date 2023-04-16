p = int(input('digite aqui o primeiro termo: '))
r = int(input('razão: '))
d_c = int(input('digite o  valor do termo que quer calcular '))
d = p+(d_c-1)*r
for c in range (p,d+r,r):
    print(f"{c}", end='=> ')
print('terminado!')